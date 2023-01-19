import pandas as pd


class SymptomsByBatchcodesTableFactory:

    @staticmethod
    def createSymptomsByBatchcodesTable(VAERSVAX, VAERSSYMPTOMS):
        return pd.merge(
            SymptomsByBatchcodesTableFactory._get_VAERSVAX_WITH_VAX_LOTS(VAERSVAX),
            SymptomsByBatchcodesTableFactory._getSymptomsTable(VAERSSYMPTOMS),
            on = 'VAERS_ID').set_index(['VAX_LOT1', 'VAX_LOT2'])[['SYMPTOMS']]
    
    @staticmethod
    def _get_VAERSVAX_WITH_VAX_LOTS(VAERSVAX):
        return pd.concat(
            [VAERSVAX, SymptomsByBatchcodesTableFactory._getVaxLotsTable(VAERSVAX)],
            axis=1).drop_duplicates(subset=['VAX_LOT1', 'VAX_LOT2']).reset_index()

    @staticmethod
    def _getVaxLotsTable(VAERSVAX):
        VAX_LOT_LIST_Table = VAERSVAX.groupby("VAERS_ID").agg(VAX_LOT_LIST = pd.NamedAgg(column = 'VAX_LOT', aggfunc = list))
        return pd.DataFrame(
            VAX_LOT_LIST_Table['VAX_LOT_LIST'].tolist(),
            columns = ['VAX_LOT1', 'VAX_LOT2'],
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
            ]).dropna().drop_duplicates().to_frame(name = "SYMPTOMS").reset_index()
