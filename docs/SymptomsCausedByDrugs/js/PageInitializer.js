class PageInitializer {

    static initializePage({ symptom, vaccine }) {
        PageInitializer.#configureSymptom(symptom);
        PageInitializer.#configureVaccine(vaccine);
    }

    static #configureSymptom({ symptomSelectElement, searchParam, prrByVaccineTableElement, downloadPrrByVaccineTableButton, keyColumnName }) {
        const prrByVaccineTableView = new PrrByVaccineTableView(prrByVaccineTableElement, downloadPrrByVaccineTableButton, keyColumnName);
        Select2.initializeSelectElement(
            {
                selectElement: symptomSelectElement,
                textOfOption2Select: searchParam.get(),
                onValueSelected: (id, text) => {
                    prrByVaccineTableView.displayPrrByVaccineTable4Symptom(id, text);
                    searchParam.set(text);
                },
                minimumInputLength: 0
            });
    }

    static #configureVaccine({ vaccineSelectElement, searchParam, prrBySymptomTableElement, downloadPrrBySymptomTableButton, valueName }) {
        const prrBySymptomTableView = new PrrBySymptomTableView(prrBySymptomTableElement, downloadPrrBySymptomTableButton, valueName);
        Select2.initializeSelectElement(
            {
                selectElement: vaccineSelectElement,
                textOfOption2Select: searchParam.get(),
                onValueSelected: (id, text) => {
                    prrBySymptomTableView.displayPrrBySymptomTable4Vaccine(id, text);
                    searchParam.set(text);
                },
                minimumInputLength: 0
            });
    }
}
