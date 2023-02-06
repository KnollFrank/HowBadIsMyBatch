import pandas as pd
import numpy as np
from Utils import fillLsts

class SymptomByBatchcodeTableFactory:

    @staticmethod
    def createSymptomByBatchcodeTable(VAERSVAX, VAERSSYMPTOMS):
        index_columns = SymptomByBatchcodeTableFactory._getIndexColumns(VAERSVAX)
        symptomColumn = 'SYMPTOM'
        return (pd
                    .merge(
                        SymptomByBatchcodeTableFactory._get_VAERSVAX_WITH_VAX_LOTS(VAERSVAX, index_columns),
                        SymptomByBatchcodeTableFactory._getSymptomsTable(VAERSSYMPTOMS, symptomColumn),
                        on = 'VAERS_ID')
                    .set_index(index_columns)
                    [[symptomColumn]])
    
    @staticmethod
    def _getIndexColumns(VAERSVAX):
        return [f"VAX_LOT{num}" for num in range(1, SymptomByBatchcodeTableFactory._getMaxNumShots(VAERSVAX) + 1)]

    @staticmethod
    def _getMaxNumShots(VAERSVAX):
        return VAERSVAX.index.value_counts().iloc[0]

    @staticmethod
    def _get_VAERSVAX_WITH_VAX_LOTS(VAERSVAX, index_columns):
        return (pd
                    .concat(
                        [VAERSVAX, SymptomByBatchcodeTableFactory._getVaxLotsTable(VAERSVAX, index_columns)],
                        axis = 'columns')
                    .reset_index()
                    .drop_duplicates(subset = ['VAERS_ID'] + index_columns))

    @staticmethod
    def _getVaxLotsTable(VAERSVAX, index_columns):
        VAX_LOT_LIST_Table = SymptomByBatchcodeTableFactory._getVAX_LOT_LIST_Table(VAERSVAX)
        return SymptomByBatchcodeTableFactory._fillLstsInDataframe(VAX_LOT_LIST_Table, index_columns)

    @staticmethod
    def _getVAX_LOT_LIST_Table(VAERSVAX):
        # slow: aggfunc = lambda VAX_LOT_series: list(VAX_LOT_series.sort_values())))
        # fast:
        VAX_LOT_LIST_Table = VAERSVAX.groupby("VAERS_ID").agg(
            VAX_LOT_LIST = pd.NamedAgg(
                column = 'VAX_LOT',
                aggfunc = list))
        VAX_LOT_LIST_Table['VAX_LOT_LIST'] = VAX_LOT_LIST_Table['VAX_LOT_LIST'].apply(sorted)
        return VAX_LOT_LIST_Table

    @staticmethod
    def _fillLstsInDataframe(VAX_LOT_LIST_Table, index_columns):
        return pd.DataFrame(
            fillLsts(
                lsts = VAX_LOT_LIST_Table['VAX_LOT_LIST'].tolist(),
                desiredLen = len(index_columns),
                fillValue = str(np.nan)),
            columns = index_columns,
            index = VAX_LOT_LIST_Table.index)


    @staticmethod
    def _getSymptomsTable(VAERSSYMPTOMS, symptomColumn):
        return (pd
                    .concat(
                        [
                            VAERSSYMPTOMS['SYMPTOM1'],
                            VAERSSYMPTOMS['SYMPTOM2'],
                            VAERSSYMPTOMS['SYMPTOM3'],
                            VAERSSYMPTOMS['SYMPTOM4'],
                            VAERSSYMPTOMS['SYMPTOM5']
                        ])
                    .dropna()
                    .to_frame(name = symptomColumn)
                    .reset_index())
