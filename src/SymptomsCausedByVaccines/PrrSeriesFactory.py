class PrrSeriesFactory:

    @staticmethod
    def getPrrByVaccineBySymptom(prrByVaccineAndSymptom):
        return prrByVaccineAndSymptom.apply(lambda prrByVaccine: prrByVaccine.to_dict())

    @staticmethod
    def getPrrBySymptomByVaccine(prrByVaccineAndSymptom):
        return prrByVaccineAndSymptom.apply(
            lambda prrBySymptom: prrBySymptom.to_dict(),
            axis = 'columns')
