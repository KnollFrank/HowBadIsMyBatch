import shutil
from IOUtils import IOUtils

def saveBarChartDescriptionTable(barChartDescriptionTable):
    directory = '../docs/data/barChartDescriptionTables'
    shutil.rmtree(directory, ignore_errors = True)
    for row in barChartDescriptionTable.itertuples():
        batchcode = row.BAR_CHART_DESCRIPTION['batchcode']
        barChartDescription = row.BAR_CHART_DESCRIPTION
        IOUtils.saveDictAsJson(barChartDescription, f'{directory}/{batchcode}.json')
