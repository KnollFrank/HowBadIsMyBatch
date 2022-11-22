import pandas as pd


class TestHelper:

    @staticmethod
    def createDataFrame(index, columns, data, dtypes={}):
        return pd.DataFrame(index=index, columns=columns, data=data).astype(dtypes)
