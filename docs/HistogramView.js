class HistogramView {

    #uiContainer;
    #chartWithSlider;
    #histogramChartView;

    constructor(uiContainer) {
        this.#uiContainer = uiContainer
    }

    displayHistogramViewForBatchcode(batchcode) {
        this
            .#loadHistoDescrsForBatchcode(batchcode)
            .then(histoDescrs => this.#displayHistogramViewForHistoDescrs(histoDescrs));
    }

    #loadHistoDescrsForBatchcode(batchcode) {
        const loadingText = document.createTextNode('Loading...');
        this.#uiContainer.appendChild(loadingText);
        return fetch(`data/histograms/${batchcode}.json`)
            .then(response => {
                loadingText.remove();
                return response.json();
            })
    }

    #displayHistogramViewForHistoDescrs(histoDescrs) {
        this.#displaySelectBatchcodeCombination(histoDescrs.histograms);
        this.#chartWithSlider = UIUtils.instantiateTemplate('template-chartWithSlider');
        this.#uiContainer.appendChild(this.#chartWithSlider);
        this.#histogramChartView = new HistogramChartView(this.#getCanvas());
        this.#displayHistogram(histoDescrs.histograms[0]);
    }

    #getCanvas() {
        return this.#chartWithSlider.querySelector("canvas");
    }

    #displaySelectBatchcodeCombination(histograms) {
        const selectBatchcodeCombination = UIUtils.instantiateTemplate('template-selectBatchcodeCombination');
        const batchcodesSelect = selectBatchcodeCombination.querySelector('#batchcodesSelect');
        this.#addBatchcodeCombinationOptions(batchcodesSelect, histograms);
        batchcodesSelect.addEventListener(
            'change',
            event => {
                const histoDescr = histograms[event.target.value];
                this.#displayHistogram(histoDescr);
            });
        this.#uiContainer.appendChild(selectBatchcodeCombination);
    }

    #addBatchcodeCombinationOptions(batchcodesSelect, histograms) {
        this.#getBatchcodeCombinationOptions(histograms).forEach(option => batchcodesSelect.add(option));
    }

    #getBatchcodeCombinationOptions(histograms) {
        // FK-TODO: zuerst das Histogramm für den einzelnen batchcode, dann batchcodes-Array-Länge 2, 3, 4, ...
        return histograms.map(this.#getBatchcodeCombinationOption);
    }

    #getBatchcodeCombinationOption(histoDescr, index) {
        const option = document.createElement("option");
        option.text = histoDescr.batchcodes.join(', ');
        option.value = index;
        return option;
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
                height: this.#getCanvas().style.height,
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