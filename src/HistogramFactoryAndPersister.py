from HistogramFactory import createGlobalHistograms, createHistograms
from HistogramPersister import saveHistograms
from MultiIndexExploder import MultiIndexExploder
from HistogramDescriptionTableFactory import HistogramDescriptionTableFactory


def createAndSaveGlobalHistograms(symptomByBatchcodeTable):
    dictByBatchcodeTable4Country = createGlobalHistograms(symptomByBatchcodeTable)
    explodedTable = MultiIndexExploder.explodeMultiIndexOfTable(dictByBatchcodeTable4Country)
    histogramDescriptionTable = HistogramDescriptionTableFactory.createHistogramDescriptionTable(explodedTable)
    saveHistograms(histogramDescriptionTable, 'Global')


def createAndSaveHistogramsForCountries(symptomByBatchcodeTable, countries):
    dictByBatchcodeTable = createHistograms(symptomByBatchcodeTable)
    explodedTable = MultiIndexExploder.explodeMultiIndexOfTable(dictByBatchcodeTable)
    histogramDescriptionTable = HistogramDescriptionTableFactory.createHistogramDescriptionTable(explodedTable)
    for country, histogramDescriptionTableForCountry in histogramDescriptionTable.groupby('COUNTRY'):
        print(country, ':')
        saveHistograms(histogramDescriptionTableForCountry, country)