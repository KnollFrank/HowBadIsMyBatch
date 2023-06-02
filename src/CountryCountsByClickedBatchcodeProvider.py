import pandas as pd

class CountryCountsByClickedBatchcodeProvider:

    @staticmethod
    def getCountryCountsByClickedBatchcode(file):
        exploration = pd.read_csv(file, index_col = 0, skiprows = [0, 1, 2, 3, 4, 5, 7])
        exploration.index.name = 'VAX_LOT'
        exploration.rename(
            columns =
            {
                'Country': 'COUNTRY',
                'Event count': 'COUNTRY_COUNT_BY_VAX_LOT'
            },
            inplace = True)
        exploration.set_index('COUNTRY',append = True, inplace = True)
        return exploration
