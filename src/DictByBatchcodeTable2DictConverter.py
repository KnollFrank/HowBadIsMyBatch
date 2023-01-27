import json


class DictByBatchcodeTable2DictConverter:

    @staticmethod
    def convertDictByBatchcodeTable2Dict(dictByBatchcodeTable, batchcode):
        return {
                "batchcode": batchcode,
                "histograms": DictByBatchcodeTable2DictConverter._getHistograms(dictByBatchcodeTable)
            }

    @staticmethod
    def _getHistograms(dictByBatchcodeTable):
        return (
            dictByBatchcodeTable
                .apply(
                    lambda row: {
                        "batchcodes": DictByBatchcodeTable2DictConverter._getNaNBatchcodes(row.name),
                        "histogram": row['SYMPTOM_COUNT_BY_VAX_LOT']
                    },
                    axis = 'columns')
                .to_list()
        )
    
    @staticmethod
    def _getNaNBatchcodes(batchcodes):
        # FK-TODO: handle 'nan' everywhere correctly
        return [batchcode for batchcode in batchcodes if batchcode != 'nan']
