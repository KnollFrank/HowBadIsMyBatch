import pandas as pd
from CompletedBatchcodeColumnAdder import CompletedBatchcodeColumnAdder
from BatchcodeCompletion import BatchcodeCompletion
from CountriesColumnAdder import CountriesColumnAdder
from BatchCodeTableFactory import BatchCodeTableFactory

def getCountriesByCompletedBatchcode(internationalVaersCovid19):
    batchCodeTable = BatchCodeTableFactory(internationalVaersCovid19).createGlobalBatchCodeTable()
    country_By_Batchcode_Search_Term = _readExploration('data/Country By Batchcode Search Term.csv', indexName = 'Batchcode Search Term')
    completedBatchcodeColumnAdder = CompletedBatchcodeColumnAdder(BatchcodeCompletion(ADR_by_Batchcode = batchCodeTable).completeBatchcode)
    country_By_Batchcode_Search_Term = completedBatchcodeColumnAdder.addCompletedBatchcodeColumn(country_By_Batchcode_Search_Term)
    columnName = 'Countries'
    country_By_Batchcode_Search_Term = CountriesColumnAdder().addCountriesColumn(
        country_By_Batchcode_Search_Term,
        columnName = columnName)
    country_By_Batchcode_Search_Term = country_By_Batchcode_Search_Term[[columnName]].droplevel('Batchcode Search Term')
    return country_By_Batchcode_Search_Term

def getCountriesByClickedBatchcode():
    country_By_Clicked_Batchcode = _readExploration(
        'data/Country By Clicked Batchcode.csv',
        indexName = 'Clicked Batchcode')
    columnName = 'Countries'
    country_By_Clicked_Batchcode = CountriesColumnAdder().addCountriesColumn(
        country_By_Clicked_Batchcode,
        columnName = columnName)
    country_By_Clicked_Batchcode = country_By_Clicked_Batchcode[[columnName]]
    return country_By_Clicked_Batchcode

def _readExploration(csvFile, indexName):
    exploration = pd.read_csv(csvFile, header=[0], index_col=0, skiprows=6, on_bad_lines='warn')
    exploration.drop(index=indexName, inplace=True)
    exploration.index.rename(indexName, inplace=True)
    exploration.drop(columns='Totals', inplace=True)
    for column in exploration.columns:
           exploration[column] = exploration[column].astype('int64')
    return exploration