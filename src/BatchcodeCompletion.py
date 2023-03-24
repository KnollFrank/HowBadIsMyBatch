from SmartRegexpFactory import SmartRegexpFactory

class BatchcodeCompletion:
    
    def __init__(self, ADR_by_Batchcode):
        self.ADR_by_Batchcode = ADR_by_Batchcode.sort_values(by = 'Adverse Reaction Reports', ascending = False)

    def completeBatchcode(self, partialBatchcode):
        smartRegexp = SmartRegexpFactory().createSmartRegexp(partialBatchcode)
        filteredBbatchCodeTable = self.ADR_by_Batchcode[self.ADR_by_Batchcode.index.str.contains(smartRegexp, na=False, regex=True)]
        return filteredBbatchCodeTable.index[0] if not filteredBbatchCodeTable.empty else None
