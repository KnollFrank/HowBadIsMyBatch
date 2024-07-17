class PageInitializer {

    static initializePage({ symptom, vaccine, pdf }) {
        const prrByVaccineTableView = PageInitializer.#configureSymptom(symptom);
        const prrBySymptomTableView = PageInitializer.#configureVaccine(vaccine);
        PageInitializer.#configurePDFButton(
            {
                pdf,
                symptom: {
                    selectElement: symptom.symptomSelectElement,
                    table: prrByVaccineTableView.getTable()
                },
                vaccine: {
                    selectElement: vaccine.vaccineSelectElement,
                    table: prrBySymptomTableView.getTable()
                }
            });
    }

    static #configureSymptom({ symptomSelectElement, urlSearchParam, prrByVaccineTableElement, keyColumnName }) {
        const prrByVaccineTableView = new PrrByVaccineTableView(prrByVaccineTableElement, keyColumnName);
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
        return prrByVaccineTableView;
    }

    static #configureVaccine({ vaccineSelectElement, urlSearchParam, prrBySymptomTableElement }) {
        const prrBySymptomTableView = new PrrBySymptomTableView(prrBySymptomTableElement);
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
        return prrBySymptomTableView;
    }

    static #configurePDFButton({ pdf: { pdfButton, heading, valueName }, symptom, vaccine }) {
        pdfButton.addEventListener(
            'click',
            () => PdfCreator
                .createPdf({ symptom, vaccine, heading, valueName })
                .download(heading));
    }
}
