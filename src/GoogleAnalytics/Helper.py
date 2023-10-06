import shutil

def persistCityCountsByClickedBatchcodeTables(dataDir, n, cityCountsByClickedBatchcodeTable):
    _prepare(dataDir)
    for row in _getMostCommonBatchesTable(n, cityCountsByClickedBatchcodeTable).itertuples():
        _persistCityCountsByClickedBatchcodeTable(
            dataDir = dataDir,
            batch = row.Index,
            count = row.CITY_COUNT_BY_VAX_LOT,
            cityCountsByClickedBatchcodeTable = cityCountsByClickedBatchcodeTable.loc[(row.Index, slice(None), slice(None), slice(None)), :])

def _prepare(dataDir):
    shutil.rmtree(dataDir, ignore_errors = True)
    dataDir.mkdir(parents = True, exist_ok = True)

def _getMostCommonBatchesTable(n, cityCountsByClickedBatchcodeTable):
    df_sorted = _dataframeWithoutIndexValue(
        dataframe = (cityCountsByClickedBatchcodeTable
                        .groupby('VAX_LOT')
                        .sum()
                        .sort_values(by = 'CITY_COUNT_BY_VAX_LOT', ascending = False)),
        indexValue = '(not set)')
    return df_sorted.iloc[:n]

def _dataframeWithoutIndexValue(dataframe, indexValue):
    return dataframe[dataframe.index != indexValue]
    
def _persistCityCountsByClickedBatchcodeTable(dataDir, batch, count, cityCountsByClickedBatchcodeTable):
    (cityCountsByClickedBatchcodeTable
    .reset_index()
    .to_excel(f'{str(dataDir)}/{count}_{batch}.xlsx'))
