from IOUtils import IOUtils
import numpy as np


def createAndSaveBatchCodeTables(
        minADRsForLethality,
        batchCodeTableFactory,
        onCountryProcessed = lambda country: None):
    _createAndSaveBatchCodeTableForCountry(
        createBatchCodeTableForCountry = lambda country: batchCodeTableFactory.createGlobalBatchCodeTable(),
        country = 'Global',
        minADRsForLethality = minADRsForLethality,
        onCountryProcessed = onCountryProcessed)


def _createAndSaveBatchCodeTableForCountry(createBatchCodeTableForCountry, country, minADRsForLethality, onCountryProcessed):
    batchCodeTable = createBatchCodeTableForCountry(country)
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
    IOUtils.saveDataFrameAsJson(
        batchCodeTable,
        '../docs/data/batchCodeTables/' + country + '.json')
    onCountryProcessed(country)
