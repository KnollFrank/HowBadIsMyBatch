class PrrBySymptomTableView {

    #prrBySymptomTable;
    #downloadPrrBySymptomTableButton;
    #prrBySymptom;
    #vaccine;

    constructor(prrBySymptomTableElement, downloadPrrBySymptomTableButton) {
        this.#prrBySymptomTable = new PrrBySymptomTable(prrBySymptomTableElement);
        this.#prrBySymptomTable.initialize();
        this.#initializeButton(downloadPrrBySymptomTableButton);
    }

    displayPrrBySymptomTable4Vaccine(vaccine) {
        UIUtils.disableButton(this.#downloadPrrBySymptomTableButton);
        PrrByVaccineProvider
            .getPrrBySymptom(vaccine)
            .then(prrBySymptom => {
                this.#prrBySymptom = prrBySymptom;
                this.#vaccine = vaccine;
                this.#prrBySymptomTable.display(prrBySymptom);
                UIUtils.enableButton(this.#downloadPrrBySymptomTableButton);
            });
    }

    #initializeButton(downloadPrrBySymptomTableButton) {
        this.#downloadPrrBySymptomTableButton = downloadPrrBySymptomTableButton;
        UIUtils.disableButton(downloadPrrBySymptomTableButton);
        downloadPrrBySymptomTableButton.addEventListener(
            'click',
            () => this.#downloadPrrBySymptom())
    }

    #downloadPrrBySymptom() {
        UIUtils.downloadUrlAsFilename(
            window.URL.createObjectURL(
                new Blob(
                    [
                        PrrByKey2CsvConverter.convertPrrByKey2Csv(
                            {
                                heading: '# Vaccine: ' + this.#vaccine,
                                columns: {
                                    keyColumn: 'Symptom',
                                    prrColumn: 'Proportional Reporting Ratio > 1'
                                },
                                prrByKey: this.#prrBySymptom
                            })
                    ],
                    { type: 'text/csv' })),
            this.#vaccine
        );
    }
}
