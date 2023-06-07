class BatchcodeByCountryBarChartView {

    #uiContainer;

    constructor(uiContainer) {
        this.#uiContainer = uiContainer
    }

    displayBatchcodeByCountryBarChart(batchcode) {
        this
            .#loadBarChartDescription(batchcode)
            .then(barChartDescription => this.#displayBatchcodeByCountryBarChart(barChartDescription));
    }

    #loadBarChartDescription(batchcode) {
        const loadingText = document.createTextNode('Loading...');
        this.#uiContainer.appendChild(loadingText);
        return BarChartDescriptionProvider
            .getBarChartDescription(batchcode)
            .then(barChartDescriptionTable => {
                loadingText.remove();
                return barChartDescriptionTable;
            });
    }

    #displayBatchcodeByCountryBarChart(barChartDescription) {
        this.#displayHeading(barChartDescription.batchcode);
        const chartWithSlider = UIUtils.instantiateTemplate('template-chartWithSlider');
        const chartView = new BatchcodeByCountryBarChartView2(chartWithSlider.querySelector("canvas"));
        this.#uiContainer.appendChild(chartWithSlider);
        this.#displayBarChart(barChartDescription, chartView);
    }

    #displayHeading(batchcode) {
        const h1 = document.createElement("h3");
        h1.appendChild(document.createTextNode(`Frequencies of reported Symptoms for Batch Code Combinations containing ${batchcode}`));
        this.#uiContainer.appendChild(h1);
    }

    #displayBarChart(barChartDescription, chartView) {
        chartView.displayChart(barChartDescription);
    }
}
