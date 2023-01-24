class HistogramTable2JsonTableConverter:

    @staticmethod
    def convertHistogramTable2JsonTable(symptomHistogramByBatchcodeTable):
        vax_lot_columns = symptomHistogramByBatchcodeTable.index.names.difference(['SYMPTOM'])
        return (
            symptomHistogramByBatchcodeTable
                    .groupby(vax_lot_columns)
                    .agg(lambda histogram_with_vax_lots: HistogramTable2JsonTableConverter._histogram_to_json(histogram_with_vax_lots, vax_lot_columns))
        )

    @staticmethod
    def _histogram_to_json(histogram_with_vax_lots, vax_lot_columns):
        histogram = histogram_with_vax_lots.reset_index(level = vax_lot_columns, drop=True)
        return histogram.to_json()
