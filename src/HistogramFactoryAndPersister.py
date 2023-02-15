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
    for count, country in enumerate(countries, start = 1):
        _createAndSaveHistogramsForCountry(
            count = count,
            numCountries = len(countries),
            country = country,
            dictByBatchcodeTable = dictByBatchcodeTable)


def _createAndSaveHistogramsForCountry(count, numCountries, country, dictByBatchcodeTable):
    # FK-TODO: use https://github.com/tqdm/tqdm
    print(f'saving histograms for country {count}/{numCountries}: {country}')
    dictByBatchcodeTable4Country = dictByBatchcodeTable[dictByBatchcodeTable['COUNTRY'] == country]
    saveHistograms(dictByBatchcodeTable4Country, country)
