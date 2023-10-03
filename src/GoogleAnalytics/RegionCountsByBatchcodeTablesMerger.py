from GoogleAnalytics.RegionCountsByClickedBatchcodeProvider import RegionCountsByClickedBatchcodeProvider
from GoogleAnalytics.FilesProvider import FilesProvider
from GoogleAnalytics.Resolution import Resolution
from TablesHelper import TablesHelper

class RegionCountsByBatchcodeTablesMerger:

    @staticmethod
    def getRegionCountsByClickedBatchcode(dataDir):
        files = FilesProvider(dataDir).getFilesHavingResolution(Resolution.CITY)
        tables = [RegionCountsByClickedBatchcodeProvider.getRegionCountsByClickedBatchcode(file) for file in files]
        table = TablesHelper.concatTables_groupByIndex_sum(tables)
        return table
