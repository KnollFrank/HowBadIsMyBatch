import pandas as pd
from CompletedBatchcodeColumnAdder import CompletedBatchcodeColumnAdder
from BatchcodeCompletion import BatchcodeCompletion
from CountriesColumnAdder import CountriesColumnAdder
from BatchCodeTableFactory import BatchCodeTableFactory

def getCountriesByCompletedBatchcode(internationalVaersCovid19):
    result = _readExploration('data/Country By Batchcode Search Term.csv', indexName = 'Batchcode Search Term')
    result = _addCompletedBatchcodeColumn(result, internationalVaersCovid19)
    columnName = 'Countries'
    result = CountriesColumnAdder().addCountriesColumn(result, columnName = columnName)
    return result[[columnName]].droplevel('Batchcode Search Term')

def _addCompletedBatchcodeColumn(country_By_Batchcode_Search_Term, internationalVaersCovid19):
    return CompletedBatchcodeColumnAdder(_getCompleteBatchcode(internationalVaersCovid19)).addCompletedBatchcodeColumn(country_By_Batchcode_Search_Term)

def _getCompleteBatchcode(internationalVaersCovid19):
    batchCodeTable = BatchCodeTableFactory(internationalVaersCovid19).createGlobalBatchCodeTable()
    return BatchcodeCompletion(ADR_by_Batchcode = batchCodeTable).completeBatchcode
     
def getCountriesByClickedBatchcode():
    result = _readExploration('data/Country By Clicked Batchcode.csv', indexName = 'Clicked Batchcode')
    columnName = 'Countries'
    result = CountriesColumnAdder().addCountriesColumn(result, columnName = columnName)
    return result[[columnName]]

def _readExploration(csvFile, indexName):
    exploration = pd.read_csv(csvFile, header=[0], index_col=0, skiprows=6, on_bad_lines='warn')
    exploration.drop(index=indexName, inplace=True)
    exploration.index.rename(indexName, inplace=True)
    exploration.drop(columns='Totals', inplace=True)
    for column in exploration.columns:
           exploration[column] = exploration[column].astype('int64')
    return exploration