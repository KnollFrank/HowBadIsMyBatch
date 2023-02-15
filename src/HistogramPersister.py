import shutil
from IOUtils import IOUtils

def saveHistograms(histogramDescriptionTable, country):
    directory = f'../docs/data/histograms/{country}'
    shutil.rmtree(directory, ignore_errors = True)
    for row in histogramDescriptionTable.itertuples():
        batchcode = row.Index
        histogramDescription = row.HISTOGRAM_DESCRIPTION
        IOUtils.saveDictAsJson(histogramDescription, f'{directory}/{batchcode}.json')
