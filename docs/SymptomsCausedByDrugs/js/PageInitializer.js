class PageInitializer {

    static initializePage({ symptom, vaccine }) {
        PageInitializer.#configureSymptom(symptom);
        PageInitializer.#configureVaccine(vaccine);
    }

    static #configureSymptom({ symptomSelectElement, selectSymptom, prrByVaccineTableElement, downloadPrrByVaccineTableButton, keyColumnName }) {
        const prrByVaccineTableView = new PrrByVaccineTableView(prrByVaccineTableElement, downloadPrrByVaccineTableButton, keyColumnName);
        Select2.initializeSelectElement(
            {
                selectElement: symptomSelectElement,
                textOfOption2Select: selectSymptom,
                onValueSelected: (id, text) => prrByVaccineTableView.displayPrrByVaccineTable4Symptom(id, text),
                minimumInputLength: 0
            });
    }

    static #configureVaccine({ vaccineSelectElement, selectVaccine, prrBySymptomTableElement, downloadPrrBySymptomTableButton, valueName }) {
        const prrBySymptomTableView = new PrrBySymptomTableView(prrBySymptomTableElement, downloadPrrBySymptomTableButton, valueName);
        Select2.initializeSelectElement(
            {
                selectElement: vaccineSelectElement,
                textOfOption2Select: selectVaccine,
                onValueSelected: (id, text) => prrBySymptomTableView.displayPrrBySymptomTable4Vaccine(id, text),
                minimumInputLength: 0
            });
    }
}
