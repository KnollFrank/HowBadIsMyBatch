from HistogramFactory import createHistograms
from HistogramPersister import saveHistograms
from MultiIndexExploder import MultiIndexExploder
from HistogramDescriptionTableFactory import HistogramDescriptionTableFactory
from HistogramDescriptionTableSelector import HistogramDescriptionTableSelector
from BatchCodeTableIntoHistogramDescriptionTableMerger import BatchCodeTableIntoHistogramDescriptionTableMerger


def createAndSaveGlobalHistograms(symptomByBatchcodeTable, batchCodeTable):
    symptomByBatchcodeTable = symptomByBatchcodeTable.assign(COUNTRY = 'Global')
    dictByBatchcodeTable = createHistograms(symptomByBatchcodeTable)
    explodedTable = MultiIndexExploder.explodeMultiIndexOfTable(dictByBatchcodeTable)
    histogramDescriptionTable = HistogramDescriptionTableFactory.createHistogramDescriptionTable(explodedTable)
    histogramDescriptionTable = HistogramDescriptionTableSelector.selectHistogramsWithShortestBatchcodeCombinations(histogramDescriptionTable)
    histogramDescriptionTable = BatchCodeTableIntoHistogramDescriptionTableMerger().mergeBatchCodeTableIntoHistogramDescriptionTable(
        batchCodeTable = _rearrange(batchCodeTable),
        histogramDescriptionTable = histogramDescriptionTable)
    for country, histogramDescriptionTableForCountry in histogramDescriptionTable.groupby('COUNTRY'):
        print(f'saving histograms for {country}')
        saveHistograms(histogramDescriptionTableForCountry, country)


def _rearrange(batchCodeTable):
    batchCodeTable = batchCodeTable.set_index('Batch')
    batchCodeTable.index.rename('VAX_LOT', inplace = True)
    return batchCodeTable