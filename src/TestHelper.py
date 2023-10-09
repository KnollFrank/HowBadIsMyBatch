import pandas as pd


class TestHelper:

    @staticmethod
    def createDataFrame(columns, data, dtypes={}, **kwargs):
        return pd.DataFrame(columns=columns, data=data, **kwargs).astype(dtypes)

    @staticmethod
    def createSeries(indexName, **kwargs):
        series = pd.Series(**kwargs)
        series.index.name = indexName
        return series
