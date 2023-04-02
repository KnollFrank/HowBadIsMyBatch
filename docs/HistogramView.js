class HistogramView {

    #uiContainer;

    constructor(uiContainer) {
        this.#uiContainer = uiContainer
    }

    displayHistogramView(batchcode) {
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
        this.#displayHeading(histoDescrs.batchcode);
        const chartWithSlider = UIUtils.instantiateTemplate('template-chartWithSlider');
        const histogramChartView = new HistogramChartView(chartWithSlider.querySelector("canvas"));
        this.#displaySelectBatchcodeCombination(histoDescrs.histograms, histogramChartView, chartWithSlider);
        this.#uiContainer.appendChild(chartWithSlider);
        this.#displayHistogram(histoDescrs.histograms[0], histogramChartView, chartWithSlider);
    }

    #displayHeading(batchcode) {
        const h1 = document.createElement("h3");
        h1.appendChild(document.createTextNode(`Frequencies of reported Symptoms for Batch Code Combinations containing ${batchcode}`));
        this.#uiContainer.appendChild(h1);
    }

    #displaySelectBatchcodeCombination(histograms, histogramChartView, chartWithSlider) {
        const selectBatchcodeCombination =
            BatchcodeCombinationSelection.getSelectBatchcodeCombination(
                {
                    histograms: histograms,
                    onSelect: histoDescr => this.#displayHistogram(histoDescr, histogramChartView, chartWithSlider)
                });
        this.#uiContainer.appendChild(selectBatchcodeCombination);
    }

    #displayHistogram(histoDescr, histogramChartView, chartWithSlider) {
        histogramChartView.displayChart(histoDescr);
        this.#createSlider(
            {
                sliderElement: chartWithSlider.querySelector(".slider"),
                range: {
                    min: 0,
                    max: Object.keys(histoDescr.histogram).length
                },
                orientation: 'vertical',
                height: chartWithSlider.querySelector("canvas").style.height,
                onUpdate: range => histogramChartView.setData(this.#slice(histoDescr, range))
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
