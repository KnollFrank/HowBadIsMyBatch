class PrrByVaccineTableView {

    #prrByVaccineTable;
    #prrByVaccine;
    #symptom;

    constructor(prrByVaccineTableElement, downloadPrrByVaccineTableButton) {
        this.#prrByVaccineTable = new PrrByVaccineTable(prrByVaccineTableElement);
        this.#prrByVaccineTable.initialize();
        downloadPrrByVaccineTableButton.addEventListener(
            'click',
            () => this.#downloadPrrByVaccine())
    }

    displayPrrByVaccineTable4Symptom(symptom) {
        PrrByVaccineProvider
            .getPrrByVaccine(symptom)
            .then(prrByVaccine => {
                this.#prrByVaccine = prrByVaccine;
                this.#symptom = symptom;
                this.#prrByVaccineTable.display(prrByVaccine);
            });
    }

    #downloadPrrByVaccine() {
        UIUtils.downloadUrlAsFilename(
            window.URL.createObjectURL(
                new Blob(
                    [Utils.convertDict2CSV(this.#prrByVaccine)],
                    { type: 'text/csv' })),
            this.#symptom
        );
    }
}
