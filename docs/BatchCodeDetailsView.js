class BatchCodeDetailsView {

    #uiContainer;
    #headingElement;
    #batchCodesSelectElement;
    #adverseReactionReportsChartView;
    #histogramChartView;
    #chartWithSlider;

    constructor(uiContainer) {
        this.#uiContainer = uiContainer
        this.#headingElement = this.#uiContainer.querySelector(".heading");
        this.#batchCodesSelectElement = new ElementWithSingleChangeEventListener(this.#uiContainer.querySelector("#batchCodesSelect"));
        this.#adverseReactionReportsChartView = new AdverseReactionReportsChartView(this.#uiContainer.querySelector('#adverseReactionReportsChartView'));
        this.#chartWithSlider = this.#uiContainer.querySelector('.chartWithSlider');
        this.#histogramChartView = new HistogramChartView(this.#chartWithSlider.querySelector("canvas"));
    }

    displayBatchCodeDetails(batchcode) {
        this
            .#loadHistoDescrs(batchcode)
            .then(histoDescrs => this.#displayHistogramViewForHistoDescrs(histoDescrs));
    }

    #loadHistoDescrs(batchcode) {
        const loadingText = document.createTextNode('Loading...');
        this.#uiContainer.appendChild(loadingText);
        return HistoDescrsProvider
            .getHistoDescrs(batchcode)
            .then(histoDescrs => {
                loadingText.remove();
                return histoDescrs;
            });
    }

    #displayHistogramViewForHistoDescrs(histoDescrs) {
        this.#displayHeading(histoDescrs.batchcode, histoDescrs['Company']);
        this.#displayAdverseReactionReportsChart(histoDescrs);
        this.#displaySelectBatchcodeCombination(histoDescrs.histograms);
        this.#displayHistogram(histoDescrs.histograms[0]);
    }

    #displayHeading(batchcode, company) {
        this.#headingElement.textContent = `Frequencies of reported Symptoms for Batch Code Combinations containing ${batchcode} from ${company}`
    }

    #displayAdverseReactionReportsChart(histoDescrs) {
        this.#adverseReactionReportsChartView.displayChart(
            {
                'Adverse Reaction Reports': histoDescrs['Adverse Reaction Reports'],
                'Deaths': histoDescrs['Deaths'],
                'Disabilities': histoDescrs['Disabilities'],
                'Life Threatening Illnesses': histoDescrs['Life Threatening Illnesses']
            });
    }

    #displaySelectBatchcodeCombination(histograms) {
        BatchcodeCombinationSelection.configureSelectBatchcodeCombinationElement(
            {
                batchCodesSelectElement: this.#batchCodesSelectElement,
                histograms: histograms,
                onSelect: histoDescr => this.#displayHistogram(histoDescr)
            });
    }

    #displayHistogram(histoDescr) {
        this.#histogramChartView.displayChart(histoDescr);
        this.#createSlider(
            {
                sliderElement: this.#chartWithSlider.querySelector(".slider"),
                range: {
                    min: 0,
                    max: Object.keys(histoDescr.histogram).length
                },
                orientation: 'vertical',
                height: this.#chartWithSlider.querySelector("canvas").style.height,
                onUpdate: range => this.#histogramChartView.setData(this.#slice(histoDescr, range))
            });
    }

    #slice(histoDescr, { start, endInclusive }) {
        return {
            batchcodes: histoDescr.batchcodes,
            histogram: Utils.sliceDict(histoDescr.histogram, start, endInclusive + 1)
        };
    }

    #createSlider({ sliderElement, range, orientation, height = null, onUpdate }) {
        if ('noUiSlider' in sliderElement) {
            sliderElement.noUiSlider.destroy();
        }
        noUiSlider.create(
            sliderElement,
            {
                start: [range.min, range.max],
                connect: true,
                range: range,
                step: 1,
                orientation: orientation
            });
        sliderElement.noUiSlider.on(
            'update',
            ([start, endInclusive]) =>
                onUpdate(
                    {
                        start: parseInt(start, 10),
                        endInclusive: parseInt(endInclusive, 10)
                    }));
        if (height != null) {
            sliderElement.style.height = height;
        }
    }
}
