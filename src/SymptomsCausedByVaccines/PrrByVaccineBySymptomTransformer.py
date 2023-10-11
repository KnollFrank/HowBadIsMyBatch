class PrrByVaccineBySymptomTransformer:

    @staticmethod
    def removeNonZeroPrrs(prrByVaccineBySymptom):
        return prrByVaccineBySymptom.map(
            lambda prrByVaccine: {vaccine: prr for vaccine, prr in prrByVaccine.items() if prr != 0})
