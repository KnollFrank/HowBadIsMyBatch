import pandas as pd


class TablesHelper:

    @staticmethod
    def concatTables_groupByIndex_sum(tables):
        return (pd
                .concat(tables)
                .groupby(tables[0].index.names)
                .sum())
