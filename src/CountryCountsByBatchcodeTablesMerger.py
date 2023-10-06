import glob
from CountryCountsByClickedBatchcodeProvider import CountryCountsByClickedBatchcodeProvider
from TablesHelper import TablesHelper

class CountryCountsByBatchcodeTablesMerger:

    @staticmethod
    def getCountryCountsByClickedBatchcodeTable():
        return TablesHelper.concatTables_groupByIndex_sum(CountryCountsByBatchcodeTablesMerger._getTables())

    @staticmethod
    def _getTables():
        files = glob.glob(r'data/GoogleAnalytics/*')
        return [CountryCountsByClickedBatchcodeProvider.getCountryCountsByClickedBatchcode(file) for file in files]
