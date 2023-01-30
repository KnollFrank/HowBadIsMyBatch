class HistogramView {

    #uiContainer;

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
        const chartWithSlider = UIUtils.instantiateTemplate('template-chartWithSlider');
        const histogramChartView = new HistogramChartView(chartWithSlider.querySelector("canvas"));
        this.#displaySelectBatchcodeCombination(histoDescrs.histograms, histogramChartView, chartWithSlider);
        this.#uiContainer.appendChild(chartWithSlider);
        this.#displayHistogram(histoDescrs.histograms[0], histogramChartView, chartWithSlider);
    }

    #displaySelectBatchcodeCombination(histograms, histogramChartView, chartWithSlider) {
        const selectBatchcodeCombination = UIUtils.instantiateTemplate('template-selectBatchcodeCombination');
        const batchcodesSelect = selectBatchcodeCombination.querySelector('#batchcodesSelect');
        this.#addBatchcodeCombinationOptions(batchcodesSelect, histograms);
        batchcodesSelect.addEventListener(
            'change',
            event => {
                const histoDescr = histograms[event.target.value];
                this.#displayHistogram(histoDescr, histogramChartView, chartWithSlider);
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