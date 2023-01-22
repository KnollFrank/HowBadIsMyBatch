import pandas as pd
import numpy as np

class SymptomsByBatchcodesTableFactory:

    @staticmethod
    def createSymptomsByBatchcodesTable(VAERSVAX, VAERSSYMPTOMS):
        index_columns = SymptomsByBatchcodesTableFactory._getIndexColumns(VAERSVAX)
        symptomsColumn = 'SYMPTOMS'
        return pd.merge(
            SymptomsByBatchcodesTableFactory._get_VAERSVAX_WITH_VAX_LOTS(VAERSVAX, index_columns),
            SymptomsByBatchcodesTableFactory._getSymptomsTable(VAERSSYMPTOMS, symptomsColumn),
            on = 'VAERS_ID').set_index(index_columns)[[symptomsColumn]]
    
    @staticmethod
    def _getIndexColumns(VAERSVAX):
        return [f"VAX_LOT{num}" for num in range(1, SymptomsByBatchcodesTableFactory._getMaxNumShots(VAERSVAX) + 1)]

    @staticmethod
    def _getMaxNumShots(VAERSVAX):
        return VAERSVAX.index.value_counts().iloc[0]

    @staticmethod
    def _get_VAERSVAX_WITH_VAX_LOTS(VAERSVAX, index_columns):
        return pd.concat(
            [VAERSVAX, SymptomsByBatchcodesTableFactory._getVaxLotsTable(VAERSVAX, index_columns)],
            axis='columns').reset_index().drop_duplicates(subset = ['VAERS_ID'] + index_columns)

    @staticmethod
    def _getVaxLotsTable(VAERSVAX, index_columns):       
        VAX_LOT_LIST_Table = VAERSVAX.groupby("VAERS_ID").agg(
            VAX_LOT_LIST = pd.NamedAgg(
                column = 'VAX_LOT',
                aggfunc = lambda VAX_LOT_series: list(VAX_LOT_series.sort_values())))
        return pd.DataFrame(
            fillLsts(
                lsts = VAX_LOT_LIST_Table['VAX_LOT_LIST'].tolist(),
                desiredLen = len(index_columns),
                fillValue = str(np.nan)),
            columns = index_columns,
            index = VAX_LOT_LIST_Table.index)

    @staticmethod
    def _getSymptomsTable(VAERSSYMPTOMS, symptomsColumn):
        return pd.concat(
            [
                VAERSSYMPTOMS['SYMPTOM1'],
                VAERSSYMPTOMS['SYMPTOM2'],
                VAERSSYMPTOMS['SYMPTOM3'],
                VAERSSYMPTOMS['SYMPTOM4'],
                VAERSSYMPTOMS['SYMPTOM5']
            ]).dropna().to_frame(name = symptomsColumn).reset_index()

def fillLsts(lsts, desiredLen, fillValue):
    return [fillLst(lst, desiredLen, fillValue) for lst in lsts]

def fillLst(lst, desiredLen, fillValue):
    return lst + [fillValue] * (max(desiredLen - len(lst), 0))