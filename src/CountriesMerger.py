import pandas as pd


class CountriesMerger:

    @staticmethod
    def mergeCountriesSerieses(countriesSeriesA, countriesSeriesB):
        return (pd
                .merge(countriesSeriesA, countriesSeriesB, how='left', left_index=True, right_index=True)
                .apply(lambda countries: sorted(set(countries.dropna())), axis='columns'))
