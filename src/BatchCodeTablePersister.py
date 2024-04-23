import numpy as np

def createGlobalBatchCodeTable(deleteEntriesWithADRsLessThanOrEqual, minADRsForLethality, batchCodeTableFactory):
    batchCodeTable = batchCodeTableFactory.createGlobalBatchCodeTable()
    batchCodeTable = batchCodeTable[~(batchCodeTable['Adverse Reaction Reports'] <= deleteEntriesWithADRsLessThanOrEqual)]
    batchCodeTable.index.set_names("Batch", inplace=True)
    if minADRsForLethality is not None:
        batchCodeTable.loc[
            batchCodeTable['Adverse Reaction Reports'] < minADRsForLethality,
            ['Severe reports', 'Lethality']
        ] = [np.nan, np.nan]
    batchCodeTable = batchCodeTable.reset_index();
    batchCodeTable = batchCodeTable[
        [
            'Batch',
            'Adverse Reaction Reports',
            'Deaths',
            'Disabilities',
            'Life Threatening Illnesses',
            'Hospitalizations',
            'Company',
            'Severe reports',
            'Lethality'
        ]]
    return batchCodeTable
