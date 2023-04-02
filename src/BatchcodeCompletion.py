from SmartRegexpFactory import SmartRegexpFactory
import pandas as pd

class BatchcodeCompletion:
    
    def __init__(self, ADR_by_Batchcode):
        self.ADR_by_Batchcode = ADR_by_Batchcode.sort_values(by = 'Adverse Reaction Reports', ascending = False)

    def completeBatchcode(self, partialBatchcode):
        if pd.isna(partialBatchcode):
            return None
        return self._getBatchcodeHavingMostADRs(self._filterBy(partialBatchcode))
    
    def _filterBy(self, partialBatchcode):
        smartRegexp = SmartRegexpFactory().createSmartRegexp(partialBatchcode)
        return self.ADR_by_Batchcode[self.ADR_by_Batchcode.index.str.contains(smartRegexp, na = False, regex = True)]

    def _getBatchcodeHavingMostADRs(self, ADR_by_Batchcode):
        return ADR_by_Batchcode.index[0] if not ADR_by_Batchcode.empty else None
