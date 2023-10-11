class PrrByVaccineBySymptomFactory:

    @staticmethod
    def getPrrByVaccineBySymptom(prrByVaccineAndSymptom):
        return prrByVaccineAndSymptom.apply(lambda prrByVaccine: prrByVaccine.to_dict())
