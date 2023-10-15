class PrrByVaccineTableView {

    #delegate;

    constructor(prrByVaccineTableElement, downloadPrrByVaccineTableButton) {
        this.#delegate = new PrrByKeyTableView(
            new PrrByVaccineTable(prrByVaccineTableElement),
            downloadPrrByVaccineTableButton,
            'Symptom',
            PrrByVaccineProvider.getPrrByVaccine);
    }

    displayPrrByVaccineTable4Symptom(symptom) {
        this.#delegate.displayPrrByKeyTable4Value(symptom);
    }
}
