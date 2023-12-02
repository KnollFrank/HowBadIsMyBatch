class DataFrameFilter:

    @staticmethod
    def withoutZeroRowsAndZeroColumns(dataFrame):
        return DataFrameFilter._withoutZeroColumns(DataFrameFilter._withoutZeroRows(dataFrame))
        
    @staticmethod
    def _withoutZeroRows(dataFrame):
        isZeroRow = DataFrameFilter._isAllZero(dataFrame, 'columns')
        return dataFrame.loc[~isZeroRow]

    @staticmethod
    def _withoutZeroColumns(dataFrame):
        isZeroColumn = DataFrameFilter._isAllZero(dataFrame, 'index')
        return dataFrame.loc[:, ~isZeroColumn]
    
    @staticmethod
    def _isAllZero(dataFrame, axis):
        return (dataFrame == 0.0).all(axis = axis)
