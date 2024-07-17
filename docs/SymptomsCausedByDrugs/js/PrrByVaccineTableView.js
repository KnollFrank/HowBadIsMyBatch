class PrrByVaccineTableView {

    #delegate;

    constructor(prrByVaccineTableElement, keyColumnName) {
        this.#delegate = new PrrByKeyTableView(
            this.#createPrrByVaccineTable(prrByVaccineTableElement, keyColumnName),
            PrrByVaccineProvider.getPrrByVaccine);
    }

    displayPrrByVaccineTable4Symptom(id) {
        this.#delegate.displayPrrByKeyTable4Value(id);
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
