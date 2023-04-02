from CountriesMerger import CountriesMerger
from CountriesByBatchcodeProvider import getCountriesByBatchcodeBeforeDeletion
from BatchCodeTableFactory import BatchCodeTableFactory

class BatchCodeTableHavingGuessedCountriesFactory:

    def __init__(self, batchCodeTableFactoryDelegate):
        self.batchCodeTableFactoryDelegate = batchCodeTableFactoryDelegate
        self.countriesByBatchcodeBeforeDeletion = getCountriesByBatchcodeBeforeDeletion()

    def createGlobalBatchCodeTable(self, countriesAsList = False):
        batchCodeTable = self.batchCodeTableFactoryDelegate.createGlobalBatchCodeTable(countriesAsList = True)
        self._guessCountries(batchCodeTable, countriesAsList)
        return batchCodeTable

    def createBatchCodeTableByCountry(self, country, countriesAsList = False):
        batchCodeTable = self.batchCodeTableFactoryDelegate.createBatchCodeTableByCountry(country, countriesAsList = True)
        self._guessCountries(batchCodeTable, countriesAsList)
        return batchCodeTable

    def _guessCountries(self, batchCodeTable, countriesAsList):
        batchCodeTable['Countries'] = CountriesMerger.mergeSrcIntoDst(
            dst = batchCodeTable['Countries'],
            src = self.countriesByBatchcodeBeforeDeletion['Countries'])
