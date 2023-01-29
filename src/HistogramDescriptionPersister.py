from TableByBatchcodeFilter import TableByBatchcodeFilter
from DictByBatchcodeTable2DictConverter import DictByBatchcodeTable2DictConverter
from IOUtils import IOUtils


class HistogramDescriptionPersister:

    def __init__(self, directory):
        self.directory = directory

    def saveHistogramDescriptionsForBatchcodes(self, batchcodes, dictByBatchcodeTable, progress):
        for count, batchcode in enumerate(batchcodes, start = 1):
            histogramDescription = self._getHistogramDescriptionForBatchcode(batchcode, dictByBatchcodeTable)
            # FK-TODO: nicht direkt {batchcode}.json speichern, denn im Dateinamen könnte sich dann ein '/' befinden, was ein nicht gewünschtes Unterverzeichnis erzeugt. Deshalb in der Batchcode-Tabelle eine unsichtbare Spalte einfügen, in welcher für den jeweiligen batchcode der bereinigte und eindeutige Dateiname steht (z.B. einfach durchnummeriert: 0.json, 1.json, ...).
            IOUtils.saveDictAsJson(histogramDescription, f'{self.directory}/{batchcode}.json')
            progress(count, len(batchcodes), batchcode)

    def _getHistogramDescriptionForBatchcode(self, batchcode, dictByBatchcodeTable):
        dictByBatchcodeTableForBatchcode = TableByBatchcodeFilter.filterTableByBatchcode(batchcode, dictByBatchcodeTable)
        histogramDescription = DictByBatchcodeTable2DictConverter.convertDictByBatchcodeTable2Dict(dictByBatchcodeTableForBatchcode, batchcode)
        return histogramDescription
