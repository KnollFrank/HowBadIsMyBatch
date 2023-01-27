from TableByBatchcodeFilter import TableByBatchcodeFilter
from DictByBatchcodeTable2DictConverter import DictByBatchcodeTable2DictConverter
from IOUtils import IOUtils


class HistogramDescriptionPersister:

    def __init__(self, directory):
        self.directory = directory

    def saveHistogramDescriptionsForBatchcodes(self, batchcodes, dictByBatchcodeTable):
        for batchcode in batchcodes:
            histogramDescription = self._getHistogramDescriptionForBatchcode(batchcode, dictByBatchcodeTable)
            print('saving', batchcode)
            IOUtils.saveDictAsJson(
                histogramDescription,
                f'{self.directory}/{batchcode}.json')

    def _getHistogramDescriptionForBatchcode(self, batchcode, dictByBatchcodeTable):
        dictByBatchcodeTableForBatchcode = TableByBatchcodeFilter.filterTableByBatchcode(batchcode, dictByBatchcodeTable)
        histogramDescription = DictByBatchcodeTable2DictConverter.convertDictByBatchcodeTable2Dict(dictByBatchcodeTableForBatchcode, batchcode)
        return histogramDescription
