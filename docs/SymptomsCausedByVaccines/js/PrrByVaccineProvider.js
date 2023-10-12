class PrrByVaccineProvider {

    static getPrrByVaccine(symptom) {
        return fetch(`../data/ProportionalReportingRatios/${symptom}.json`).then(response => response.json());
    }
}