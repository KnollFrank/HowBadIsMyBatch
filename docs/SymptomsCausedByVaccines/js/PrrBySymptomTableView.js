class PrrBySymptomTableView {

    #delegate;

    constructor(prrBySymptomTableElement, downloadPrrBySymptomTableButton) {
        this.#delegate = new PrrByKeyTableView(
            new PrrBySymptomTable(prrBySymptomTableElement),
            downloadPrrBySymptomTableButton,
            'Vaccine',
            PrrByVaccineProvider.getPrrBySymptom);
    }

    displayPrrBySymptomTable4Vaccine(vaccine) {
        this.#delegate.displayPrrByKeyTable4Value(vaccine);
    }
}
