import pandas as pd


class MultiIndexValuesProvider:

    @staticmethod
    def getValues(multiIndex):
        df = multiIndex.to_frame(index = False)
        values = (pd
                    .concat([df[column] for column in df.columns])
                    .unique())
        return set(values)
