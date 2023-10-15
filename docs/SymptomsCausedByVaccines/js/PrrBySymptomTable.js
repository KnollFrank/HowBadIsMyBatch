class PrrBySymptomTable {

    #delegate;

    constructor(tableElement) {
        this.#delegate = new PrrByKeyTable({
            tableElement: tableElement,
            keyColumnName: 'Symptom',
            prrColumnName: 'Proportional Reporting Ratio > 1',
            shallMarkRowIfPrrTooHigh: false
        });
    }

    initialize() {
        this.#delegate.initialize();
    }

    display(prrBySymptom) {
        this.#delegate.display(prrBySymptom);
    }

    getDisplayedTableAsCsv(heading) {
        return this.#delegate.getDisplayedTableAsCsv(heading);
    }
}
