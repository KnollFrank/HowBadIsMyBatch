import pandas as pd
import numpy as np

class SymptomsByBatchcodesTableFactory:

    @staticmethod
    def createSymptomsByBatchcodesTable(VAERSVAX, VAERSSYMPTOMS):
        index_columns = ['VAX_LOT1', 'VAX_LOT2']
        return pd.merge(
            SymptomsByBatchcodesTableFactory._get_VAERSVAX_WITH_VAX_LOTS(VAERSVAX, index_columns),
            SymptomsByBatchcodesTableFactory._getSymptomsTable(VAERSSYMPTOMS),
            on = 'VAERS_ID').set_index(index_columns)[['SYMPTOMS']]
    
    @staticmethod
    def _get_VAERSVAX_WITH_VAX_LOTS(VAERSVAX, index_columns):
        return pd.concat(
            [VAERSVAX, SymptomsByBatchcodesTableFactory._getVaxLotsTable(VAERSVAX, index_columns)],
            axis='columns').reset_index().drop_duplicates(subset = ['VAERS_ID'] + index_columns)

    @staticmethod
    def _getVaxLotsTable(VAERSVAX, index_columns):
        VAX_LOT_LIST_Table = VAERSVAX.groupby("VAERS_ID").agg(VAX_LOT_LIST = pd.NamedAgg(column = 'VAX_LOT', aggfunc = list))
        return pd.DataFrame(
            [fill(VAX_LOTS, 2, str(np.nan)) for VAX_LOTS in VAX_LOT_LIST_Table['VAX_LOT_LIST'].tolist()],
            columns = index_columns,
            index = VAX_LOT_LIST_Table.index)

    @staticmethod
    def _getSymptomsTable(VAERSSYMPTOMS):
        return pd.concat(
            [
                VAERSSYMPTOMS['SYMPTOM1'],
                VAERSSYMPTOMS['SYMPTOM2'],
                VAERSSYMPTOMS['SYMPTOM3'],
                VAERSSYMPTOMS['SYMPTOM4'],
                VAERSSYMPTOMS['SYMPTOM5']
            ]).dropna().to_frame(name = "SYMPTOMS").reset_index()

def fill(lst, desiredLen, fillValue):
    return lst + [fillValue] * (max(desiredLen - len(lst), 0))