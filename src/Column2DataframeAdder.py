import pandas as pd


def addColumn2Dataframe(dataframe, column):
    return pd.merge(
        dataframe,
        column,
        how = 'left',
        left_on = 'LOT_NUMBER',
        right_index = True,
        validate = 'many_to_one')
