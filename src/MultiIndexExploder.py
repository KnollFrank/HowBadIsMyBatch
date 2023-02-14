import numpy as np
import Utils


class MultiIndexExploder:

    @staticmethod
    def explodeMultiIndexOfTable(table):
        batchcodeColumns = table.index.names
        explodedTable = table.loc[np.repeat(table.index, len(batchcodeColumns))].reset_index()
        explodedTable['VAX_LOT_EXPLODED'] = Utils.flatten(table.index.values)
        return explodedTable.set_index(['VAX_LOT_EXPLODED'] + batchcodeColumns)
