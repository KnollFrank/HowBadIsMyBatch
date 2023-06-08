class BatchcodeByCountryBarChartView {

    #uiContainer;

    constructor(uiContainer) {
        this.#uiContainer = uiContainer
    }

    displayBatchcodeByCountryBarChart(barChartDescription) {
        const chartWithSlider = UIUtils.instantiateTemplate('template-chartWithSlider');
        const chartView = new BatchcodeByCountryBarChartView2(chartWithSlider.querySelector("canvas"));
        this.#uiContainer.appendChild(chartWithSlider);
        this.#displayBarChart(barChartDescription, chartView);
    }

    #displayBarChart(barChartDescription, chartView) {
        chartView.displayChart(barChartDescription);
    }
}
