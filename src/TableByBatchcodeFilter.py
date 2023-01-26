class TableByBatchcodeFilter:

    @staticmethod
    def filterTableByBatchcode(batchcode, table):
        table = table.reset_index()
        filteredTable = table[
            (table['VAX_LOT1'] == batchcode) |
            (table['VAX_LOT2'] == batchcode)]
        return filteredTable.set_index(['VAX_LOT1', 'VAX_LOT2'])
