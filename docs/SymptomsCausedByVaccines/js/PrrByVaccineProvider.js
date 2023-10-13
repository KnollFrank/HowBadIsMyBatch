class PrrByVaccineProvider {

    static getPrrByVaccine(symptom) {
        return fetch(`../data/ProportionalReportingRatios/symptoms/${symptom}.json`).then(response => response.json());
    }

    static getPrrBySymptom(vaccine) {
        return fetch(`../data/ProportionalReportingRatios/vaccines/${vaccine}.json`).then(response => response.json());
    }
}