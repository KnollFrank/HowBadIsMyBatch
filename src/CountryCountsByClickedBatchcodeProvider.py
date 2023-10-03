import pandas as pd
from GoogleAnalytics.ResolutionProvider import Resolution, ResolutionProvider
from GoogleAnalytics.GoogleAnalyticsReader import GoogleAnalyticsReader
from GoogleAnalytics.RegionCountsByClickedBatchcodeProvider import RegionCountsByClickedBatchcodeProvider

class CountryCountsByClickedBatchcodeProvider:

    @staticmethod
    def getCountryCountsByClickedBatchcode(file):
        if ResolutionProvider.getResolution(file) == Resolution.CITY:
            return CountryCountsByClickedBatchcodeProvider._getCountryCountsByClickedBatchcode_fromCityResolution(file)
        else:
            return CountryCountsByClickedBatchcodeProvider._getCountryCountsByClickedBatchcode_fromCountryResolution(file)

    @staticmethod
    def _getCountryCountsByClickedBatchcode_fromCityResolution(file):
        cityCountsByClickedBatchcodeTable = CountryCountsByClickedBatchcodeProvider._getCityCountsByClickedBatchcode(file)
        return (cityCountsByClickedBatchcodeTable
                .groupby(['VAX_LOT', 'COUNTRY'])
                .agg(COUNTRY_COUNT_BY_VAX_LOT =
                      pd.NamedAgg(
                          column = 'CITY_COUNT_BY_VAX_LOT',
                          aggfunc = sum)))

    @staticmethod
    def _getCityCountsByClickedBatchcode(file):
        return RegionCountsByClickedBatchcodeProvider._getCityCountsByClickedBatchcode(file)

    @staticmethod
    def _getCountryCountsByClickedBatchcode_fromCountryResolution(file):
        return GoogleAnalyticsReader.read_csv(
            file = file,
            columns = {
                'Country': 'COUNTRY',
                'Event count': 'COUNTRY_COUNT_BY_VAX_LOT'
            },
            index_columns = ['COUNTRY'])
