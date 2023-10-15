class PrrByVaccineTable {

    #delegate;

    constructor(tableElement) {
        this.#delegate = new PrrByKeyTable({
            tableElement: tableElement,
            keyColumnName: 'Vaccine',
            prrColumnName: 'Proportional Reporting Ratio',
            shallMarkRowIfPrrTooHigh: true
        });
    }

    initialize() {
        this.#delegate.initialize();
    }

    display(prrByVaccine) {
        this.#delegate.display(prrByVaccine);
    }

    getDisplayedTableAsCsv(heading) {
        return this.#delegate.getDisplayedTableAsCsv(heading);
    }
}
