import pandas as pd

class BatchCodeTableIntoHistogramDescriptionTableMerger:

    # FK-TODO: refactor
    @staticmethod
    def mergeBatchCodeTableIntoHistogramDescriptionTable(batchCodeTable, histogramDescriptionTable):
        def merge(src):
             dst = src['HISTOGRAM_DESCRIPTION']
             # dict_3 = {**dict_1, **dict_2}
             dst['Adverse Reaction Reports'] = src['Adverse Reaction Reports']
             dst['Deaths'] = src['Deaths']
             dst['Disabilities'] = src['Disabilities']
             dst['Life Threatening Illnesses'] = src['Life Threatening Illnesses']
             dst['Company'] = src['Company']
             dst['Severe reports'] = src['Severe reports']
             dst['Lethality'] = src['Lethality']
             return dst
        mergedTable = pd.merge(
             histogramDescriptionTable,
             batchCodeTable,
             how = 'left',
             left_index = True,
             right_index = True,
             validate = 'one_to_one')
        mergedTable = mergedTable[['HISTOGRAM_DESCRIPTION', 'Adverse Reaction Reports', 'Deaths', 'Disabilities', 'Life Threatening Illnesses', 'Company', 'Severe reports', 'Lethality']].apply(merge, axis='columns')
        mergedTable.name = 'HISTOGRAM_DESCRIPTION'
        mergedTable = mergedTable.to_frame()
        mergedTable['COUNTRY'] = histogramDescriptionTable['COUNTRY']
        return mergedTable
