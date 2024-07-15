class PageInitializer {

    static initializePage({ symptom, vaccine, pdfButton }) {
        PageInitializer.#configureSymptom(symptom);
        PageInitializer.#configureVaccine(vaccine);
        PageInitializer.#configurePDFButton(pdfButton);
    }

    static #configureSymptom({ symptomSelectElement, urlSearchParam, prrByVaccineTableElement, downloadPrrByVaccineTableButton, keyColumnName }) {
        const prrByVaccineTableView = new PrrByVaccineTableView(prrByVaccineTableElement, downloadPrrByVaccineTableButton, keyColumnName);
        Select2.initializeSelectElement(
            {
                selectElement: symptomSelectElement,
                minimumInputLength: 0,
                textOfOption2Select: urlSearchParam.get(),
                onSelectOptionHavingValueAndText: (id, text) => {
                    prrByVaccineTableView.displayPrrByVaccineTable4Symptom(id, text);
                    urlSearchParam.set(text);
                }
            });
    }

    static #configureVaccine({ vaccineSelectElement, urlSearchParam, prrBySymptomTableElement, downloadPrrBySymptomTableButton, valueName }) {
        const prrBySymptomTableView = new PrrBySymptomTableView(prrBySymptomTableElement, downloadPrrBySymptomTableButton, valueName);
        Select2.initializeSelectElement(
            {
                selectElement: vaccineSelectElement,
                textOfOption2Select: urlSearchParam.get(),
                onSelectOptionHavingValueAndText: (id, text) => {
                    prrBySymptomTableView.displayPrrBySymptomTable4Vaccine(id, text);
                    urlSearchParam.set(text);
                },
                minimumInputLength: 0
            });
    }

    static #configurePDFButton(pdfButton) {
        pdfButton.addEventListener(
            'click',
            () => PdfCreator.createPdf().open());
    }
}
