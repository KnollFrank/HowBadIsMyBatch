class DataFrameFilter:

    @staticmethod
    def withoutZeroRowsAndZeroColumns(dataFrame):
        return DataFrameFilter._withoutZeroColumns(DataFrameFilter._withoutZeroRows(dataFrame))
        
    @staticmethod
    def _withoutZeroRows(dataFrame):
        return dataFrame.loc[~DataFrameFilter._isZeroRow(dataFrame)]

    @staticmethod
    def _isZeroRow(dataFrame):
        return (dataFrame == 0.0).all(axis = 'columns')

    @staticmethod
    def _withoutZeroColumns(dataFrame):
        return dataFrame.loc[:, (dataFrame != 0.0).any(axis = 'index')]
