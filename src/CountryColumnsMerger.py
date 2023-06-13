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
            suffixes = ('_dst', '_src'))
        merged['COUNTRY'] = (merged
                                .apply(
                                    lambda series: CountryColumnsMerger._mergeSrcIntoDst(
                                                        series['COUNTRY_src'],
                                                        series['COUNTRY_dst']),
                                    axis = 'columns')
                                .astype('string'))
        return merged.drop(columns = ['COUNTRY_dst', 'COUNTRY_src'])
    
    @staticmethod
    def _mergeSrcIntoDst(src, dst):
        if (CountryColumnsMerger._notEqual(src, dst)) or (pd.isnull(src) and pd.isnull(dst)):
            raise Exception()        
        
        if pd.isnull(dst) and not pd.isnull(src):
            return src
        else:
            return dst

    @staticmethod
    def _notEqual(src, dst):
        return not pd.isnull(src) and not pd.isnull(dst) and src != dst
    