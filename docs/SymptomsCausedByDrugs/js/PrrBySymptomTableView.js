class PrrBySymptomTableView {

    #delegate;

    // FK-TODO: remove downloadPrrBySymptomTableButton, valueName
    constructor(prrBySymptomTableElement, downloadPrrBySymptomTableButton, valueName) {
        this.#delegate = new PrrByKeyTableView(
            this.#createPrrBySymptomTable(prrBySymptomTableElement),
            PrrByVaccineProvider.getPrrBySymptom);
    }

    displayPrrBySymptomTable4Vaccine(id, text) {
        this.#delegate.displayPrrByKeyTable4Value(id, text);
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
