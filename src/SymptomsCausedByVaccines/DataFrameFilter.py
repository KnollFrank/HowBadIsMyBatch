class DataFrameFilter:

    @staticmethod
    def withoutZeroRows(dataFrame):
        return dataFrame.loc[~DataFrameFilter._isZeroRow(dataFrame)]

    @staticmethod
    def _isZeroRow(dataFrame):
        return (dataFrame == 0.0).all(axis = 'columns')
