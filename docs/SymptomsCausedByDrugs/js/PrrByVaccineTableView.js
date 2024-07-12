class PrrByVaccineTableView {

    #delegate;

    constructor(prrByVaccineTableElement, downloadPrrByVaccineTableButton) {
        this.#delegate = new PrrByKeyTableView(
            this.#createPrrByVaccineTable(prrByVaccineTableElement),
            downloadPrrByVaccineTableButton,
            'Symptom',
            PrrByVaccineProvider.getPrrByVaccine);
    }

    displayPrrByVaccineTable4Symptom(id, text) {
        this.#delegate.displayPrrByKeyTable4Value(id, text);
    }

    #createPrrByVaccineTable(tableElement) {
        return new PrrByKeyTable({
            tableElement: tableElement,
            keyColumnName: 'Drug',
            prrColumnName: 'Lower Confidence Limit of Proportional Reporting Ratio',
            shallMarkRowIfPrrTooHigh: true
        });
    }
}
