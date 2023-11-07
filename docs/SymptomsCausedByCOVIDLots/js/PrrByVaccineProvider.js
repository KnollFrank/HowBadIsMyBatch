class PrrByVaccineProvider {

    static getPrrByVaccine(symptom) {
        return fetch(`../data/SymptomsCausedByCOVIDLots/ProportionalReportingRatios/symptoms/${symptom}.json`).then(response => response.json());
    }

    static getPrrBySymptom(vaccine) {
        return fetch(`../data/SymptomsCausedByCOVIDLots/ProportionalReportingRatios/vaccines/${vaccine}.json`).then(response => response.json());
    }
}