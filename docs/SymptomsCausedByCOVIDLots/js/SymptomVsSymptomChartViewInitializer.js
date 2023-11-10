class SymptomVsSymptomChartViewInitializer {

    #symptomVsSymptomChartView;
    #symptomX;
    #symptomY;
    #batches;
    #data;
    #downloadSymptomVsSymptomChartButton;

    configureSymptomVsSymptomChart(
        { symptomSelectXElement, symptomSelectYElement, symptomVsSymptomChartViewElement, downloadSymptomVsSymptomChartButton },
        initializeSelectElement) {

        this.#initializeButton(downloadSymptomVsSymptomChartButton);
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
        UIUtils.disableButton(this.#downloadSymptomVsSymptomChartButton);
        if (this.#symptomX == null || this.#symptomY == null) {
            return;
        }

        this.#symptomVsSymptomChartView
            .loadAndDisplayChart(this.#symptomX, this.#symptomY)
            .then(({ labels, data }) => {
                this.#batches = labels;
                this.#data = data;
                UIUtils.enableButton(this.#downloadSymptomVsSymptomChartButton);
            });
    }

    #initializeButton(downloadSymptomVsSymptomChartButton) {
        this.#downloadSymptomVsSymptomChartButton = downloadSymptomVsSymptomChartButton;
        UIUtils.disableButton(downloadSymptomVsSymptomChartButton);
        downloadSymptomVsSymptomChartButton.addEventListener(
            'click',
            () => this.#downloadSymptomVsSymptomChart())
    }

    #downloadSymptomVsSymptomChart() {
        UIUtils.downloadUrlAsFilename(
            window.URL.createObjectURL(
                new Blob(
                    [
                        ScatterChart2CsvConverter.convertScatterChart2Csv(
                            {
                                symptomX: this.#symptomX,
                                symptomY: this.#symptomY,
                                batches: this.#batches,
                                data: this.#data
                            }
                        )
                    ],
                    { type: 'text/csv' })),
            `${this.#symptomX} Vs ${this.#symptomY}`
        );
    }
}