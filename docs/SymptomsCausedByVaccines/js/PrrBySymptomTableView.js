class PrrBySymptomTableView {

    #delegate;

    constructor(prrBySymptomTableElement, downloadPrrBySymptomTableButton) {
        this.#delegate = new PrrByKeyTableView(
            this.#createPrrBySymptomTable(prrBySymptomTableElement),
            downloadPrrBySymptomTableButton,
            'Vaccine',
            PrrByVaccineProvider.getPrrBySymptom);
    }

    displayPrrBySymptomTable4Vaccine(vaccine) {
        this.#delegate.displayPrrByKeyTable4Value(vaccine);
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
