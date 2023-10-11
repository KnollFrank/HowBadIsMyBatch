import pandas as pd


class PrrByVaccineTableFactory:

    @staticmethod
    def getPrrByVaccineTable(prrByVaccineAndSymptom):
        return pd.DataFrame(
            columns = ['11-beta-hydroxylase deficiency'],
            data = [  [prrByVaccineAndSymptom['11-beta-hydroxylase deficiency'].to_dict()]],
            index = pd.Index(['PrrByVaccine']))
