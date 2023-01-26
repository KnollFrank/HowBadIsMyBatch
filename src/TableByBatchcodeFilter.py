from functools import reduce


class TableByBatchcodeFilter:

    @staticmethod
    def filterTableByBatchcode(batchcode, table):
        batchcodeColumns = table.index.names
        table = table.reset_index()
        filteredTable = table[TableByBatchcodeFilter._existsBatchcodeInAnyBatchcodeColumn(table, batchcodeColumns, batchcode)]
        return filteredTable.set_index(batchcodeColumns)

    @staticmethod
    def _existsBatchcodeInAnyBatchcodeColumn(table, batchcodeColumns, batchcode):
        return reduce(
            lambda accum, batchcodeColumn: accum | (table[batchcodeColumn] == batchcode),
            batchcodeColumns,
            [False] * len(table.index))
