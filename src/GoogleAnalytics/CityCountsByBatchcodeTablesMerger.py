import pandas as pd
from GoogleAnalytics.RegionCountsByClickedBatchcodeProvider import RegionCountsByClickedBatchcodeProvider
from GoogleAnalytics.FilesProvider import FilesProvider
from GoogleAnalytics.Resolution import Resolution

class CityCountsByBatchcodeTablesMerger:

    @staticmethod
    def getCityCountsByClickedBatchcode(dataDir, includeDateRange = False):
        files = FilesProvider(dataDir).getFilesHavingResolution(Resolution.CITY)
        cityCountsByClickedBatchcodeTables = [RegionCountsByClickedBatchcodeProvider._getCityCountsByClickedBatchcode(file, includeDateRange) for file in files]
        table = pd.concat(cityCountsByClickedBatchcodeTables)
        return CityCountsByBatchcodeTablesMerger._getCityCountsByClickedBatchcodeFromTable(table)

    @staticmethod
    def _getCityCountsByClickedBatchcodeFromTable(cityCountsByClickedBatchcodeTable):
        return (cityCountsByClickedBatchcodeTable
                .groupby(cityCountsByClickedBatchcodeTable.index.names)
                .sum())
