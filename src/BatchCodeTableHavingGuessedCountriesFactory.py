from CountriesMerger import CountriesMerger
from CountriesByBatchcodeProvider import getCountriesByBatchcodeBeforeDeletion, getCountriesByClickedBatchcode
from BatchCodeTableFactory import BatchCodeTableFactory

class BatchCodeTableHavingGuessedCountriesFactory:

    def __init__(self, batchCodeTableFactoryDelegate):
        self.batchCodeTableFactoryDelegate = batchCodeTableFactoryDelegate
        self.countriesByBatchcodeBeforeDeletion = getCountriesByBatchcodeBeforeDeletion()
        self.countriesByClickedBatchcode = getCountriesByClickedBatchcode()

    def createGlobalBatchCodeTable(self, countriesAsList = False):
        batchCodeTable = self.batchCodeTableFactoryDelegate.createGlobalBatchCodeTable(countriesAsList = True)
        self._guessCountries(batchCodeTable, countriesAsList)
        return batchCodeTable

    def createBatchCodeTableByCountry(self, country, countriesAsList = False):
        batchCodeTable = self.batchCodeTableFactoryDelegate.createBatchCodeTableByCountry(country, countriesAsList = True)
        self._guessCountries(batchCodeTable, countriesAsList)
        return batchCodeTable

    def _guessCountries(self, batchCodeTable, countriesAsList):
        self._mergeCountriesOfSrcIntoDst(
            dst = batchCodeTable,
            src = self.countriesByBatchcodeBeforeDeletion)
        self._mergeCountriesOfSrcIntoDst(
            dst = batchCodeTable,
            src = self.countriesByClickedBatchcode)
        BatchCodeTableFactory._convertCountries(batchCodeTable, countriesAsList)

    def _mergeCountriesOfSrcIntoDst(self, dst, src):
        dst['Countries'] = CountriesMerger.mergeSrcIntoDst(dst = dst['Countries'], src = src['Countries'])
