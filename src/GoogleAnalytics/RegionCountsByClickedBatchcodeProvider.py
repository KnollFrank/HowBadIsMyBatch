import pandas as pd
from GoogleAnalytics.GoogleAnalyticsReader import GoogleAnalyticsReader

class RegionCountsByClickedBatchcodeProvider:

    @staticmethod
    def getRegionCountsByClickedBatchcode(file):
        return RegionCountsByClickedBatchcodeProvider._getRegionCountsByClickedBatchcodeFromTable(RegionCountsByClickedBatchcodeProvider._getCityCountsByClickedBatchcode(file))

    # FK-TODO: delegate same method CountryCountsByClickedBatchcodeProvider._getCityCountsByClickedBatchcode() to here
    @staticmethod
    def _getCityCountsByClickedBatchcode(file, includeDateRange = False):
        return GoogleAnalyticsReader.read_csv(
            file = file,
            columns = {
                'Country': 'COUNTRY',
                'Region': 'REGION',
                'City': 'CITY',
                'Event count': 'CITY_COUNT_BY_VAX_LOT'
            },
            index_columns = ['COUNTRY', 'REGION', 'CITY'],
            # FK-TODO: inline {'startDate' : 'START_DATE', 'endDate': 'END_DATE'} ?
            dateRangeIndexColumns = {'startDate' : 'START_DATE', 'endDate': 'END_DATE'} if includeDateRange else None)

    @staticmethod
    def _getRegionCountsByClickedBatchcodeFromTable(cityCountsByClickedBatchcodeTable):
        return (cityCountsByClickedBatchcodeTable
                .groupby(['VAX_LOT', 'COUNTRY', 'REGION'])
                .agg(REGION_COUNT_BY_VAX_LOT =
                      pd.NamedAgg(
                          column = 'CITY_COUNT_BY_VAX_LOT',
                          aggfunc = sum)))
