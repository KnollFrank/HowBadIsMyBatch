import pandas as pd

class HistogramDescriptionTableFactory:

    @staticmethod
    def createHistogramDescriptionTable(dictByBatchcodeTable):
        histogramDescriptionTable = (
            dictByBatchcodeTable
                .groupby('VAX_LOT_EXPLODED')
                .agg(HistogramDescriptionTableFactory._getHistograms)
                .drop('nan'))
        histogramDescriptionTable = histogramDescriptionTable.rename(columns = { "SYMPTOM_COUNT_BY_VAX_LOT": "HISTOGRAM_DESCRIPTION" })
        histogramDescriptionTable.index.rename('VAX_LOT', inplace = True)
        return histogramDescriptionTable
    
    @staticmethod
    def _getHistograms(dictByBatchcodeTable):
        dictByBatchcodeTable = dictByBatchcodeTable.to_frame()
        dictByBatchcodeTable = dictByBatchcodeTable.rename(columns = { "SYMPTOM_COUNT_BY_VAX_LOT": "histogram" })
        HistogramDescriptionTableFactory._addBatchcodesColumn(dictByBatchcodeTable)
        histograms = dictByBatchcodeTable.to_dict('records')
        return {
                "batchcode": dictByBatchcodeTable.index.get_level_values('VAX_LOT_EXPLODED')[0],
                "histograms": histograms
            }
    
    @staticmethod
    def _addBatchcodesColumn(dictByBatchcodeTable):
        batchcodeColumns = dictByBatchcodeTable.index.names.difference(['VAX_LOT_EXPLODED'])
        dictByBatchcodeTable['batchcodes'] = dictByBatchcodeTable.reset_index()[batchcodeColumns].values.tolist()
        dictByBatchcodeTable['batchcodes'] = dictByBatchcodeTable['batchcodes'].map(HistogramDescriptionTableFactory._getNaNBatchcodes)

    @staticmethod
    def _getNaNBatchcodes(batchcodes):
        # FK-TODO: handle 'nan' everywhere correctly
        return [batchcode for batchcode in batchcodes if batchcode != 'nan']
