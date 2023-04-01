from IOUtils import IOUtils
from BatchCodeTableFactory import BatchCodeTableFactory
import numpy as np
from HtmlUtils import getCountries


def createAndSaveBatchCodeTables(
        internationalVaersCovid19,
        minADRsForLethality,
        onCountryProcessed = lambda country: None):
    batchCodeTableFactory = BatchCodeTableFactory(internationalVaersCovid19)
    _createAndSaveBatchCodeTablesForCountries(
        createBatchCodeTableForCountry = lambda country: batchCodeTableFactory.createBatchCodeTableByCountry(country),
        countries = getCountries(internationalVaersCovid19),
        minADRsForLethality = minADRsForLethality,
        onCountryProcessed = onCountryProcessed)
    _createAndSaveBatchCodeTableForCountry(
        # FK-TODO: createBatchCodeTableForCountry so definieren, dass createGlobalBatchCodeTable() sofort die gemergten Countries erzeugt
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
            'Countries',
            'Severe reports',
            'Lethality'
        ]]
    IOUtils.saveDataFrameAsJson(
        batchCodeTable,
        '../docs/data/batchCodeTables/' + country + '.json')
    onCountryProcessed(country)


def _createAndSaveBatchCodeTablesForCountries(createBatchCodeTableForCountry, countries, minADRsForLethality, onCountryProcessed):
    for country in countries:
        _createAndSaveBatchCodeTableForCountry(createBatchCodeTableForCountry, country, minADRsForLethality, onCountryProcessed)
