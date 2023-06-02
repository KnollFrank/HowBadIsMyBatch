import pandas as pd
import glob
from CountryCountsByClickedBatchcodeProvider import CountryCountsByClickedBatchcodeProvider

class CountryCountsByBatchcodeTablesMerger:

    @staticmethod
    def mergeCountryCountsByBatchcodeTables(countryCountsByBatchcodeTables):
        return (pd
                .concat(countryCountsByBatchcodeTables)
                .groupby(countryCountsByBatchcodeTables[0].index.names)
                .sum())

    @staticmethod
    def getCountryCountsByClickedBatchcodeTable():
        return CountryCountsByBatchcodeTablesMerger.mergeCountryCountsByBatchcodeTables(CountryCountsByBatchcodeTablesMerger._getTables())

    @staticmethod
    def _getTables():
        files = glob.glob(r'data/*')
        return [CountryCountsByClickedBatchcodeProvider.getCountryCountsByClickedBatchcode(file) for file in files]
