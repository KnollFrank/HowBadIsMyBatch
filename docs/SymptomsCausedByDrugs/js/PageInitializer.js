class PageInitializer {

    static initializePage({ symptom, vaccine }) {
        PageInitializer.#configureSymptom(symptom);
        PageInitializer.#configureVaccine(vaccine);
    }

    static #configureSymptom({ symptomSelectElement, prrByVaccineTableElement, downloadPrrByVaccineTableButton, keyColumnName }) {
        const prrByVaccineTableView = new PrrByVaccineTableView(prrByVaccineTableElement, downloadPrrByVaccineTableButton, keyColumnName);
        PageInitializer.#initializeSelectElement(
            {
                selectElement: symptomSelectElement,
                onValueSelected: (id, text) => prrByVaccineTableView.displayPrrByVaccineTable4Symptom(id, text),
                minimumInputLength: 0
            });
    }

    static #configureVaccine({ vaccineSelectElement, prrBySymptomTableElement, downloadPrrBySymptomTableButton, valueName }) {
        const prrBySymptomTableView = new PrrBySymptomTableView(prrBySymptomTableElement, downloadPrrBySymptomTableButton, valueName);
        PageInitializer.#initializeSelectElement(
            {
                selectElement: vaccineSelectElement,
                onValueSelected: (id, text) => prrBySymptomTableView.displayPrrBySymptomTable4Vaccine(id ,text),
                minimumInputLength: 0
            });
    }

    static #initializeSelectElement({ selectElement, onValueSelected, minimumInputLength }) {
        selectElement.select2({ minimumInputLength: minimumInputLength });
        selectElement.on(
            'select2:select',
            function (event) {
                const id = event.params.data.id;
                const text = event.params.data.text;
                onValueSelected(id, text);
            });
    }
}
