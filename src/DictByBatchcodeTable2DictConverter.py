class DictByBatchcodeTable2DictConverter:

    @staticmethod
    def convertDictByBatchcodeTable2Dict(dictByBatchcodeTable, batchcode):
        return {
                "batchcode": batchcode,
                "histograms": DictByBatchcodeTable2DictConverter._getHistograms(dictByBatchcodeTable)
            }
    
    @staticmethod
    def _getHistograms(dictByBatchcodeTable):
        dictByBatchcodeTable = dictByBatchcodeTable.rename(columns = { "SYMPTOM_COUNT_BY_VAX_LOT": "histogram" })
        DictByBatchcodeTable2DictConverter._addBatchcodesColumn(dictByBatchcodeTable)
        return dictByBatchcodeTable.to_dict('records')
    
    @staticmethod
    def _addBatchcodesColumn(dictByBatchcodeTable):
        batchcodeColumns = dictByBatchcodeTable.index.names
        dictByBatchcodeTable['batchcodes'] = dictByBatchcodeTable.reset_index()[batchcodeColumns].values.tolist()
        dictByBatchcodeTable['batchcodes'] = dictByBatchcodeTable['batchcodes'].map(DictByBatchcodeTable2DictConverter._getNaNBatchcodes)

    @staticmethod
    def _getNaNBatchcodes(batchcodes):
        # FK-TODO: handle 'nan' everywhere correctly
        return [batchcode for batchcode in batchcodes if batchcode != 'nan']
