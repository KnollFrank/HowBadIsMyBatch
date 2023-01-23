class SymptomHistogramByBatchcodeTableFactory:

    @staticmethod
    def createSymptomHistogramByBatchcodeTable(symptomByBatchcodeTable):
        return (symptomByBatchcodeTable
            .groupby(symptomByBatchcodeTable.index.names)
            ['SYMPTOM'].value_counts()
            .to_frame('SYMPTOM_COUNT_BY_VAX_LOT'))
