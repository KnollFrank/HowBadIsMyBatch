import pandas as pd


class CountriesMerger:

    @staticmethod
    def mergeSrcIntoDst(src: pd.Series, dst: pd.Series):
        def merge(series):
            return sorted(set().union(*series.dropna()))
        
        mergedSeries = (pd
                        .merge(dst, src, how='left', left_index=True, right_index=True)
                        .apply(merge, axis='columns'))
        mergedSeries.name = dst.name
        return mergedSeries
