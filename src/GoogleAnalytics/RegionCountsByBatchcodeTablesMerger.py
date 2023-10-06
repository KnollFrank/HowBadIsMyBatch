import pandas as pd
from GoogleAnalytics.RegionCountsByClickedBatchcodeProvider import RegionCountsByClickedBatchcodeProvider
from GoogleAnalytics.FilesProvider import FilesProvider
from GoogleAnalytics.Resolution import Resolution

class RegionCountsByBatchcodeTablesMerger:

    @staticmethod
    def getRegionCountsByClickedBatchcode(dataDir):
        files = FilesProvider(dataDir).getFilesHavingResolution(Resolution.CITY)
        cityCountsByClickedBatchcodeTables = [RegionCountsByClickedBatchcodeProvider._getCityCountsByClickedBatchcode(file) for file in files]
        table = pd.concat(cityCountsByClickedBatchcodeTables)
        return RegionCountsByClickedBatchcodeProvider._getRegionCountsByClickedBatchcodeFromTable(table)
