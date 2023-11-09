class SymptomVsSymptomChartViewInitializer {

    #symptomVsSymptomChartView;
    #symptomX;
    #symptomY;

    configureSymptomVsSymptomChart(
        { symptomSelectXElement, symptomSelectYElement, symptomVsSymptomChartViewElement },
        initializeSelectElement) {

        this.#symptomVsSymptomChartView = new SymptomVsSymptomChartView(symptomVsSymptomChartViewElement);
        {
            initializeSelectElement(
                {
                    selectElement: symptomSelectXElement,
                    onValueSelected: symptomX => {
                        this.#symptomX = symptomX;
                        this.#loadAndDisplayChart();
                    },
                    minimumInputLength: 4
                });
            this.#symptomX = null;
        }
        {
            initializeSelectElement(
                {
                    selectElement: symptomSelectYElement,
                    onValueSelected: symptomY => {
                        this.#symptomY = symptomY;
                        this.#loadAndDisplayChart();
                    },
                    minimumInputLength: 4
                });
            this.#symptomY = null;
        }
        this.#loadAndDisplayChart();
    }

    #loadAndDisplayChart() {
        if (this.#symptomX != null && this.#symptomY != null) {
            this.#symptomVsSymptomChartView.loadAndDisplayChart(this.#symptomX, this.#symptomY);
        }
    }
}