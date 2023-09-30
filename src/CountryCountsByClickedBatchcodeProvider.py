import pandas as pd

class CountryCountsByClickedBatchcodeProvider:

    @staticmethod
    def getCountryCountsByClickedBatchcode(file):
        if CountryCountsByClickedBatchcodeProvider._hasCityColumn(file):
            return CountryCountsByClickedBatchcodeProvider._getCountryCountsByClickedBatchcode_fromCityResolution(file)
        else:
            return CountryCountsByClickedBatchcodeProvider._getCountryCountsByClickedBatchcode_fromCountryResolution(file)

    @staticmethod
    def _hasCityColumn(file):
        return 'City' in CountryCountsByClickedBatchcodeProvider._read_raw_csv(file).columns

    @staticmethod
    def _read_raw_csv(file):
        return pd.read_csv(file, index_col = 0, skiprows = [0, 1, 2, 3, 4, 5, 7])

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
        return CountryCountsByClickedBatchcodeProvider._read_csv(
            file = file,
            columns = {
                'Country': 'COUNTRY',
                'Region': 'REGION',
                'City': 'CITY',
                'Event count': 'CITY_COUNT_BY_VAX_LOT'
            },
            index_columns = ['COUNTRY', 'REGION', 'CITY'])

    @staticmethod
    def _getCountryCountsByClickedBatchcode_fromCountryResolution(file):
        return CountryCountsByClickedBatchcodeProvider._read_csv(
            file = file,
            columns = {
                'Country': 'COUNTRY',
                'Event count': 'COUNTRY_COUNT_BY_VAX_LOT'
            },
            index_columns = ['COUNTRY'])
    
    @staticmethod
    def _read_csv(file, columns, index_columns):
        dataframe = CountryCountsByClickedBatchcodeProvider._read_raw_csv(file)
        dataframe.index.name = 'VAX_LOT'
        dataframe.rename(
            columns = columns,
            inplace = True)
        dataframe.set_index(index_columns, append = True, inplace = True)
        return dataframe
    