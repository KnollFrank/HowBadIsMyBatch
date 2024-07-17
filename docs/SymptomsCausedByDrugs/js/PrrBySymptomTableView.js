class PrrBySymptomTableView {

    #delegate;

    constructor(prrBySymptomTableElement) {
        this.#delegate = new PrrByKeyTableView(
            this.#createPrrBySymptomTable(prrBySymptomTableElement),
            PrrByVaccineProvider.getPrrBySymptom);
    }

    displayPrrBySymptomTable4Vaccine(id) {
        this.#delegate.displayPrrByKeyTable4Value(id);
    }

    getTable() {
        return this.#delegate.getTable();
    }

    #createPrrBySymptomTable(tableElement) {
        return new PrrByKeyTable({
            tableElement: tableElement,
            keyColumnName: 'Symptom',
            prrColumnName: 'Lower Confidence Limit of Proportional Reporting Ratio >= 2',
            shallMarkRowIfPrrTooHigh: false
        });
    }
}
