class SymptomHistogramByBatchcodeTableFactory:

    @staticmethod
    def createSymptomHistogramByBatchcodeTable(symptomByBatchcodeTable):
        return symptomByBatchcodeTable.groupby(['VAX_LOT1'])['SYMPTOM'].value_counts().to_frame('SYMPTOM_COUNT_BY_VAX_LOT')
