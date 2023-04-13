from IOUtils import IOUtils
import numpy as np


def createAndSaveGlobalBatchCodeTable(minADRsForLethality, batchCodeTableFactory):
    batchCodeTable = batchCodeTableFactory.createGlobalBatchCodeTable()
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
            'Company',
            'Severe reports',
            'Lethality'
        ]]
    # FK-TODO: remove Global.json
    IOUtils.saveDataFrameAsJson(batchCodeTable, '../docs/data/batchCodeTables/Global.json')
    return batchCodeTable
