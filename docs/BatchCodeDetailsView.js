class BatchCodeDetailsView {

    #uiContainer;
    #adverseReactionReportsChartView;
    #histogramTable;

    constructor(uiContainer) {
        this.#uiContainer = uiContainer
        this.#adverseReactionReportsChartView = new AdverseReactionReportsChartView(this.#uiContainer.querySelector('#adverseReactionReportsChartView'));
        this.#histogramTable = new HistogramTable($('#histogramTable'));
        this.#histogramTable.initialize();
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
        this.#adverseReactionReportsChartView.displayChart(histoDescrs);
        this.#histogramTable.display(histoDescrs.histogram);
    }
}
