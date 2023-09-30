import pandas as pd

class CountryCountsByClickedBatchcodeProvider:

    @staticmethod
    def getCountryCountsByClickedBatchcode(file):
        return CountryCountsByClickedBatchcodeProvider._read_csv(
            file = file,
            columns = {
                'Country': 'COUNTRY',
                'Event count': 'COUNTRY_COUNT_BY_VAX_LOT'
            },
            index_columns = ['COUNTRY'])
    
    @staticmethod
    def getCityCountsByClickedBatchcode(file):
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
    def _read_csv(file, columns, index_columns):
        exploration = pd.read_csv(file, index_col = 0, skiprows = [0, 1, 2, 3, 4, 5, 7])
        exploration.index.name = 'VAX_LOT'
        exploration.rename(
            columns = columns,
            inplace = True)
        exploration.set_index(index_columns, append = True, inplace = True)
        return exploration
