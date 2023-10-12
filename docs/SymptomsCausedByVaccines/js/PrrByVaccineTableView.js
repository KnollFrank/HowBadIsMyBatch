class PrrByVaccineTableView {

    #prrByVaccineTable;

    constructor(prrByVaccineTableElement) {
        this.#prrByVaccineTable = new PrrByVaccineTable(prrByVaccineTableElement);
        this.#prrByVaccineTable.initialize();
    }

    displayPrrByVaccineTable4Symptom(symptom) {
        PrrByVaccineProvider
            .getPrrByVaccine(symptom)
            .then(prrByVaccine => this.#prrByVaccineTable.display(prrByVaccine));
    }
}
