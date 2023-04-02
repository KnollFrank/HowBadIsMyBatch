from HistogramFactory import createHistograms
from HistogramPersister import saveHistograms
from MultiIndexExploder import MultiIndexExploder
from HistogramDescriptionTableFactory import HistogramDescriptionTableFactory


def createAndSaveGlobalHistograms(symptomByBatchcodeTable):
    symptomByBatchcodeTable = symptomByBatchcodeTable.assign(COUNTRY = 'Global')
    dictByBatchcodeTable = createHistograms(symptomByBatchcodeTable)
    explodedTable = MultiIndexExploder.explodeMultiIndexOfTable(dictByBatchcodeTable)
    histogramDescriptionTable = HistogramDescriptionTableFactory.createHistogramDescriptionTable(explodedTable)
    for country, histogramDescriptionTableForCountry in histogramDescriptionTable.groupby('COUNTRY'):
        print(f'saving histograms for {country}')
        saveHistograms(histogramDescriptionTableForCountry, country)