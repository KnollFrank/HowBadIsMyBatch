class PrrByVaccineProvider {

    static getPrrByVaccine(symptom) {
        return fetch(`../data/ProportionalReportingRatios/symptoms/${symptom}.json`).then(response => response.json());
    }
}