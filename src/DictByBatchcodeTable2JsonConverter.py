import json


class DictByBatchcodeTable2JsonConverter:

    @staticmethod
    def convertDictByBatchcodeTable2Json(dictByBatchcodeTable, batchcode):
        return json.dumps(
            {
                "batchcode": batchcode,
                "histograms": DictByBatchcodeTable2JsonConverter._getHistograms(dictByBatchcodeTable)
            })

    @staticmethod
    def _getHistograms(dictByBatchcodeTable):
        return (
            dictByBatchcodeTable
                .apply(
                    lambda row: {
                        "batchcodes": list(row.name),
                        "histogram": row['SYMPTOM_COUNT_BY_VAX_LOT']
                    },
                    axis = 'columns')
                .to_list()
        )
