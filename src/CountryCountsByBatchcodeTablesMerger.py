import pandas as pd

class CountryCountsByBatchcodeTablesMerger:

    @staticmethod
    def merge(countryCountsByBatchcodeTables):
        return (pd
                .concat(countryCountsByBatchcodeTables)
                .groupby(countryCountsByBatchcodeTables[0].index.names)
                .sum())
