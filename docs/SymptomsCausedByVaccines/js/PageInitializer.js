class PageInitializer {

    static initializePage({ symptom, vaccine }) {
        PageInitializer.#configureSymptom(symptom);
        PageInitializer.#configureVaccine(vaccine);
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
                minimumInputLength: 0
            });
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
}
