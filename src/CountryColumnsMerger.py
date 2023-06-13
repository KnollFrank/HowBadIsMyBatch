import pandas as pd


class CountryColumnsMerger:

    @staticmethod
    def mergeCountryColumnOfSrcIntoDst(src: pd.DataFrame, dst: pd.DataFrame):
        def merge(series):
            if pd.isnull(series['COUNTRY_dst']):
                return series['COUNTRY_src']
            else:
                return series['COUNTRY_dst']

        merged = pd.merge(
            dst,
            src,
            how = 'left',
            left_index = True,
            right_index = True,
            suffixes=('_dst', '_src'))
        merged['COUNTRY'] = merged.apply(merge, axis = 'columns').astype('string')
        return merged.drop(columns = ['COUNTRY_dst', 'COUNTRY_src'])
    