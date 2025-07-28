import pandas as pd

class VaersDescr2DataFrameConverter:

    @staticmethod
    def createDataFrameFromDescr(vaersDescr):
        return pd.merge(
                vaersDescr['VAERSDATA'],
                vaersDescr['VAERSVAX'],
                how = 'left',
                left_index = True,
                right_index = True,
                validate = 'many_to_many')

    @staticmethod
    def createDataFrameFromDescrs(vaersDescrs):
        dataFrames = [VaersDescr2DataFrameConverter.createDataFrameFromDescr(vaersDescr) for vaersDescr in vaersDescrs]
        return pd.concat(dataFrames)
