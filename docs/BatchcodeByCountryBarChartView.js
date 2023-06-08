class BatchcodeByCountryBarChartView {

    #uiContainer;

    constructor(uiContainer) {
        this.#uiContainer = uiContainer
    }

    displayBatchcodeByCountryBarChart(barChartDescription) {
        const chartWithSlider = UIUtils.instantiateTemplate('template-chartWithSlider');
        const chartView = new BatchcodeByCountryBarChart(chartWithSlider.querySelector("canvas"));
        this.#uiContainer.appendChild(chartWithSlider);
        chartView.displayChart(barChartDescription);
    }
}
