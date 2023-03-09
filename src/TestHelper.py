import pandas as pd


class TestHelper:

    @staticmethod
    def createDataFrame(columns, data, dtypes={}, **kwargs):
        return pd.DataFrame(columns=columns, data=data, **kwargs).astype(dtypes)
