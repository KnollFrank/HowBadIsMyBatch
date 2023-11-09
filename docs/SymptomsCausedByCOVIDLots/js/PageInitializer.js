class PageInitializer {

    static #symptomVsSymptomChartView;
    static #symptomX = null;
    static #symptomY = null;

    static initializePage({ symptom, vaccine, symptomVsSymptomChart }) {
        PageInitializer.#configureSymptom(symptom);
        PageInitializer.#configureVaccine(vaccine);
        PageInitializer.#configureSymptomVsSymptomChart(symptomVsSymptomChart);
    }

    static #configureSymptom({ symptomSelectElement, prrByVaccineTableElement, downloadPrrByVaccineTableButton }) {
        const prrByVaccineTableView = new PrrByVaccineTableView(prrByVaccineTableElement, downloadPrrByVaccineTableButton);
        PageInitializer.#initializeSelectElement(
            {
                selectElement: symptomSelectElement,
                onValueSelected: symptom => prrByVaccineTableView.displayPrrByVaccineTable4Symptom(symptom),
                minimumInputLength: 4
            });
    }

    static #configureVaccine({ vaccineSelectElement, prrBySymptomTableElement, downloadPrrBySymptomTableButton }) {
        const prrBySymptomTableView = new PrrBySymptomTableView(prrBySymptomTableElement, downloadPrrBySymptomTableButton);
        PageInitializer.#initializeSelectElement(
            {
                selectElement: vaccineSelectElement,
                onValueSelected: vaccine => prrBySymptomTableView.displayPrrBySymptomTable4Vaccine(vaccine),
                minimumInputLength: 4
            });
    }

    static #configureSymptomVsSymptomChart({ symptomSelectXElement, symptomSelectYElement, symptomVsSymptomChartViewElement }) {
        PageInitializer.#symptomVsSymptomChartView = new SymptomVsSymptomChartView(symptomVsSymptomChartViewElement);
        PageInitializer.#initializeSelectElement(
            {
                selectElement: symptomSelectXElement,
                onValueSelected: symptomX => {
                    PageInitializer.#symptomX = symptomX;
                    PageInitializer.#loadAndDisplayChart();
                },
                minimumInputLength: 4
            });
        PageInitializer.#initializeSelectElement(
            {
                selectElement: symptomSelectYElement,
                onValueSelected: symptomY => {
                    PageInitializer.#symptomY = symptomY;
                    PageInitializer.#loadAndDisplayChart();
                },
                minimumInputLength: 4
            });
        PageInitializer.#loadAndDisplayChart();
    }

    static #initializeSelectElement({ selectElement, onValueSelected, minimumInputLength }) {
        selectElement.select2({ minimumInputLength: minimumInputLength });
        selectElement.on(
            'select2:select',
            function (event) {
                const value = event.params.data.id;
                onValueSelected(value);
            });
    }

    static #loadAndDisplayChart() {
        if (PageInitializer.#symptomX != null && PageInitializer.#symptomY != null) {
            PageInitializer.#symptomVsSymptomChartView.loadAndDisplayChart(
                PageInitializer.#symptomX,
                PageInitializer.#symptomY);
        }
    }
}
