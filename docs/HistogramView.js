class HistogramView {

    #uiContainer;

    constructor(uiContainer) {
        this.#uiContainer = uiContainer
    }

    displayHistogramsForBatchcode(batchcode) {
        this
            .#loadHistoDescrsForBatchcode(batchcode)
            .then(histoDescrs => this.#displayHistograms(histoDescrs));
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

    #displayHistograms(histoDescrs) {
        this.#uiContainer.appendChild(document.createTextNode(histoDescrs.batchcode));
        for (const histoDescr of histoDescrs.histograms) {
            this.#displayHistogram(histoDescr);
        }
    }

    #displayHistogram(histoDescr) {
        // FK-TODO: brauchen Slider wie bei intensivstationen
        // FK-TODO: extract class for template-chartWithSlider
        const element = UIUtils.instantiateTemplate('template-chartWithSlider');
        const canvas = element.querySelector("canvas");
        this.#uiContainer.appendChild(element);
        const histogramChartView = new HistogramChartView(canvas);
        histogramChartView.displayChart(histoDescr);
    }
}