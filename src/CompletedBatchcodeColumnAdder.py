import pandas as pd


class CompletedBatchcodeColumnAdder:

    def __init__(self, completeBatchcode):
        self.completeBatchcode = completeBatchcode

    def addCompletedBatchcodeColumn(self, tableByPartialBatchcode):
        partialBatchcodeTable = tableByPartialBatchcode.index.to_frame()
        partialBatchcodeTable['Completed Batchcode'] = partialBatchcodeTable[tableByPartialBatchcode.index.name].map(self.completeBatchcode)
        return tableByPartialBatchcode.set_index(pd.MultiIndex.from_frame(partialBatchcodeTable))
