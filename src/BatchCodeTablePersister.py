from IOUtils import IOUtils
from BatchCodeTableFactory import BatchCodeTableFactory
import numpy as np
from HtmlUtils import getCountries


def createAndSaveBatchCodeTables(internationalVaersCovid19, minADRsForLethality):
    batchCodeTableFactory = BatchCodeTableFactory(internationalVaersCovid19)
    _createAndSaveBatchCodeTablesForCountries(
        createBatchCodeTableForCountry=lambda country: batchCodeTableFactory.createBatchCodeTableByCountry(country),
        countries=getCountries(internationalVaersCovid19),
        minADRsForLethality=minADRsForLethality)
    _createAndSaveBatchCodeTableForCountry(
        createBatchCodeTableForCountry=lambda country: batchCodeTableFactory.createGlobalBatchCodeTable(),
        country='Global',
        minADRsForLethality=minADRsForLethality)


def _createAndSaveBatchCodeTableForCountry(createBatchCodeTableForCountry, country, minADRsForLethality=None):
    batchCodeTable = createBatchCodeTableForCountry(country)
    batchCodeTable.index.set_names("Batch", inplace=True)
    if minADRsForLethality is not None:
        batchCodeTable.loc[
            batchCodeTable['Adverse Reaction Reports'] < minADRsForLethality,
            ['Severe reports', 'Lethality']
        ] = [np.nan, np.nan]
    IOUtils.saveDataFrame(
        batchCodeTable,
        '../docs/data/batchCodeTables/' + country)
    # display(country + ":", batchCodeTable)
    display(country)


def _createAndSaveBatchCodeTablesForCountries(createBatchCodeTableForCountry, countries, minADRsForLethality=None):
    for country in countries:
        _createAndSaveBatchCodeTableForCountry(
            createBatchCodeTableForCountry, country, minADRsForLethality)
