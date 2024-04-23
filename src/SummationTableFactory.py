import pandas as pd

class SummationTableFactory:

    @staticmethod
    def createSummationTable(dataFrame):
        summationTable = dataFrame.agg(
            **{
                'Deaths':                     pd.NamedAgg(column = 'DIED',     aggfunc = 'sum'),
                'Adverse Reaction Reports':   pd.NamedAgg(column = 'DIED',     aggfunc = 'size'),
                'Life Threatening Illnesses': pd.NamedAgg(column = 'L_THREAT', aggfunc = 'sum'),
                'Hospitalizations':           pd.NamedAgg(column = 'HOSPITAL', aggfunc = 'sum'),
                'Disabilities':               pd.NamedAgg(column = 'DISABLE',  aggfunc = 'sum'),
                'Severities':                 pd.NamedAgg(column = 'SEVERE',   aggfunc = 'sum')
            })
        summationTable['Severe reports'] = summationTable['Severities'] / summationTable['Adverse Reaction Reports'] * 100
        summationTable['Lethality'] = summationTable['Deaths'] / summationTable['Adverse Reaction Reports'] * 100
        return summationTable[
            [
                'Adverse Reaction Reports',
                'Deaths',
                'Disabilities',
                'Life Threatening Illnesses',
                'Hospitalizations',
                'Severe reports',
                'Lethality'
            ]]
