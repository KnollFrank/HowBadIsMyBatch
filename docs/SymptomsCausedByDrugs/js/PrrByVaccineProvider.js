class PrrByVaccineProvider {

    static getPrrByVaccine(symptom) {
        return fetch(`./data/ProportionalReportingRatios/symptoms/${symptom}`).then(response => response.json());
    }

    static getPrrBySymptom(vaccine) {
        return fetch(`./data/ProportionalReportingRatios/vaccines/${vaccine}`).then(response => response.json());
    }
}