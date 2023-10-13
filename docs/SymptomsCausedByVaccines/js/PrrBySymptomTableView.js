class PrrBySymptomTableView {

    #prrBySymptomTable;

    constructor(prrBySymptomTableElement) {
        this.#prrBySymptomTable = new PrrBySymptomTable(prrBySymptomTableElement);
        this.#prrBySymptomTable.initialize();
    }

    displayPrrBySymptomTable4Vaccine(vaccine) {
        PrrByVaccineProvider
            .getPrrBySymptom(vaccine)
            .then(prrBySymptom => this.#prrBySymptomTable.display(prrBySymptom));
    }
}
