class PrrByVaccineTableView {

    #delegate;

    // FK-TODO: remove downloadPrrByVaccineTableButton
    constructor(prrByVaccineTableElement, downloadPrrByVaccineTableButton, keyColumnName) {
        this.#delegate = new PrrByKeyTableView(
            this.#createPrrByVaccineTable(prrByVaccineTableElement, keyColumnName),
            PrrByVaccineProvider.getPrrByVaccine);
    }

    displayPrrByVaccineTable4Symptom(id, text) {
        this.#delegate.displayPrrByKeyTable4Value(id, text);
    }

    getTable() {
        return this.#delegate.getTable();
    }

    #createPrrByVaccineTable(tableElement, keyColumnName) {
        return new PrrByKeyTable({
            tableElement: tableElement,
            keyColumnName: keyColumnName,
            prrColumnName: 'Lower Confidence Limit of Proportional Reporting Ratio',
            shallMarkRowIfPrrTooHigh: true
        });
    }
}
