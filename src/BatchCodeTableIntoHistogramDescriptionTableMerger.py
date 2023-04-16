import pandas as pd
from Utils import get_dictWithKeys_dictWithoutKeys


class BatchCodeTableIntoHistogramDescriptionTableMerger:

    def __init__(self):
        self.HISTOGRAM_DESCRIPTION_columnName = 'HISTOGRAM_DESCRIPTION'

    def mergeBatchCodeTableIntoHistogramDescriptionTable(self, batchCodeTable, histogramDescriptionTable):
        mergedTable = self._combineTables(batchCodeTable, histogramDescriptionTable)
        mergedTable = self._merge_columns_into_HISTOGRAM_DESCRIPTION(mergedTable)
        mergedTable['COUNTRY'] = histogramDescriptionTable['COUNTRY']
        return mergedTable

    def _combineTables(self, batchCodeTable, histogramDescriptionTable):
        mergedTable = pd.merge(
            histogramDescriptionTable,
            batchCodeTable,
            how='left',
            left_index=True,
            right_index=True,
            validate='one_to_one')
        return mergedTable[
            [
                self.HISTOGRAM_DESCRIPTION_columnName,
                'Adverse Reaction Reports',
                'Deaths',
                'Disabilities',
                'Life Threatening Illnesses',
                'Company',
                'Severe reports',
                'Lethality'
            ]]

    def _merge_columns_into_HISTOGRAM_DESCRIPTION(self, table):
        table = table.apply(
            self.__merge_columns_into_HISTOGRAM_DESCRIPTION,
            axis='columns')
        table.name = self.HISTOGRAM_DESCRIPTION_columnName
        return table.to_frame()

    def __merge_columns_into_HISTOGRAM_DESCRIPTION(self, src):
        dict_with_HISTOGRAM_DESCRIPTION, dict_without_HISTOGRAM_DESCRIPTION = get_dictWithKeys_dictWithoutKeys(
            src.to_dict(),
            {self.HISTOGRAM_DESCRIPTION_columnName})
        HISTOGRAM_DESCRIPTION = dict_with_HISTOGRAM_DESCRIPTION[self.HISTOGRAM_DESCRIPTION_columnName]
        return {**HISTOGRAM_DESCRIPTION, **dict_without_HISTOGRAM_DESCRIPTION}
