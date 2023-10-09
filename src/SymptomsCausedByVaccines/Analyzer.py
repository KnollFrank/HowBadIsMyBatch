import pandas as pd

class Analyzer:

    def __init__(self, symptomByVaccine: pd.DataFrame):
        self.symptomByVaccine = symptomByVaccine

    def getSymptomsForVaccine(self, vaxType):
        return self.symptomByVaccine.loc[vaxType]
