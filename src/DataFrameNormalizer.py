import numpy as np

class DataFrameNormalizer:
    
    @staticmethod
    def convertVAX_LOTColumnToUpperCase(dataFrame):
        dataFrame['VAX_LOT'] = dataFrame['VAX_LOT'].str.upper()

    @staticmethod
    def removeUnknownBatchCodes(dataFrame):
        dataFrame.drop(DataFrameNormalizer._isUnknownBatchCode(dataFrame).index, inplace = True)

    @staticmethod
    def _isUnknownBatchCode(dataFrame):
        return dataFrame[dataFrame['VAX_LOT'].str.contains(pat = 'UNKNOWN', regex = False, case = False, na = False)]

    @staticmethod
    def _convertColumnsOfDataFrame_Y_to_1_else_0(dataFrame, columns):
        for column in columns:
            DataFrameNormalizer._convertColumnOfDataFrame_Y_to_1_else_0(dataFrame, column)

    @staticmethod
    def _convertColumnOfDataFrame_Y_to_1_else_0(dataFrame, column):
        dataFrame[column] = DataFrameNormalizer._where(
            condition = dataFrame[column] == 'Y',
            trueValue = 1,
            falseValue = 0)

    @staticmethod
    def _where(condition, trueValue, falseValue):
        return np.where(condition, trueValue, falseValue)    
    