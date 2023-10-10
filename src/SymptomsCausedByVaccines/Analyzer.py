import pandas as pd

class Analyzer:

    def __init__(self, symptomByVaccine: pd.DataFrame):
        self.symptomByVaccine = symptomByVaccine

    def getSymptomsForVaccine(self, vaxType):
        return self.symptomByVaccine.loc[vaxType]

    def getVaccinesForSymptom(self, symptom):
        return self.symptomByVaccine[symptom]

    def getVaccines(self):
        return list(self.symptomByVaccine.index)

    def getSymptoms(self):
        return list(self.symptomByVaccine.columns)
