from IOUtils import IOUtils
import numpy as np

def createAndSaveBatchCodeTableForCountry(createBatchCodeTableForCountry, country, minADRsForLethality = None):
    batchCodeTable = createBatchCodeTableForCountry(country)
    batchCodeTable.index.set_names("Batch", inplace = True)
    if minADRsForLethality is not None:
        batchCodeTable.loc[batchCodeTable['Adverse Reaction Reports'] < minADRsForLethality, ['Severe reports', 'Lethality']] = [np.nan, np.nan]
    IOUtils.saveDataFrame(batchCodeTable, '../docs/data/batchCodeTables/' + country)
    # display(country + ":", batchCodeTable)
    display(country)

def createAndSaveBatchCodeTablesForCountries(createBatchCodeTableForCountry, countries, minADRsForLethality = None):
    for country in countries:
        createAndSaveBatchCodeTableForCountry(createBatchCodeTableForCountry, country, minADRsForLethality)