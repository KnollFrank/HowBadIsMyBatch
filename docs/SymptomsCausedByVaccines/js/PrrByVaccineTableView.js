class PrrByVaccineTableView {

    #prrByVaccineTable;
    #downloadPrrByVaccineTableButton;
    #prrByVaccine;
    #symptom;

    constructor(prrByVaccineTableElement, downloadPrrByVaccineTableButton) {
        this.#prrByVaccineTable = new PrrByVaccineTable(prrByVaccineTableElement);
        this.#prrByVaccineTable.initialize();
        this.#initializeButton(downloadPrrByVaccineTableButton);
    }

    displayPrrByVaccineTable4Symptom(symptom) {
        UIUtils.disableButton(this.#downloadPrrByVaccineTableButton);
        PrrByVaccineProvider
            .getPrrByVaccine(symptom)
            .then(prrByVaccine => {
                this.#prrByVaccine = prrByVaccine;
                this.#symptom = symptom;
                this.#prrByVaccineTable.display(prrByVaccine);
                UIUtils.enableButton(this.#downloadPrrByVaccineTableButton);
            });
    }

    #initializeButton(downloadPrrByVaccineTableButton) {
        this.#downloadPrrByVaccineTableButton = downloadPrrByVaccineTableButton;
        UIUtils.disableButton(downloadPrrByVaccineTableButton);
        downloadPrrByVaccineTableButton.addEventListener(
            'click',
            () => this.#downloadPrrByVaccine())
    }

    #downloadPrrByVaccine() {
        UIUtils.downloadUrlAsFilename(
            window.URL.createObjectURL(
                new Blob(
                    [
                        PrrByKey2CsvConverter.convertPrrByKey2Csv(
                            {
                                prrByKey: this.#prrByVaccine,
                                keyColumn: 'Vaccine',
                                prrColumn: 'Proportional Reporting Ratio'
                            })
                    ],
                    { type: 'text/csv' })),
            this.#symptom
        );
    }
}
