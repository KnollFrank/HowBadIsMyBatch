class PrrBySymptomTableView {

    #delegate;

    constructor(prrBySymptomTableElement, downloadPrrBySymptomTableButton) {
        this.#delegate = new PrrByKeyTableView(
            this.#createPrrBySymptomTable(prrBySymptomTableElement),
            downloadPrrBySymptomTableButton,
            'Drug',
            PrrByVaccineProvider.getPrrBySymptom);
    }

    displayPrrBySymptomTable4Vaccine(id, text) {
        this.#delegate.displayPrrByKeyTable4Value(id, text);
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
