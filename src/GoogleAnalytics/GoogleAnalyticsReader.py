import pandas as pd
from GoogleAnalyticsReader import GoogleAnalyticsReader as GAReader

class GoogleAnalyticsReader:

    @staticmethod
    def read_csv(file, columns, index_columns, dateRangeIndexColumns = None):
        dataframe = pd.read_csv(file, index_col = 0, skiprows = [0, 1, 2, 3, 4, 5, 7])
        dataframe.index.name = 'VAX_LOT'
        dataframe.rename(
            columns = columns,
            inplace = True)
        dataframe.set_index(index_columns, append = True, inplace = True)
        if dateRangeIndexColumns is not None:
            GoogleAnalyticsReader._addDateRangeIndexColumns(
                dataframe = dataframe,
                dateRange = GAReader._getDateRange(file),
                columns = [dateRangeIndexColumns['startDate'], dateRangeIndexColumns['endDate']])
        return dataframe

    @staticmethod
    def _addDateRangeIndexColumns(dataframe, dateRange, columns):
        dataframe[columns[0]] = dateRange[0]
        dataframe[columns[1]] = dateRange[1]
        dataframe.set_index(columns, append = True, inplace = True)
