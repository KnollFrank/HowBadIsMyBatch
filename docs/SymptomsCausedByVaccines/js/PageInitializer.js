class PageInitializer {

    static initializePage({ symptomSelectElement, prrByVaccineTableElement }) {
        const prrByVaccineTableView = new PrrByVaccineTableView(prrByVaccineTableElement);
        PageInitializer.#initializeSymptomSelectElement(
            {
                symptomSelectElement: symptomSelectElement,
                onSymptomSelected: symptom => prrByVaccineTableView.displayPrrByVaccineTable4Symptom(symptom)
            });
    }

    static #initializeSymptomSelectElement({ symptomSelectElement, onSymptomSelected }) {
        symptomSelectElement.select2({ minimumInputLength: 4 });
        symptomSelectElement.on(
            'select2:select',
            function (event) {
                const symptom = event.params.data.id;
                onSymptomSelected(symptom);
            });
        symptomSelectElement.select2('open');
    }
}
