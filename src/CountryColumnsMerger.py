import pandas as pd


class CountryColumnsMerger:

    @staticmethod
    def mergeCountryColumnOfSrcIntoDst(src: pd.DataFrame, dst: pd.DataFrame):
        merged = pd.merge(
            dst,
            src,
            how = 'left',
            left_index = True,
            right_index = True,
            suffixes=('_dst', '_src'))
        merged['COUNTRY'] = (merged
                                .apply(
                                    lambda series: CountryColumnsMerger._merge(
                                                        series['COUNTRY_src'],
                                                        series['COUNTRY_dst']),
                                    axis = 'columns')
                                .astype('string'))
        return merged.drop(columns = ['COUNTRY_dst', 'COUNTRY_src'])
    
    @staticmethod
    def _merge(src, dst):
        if (CountryColumnsMerger._isNonUnique(src, dst)) or (pd.isnull(src) and pd.isnull(dst)):
            raise Exception()        
        
        return src if not pd.isnull(src) and pd.isnull(dst) else dst

    @staticmethod
    def _isNonUnique(src, dst):
        return not pd.isnull(src) and not pd.isnull(dst) and src != dst
    