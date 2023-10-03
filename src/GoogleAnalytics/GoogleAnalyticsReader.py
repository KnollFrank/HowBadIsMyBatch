import pandas as pd

class GoogleAnalyticsReader:

    @staticmethod
    def read_csv(file, columns, index_columns):
        dataframe = pd.read_csv(file, index_col = 0, skiprows = [0, 1, 2, 3, 4, 5, 7])
        dataframe.index.name = 'VAX_LOT'
        dataframe.rename(
            columns = columns,
            inplace = True)
        dataframe.set_index(index_columns, append = True, inplace = True)
        return dataframe
