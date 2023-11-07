class PrrByVaccineTableView {

    #delegate;

    constructor(prrByVaccineTableElement, downloadPrrByVaccineTableButton) {
        this.#delegate = new PrrByKeyTableView(
            this.#createPrrByVaccineTable(prrByVaccineTableElement),
            downloadPrrByVaccineTableButton,
            'Symptom',
            PrrByVaccineProvider.getPrrByVaccine);
    }

    displayPrrByVaccineTable4Symptom(symptom) {
        this.#delegate.displayPrrByKeyTable4Value(symptom);
    }

    #createPrrByVaccineTable(tableElement) {
        return new PrrByKeyTable({
            tableElement: tableElement,
            keyColumnName: 'Batch',
            prrColumnName: 'Proportional Reporting Ratio',
            shallMarkRowIfPrrTooHigh: true
        });
    }
}
