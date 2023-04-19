import warnings

class HistogramDescriptionTableSelector:

    @staticmethod
    def selectHistogramsWithShortestBatchcodeCombinations(histogramDescriptionTable):
        histogramDescriptionTable['HISTOGRAM_DESCRIPTION'] = histogramDescriptionTable['HISTOGRAM_DESCRIPTION'].map(HistogramDescriptionTableSelector._selectHistogramWithShortestBatchcodeCombination)
        return histogramDescriptionTable
    
    @staticmethod
    def _selectHistogramWithShortestBatchcodeCombination(histoDescr):
        return {
            "batchcode": histoDescr["batchcode"],
            "histogram": HistogramDescriptionTableSelector._getHistogramWithShortestBatchcodeCombination(histoDescr)
            }
    
    @staticmethod
    def _getHistogramWithShortestBatchcodeCombination(histoDescr):
        histogramsSortedByShortestBatchcodeCombination = sorted(
            histoDescr["histograms"],
            key = lambda histogram: len(histogram["batchcodes"]))
        histogramWithShortestBatchcodeCombination = histogramsSortedByShortestBatchcodeCombination[0]
        if len(histogramWithShortestBatchcodeCombination["batchcodes"]) != 1:
            warnings.warn(f"batchcode {histoDescr['batchcode']} has non unique batchcode combination {histogramWithShortestBatchcodeCombination['batchcodes']} for it's histogram")
        return histogramWithShortestBatchcodeCombination["histogram"]
