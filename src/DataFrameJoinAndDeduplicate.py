import pandas as pd

class DataFrameJoinAndDeduplicate:

    @staticmethod
    def mergeDataframesAndDeduplicateByIndex(left: pd.DataFrame, right: pd.DataFrame):
        return DataFrameJoinAndDeduplicate._drop_duplicates(
            pd.merge(
                left,
                right,
                how = 'left',
                left_index = True,
                right_index = True,
                validate = 'many_to_many'))

    @staticmethod
    def mergeListOfDataframesAndDeduplicateByIndex(listOfDataframes):
        dataFrames = [DataFrameJoinAndDeduplicate.mergeDataframesAndDeduplicateByIndex(dataFrameLeft, dataFrameRight) for (dataFrameLeft, dataFrameRight) in listOfDataframes]
        return pd.concat(dataFrames)

    @staticmethod
    def _drop_duplicates(df):
        return df[~df.index.duplicated(keep = False)]
