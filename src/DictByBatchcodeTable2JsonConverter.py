import json


class DictByBatchcodeTable2JsonConverter:

    @staticmethod
    def convertDictByBatchcodeTable2Json(jsonByBatchcodeTable, batchcode):
        # res = jsonByBatchcodeTable.apply(lambda str: json.loads(str['SYMPTOM_COUNT_BY_VAX_LOT']), axis= 'columns')
        return json.dumps(
            {
                "batchcode": batchcode,
                "histograms": [
                    {
                        "batchcodes": ["1808982", "EW0175"],
                        "histogram": {"Blood pressure orthostatic abnormal":5,"Chest discomfort":1}
                    },
                    {
                        "batchcodes": ["015M20A", "1808982"],
                        "histogram": {"Chest discomfort":2}
                    }
                ]
            })
