from MultiIndexValuesProvider import MultiIndexValuesProvider
from HistogramDescriptionPersister import HistogramDescriptionPersister
import shutil

def saveHistograms(dictByBatchcodeTable4Country, country):
    batchcodes = MultiIndexValuesProvider.getValues(dictByBatchcodeTable4Country.index)
    batchcodes = {batchcode for batchcode in batchcodes if batchcode != 'nan'}
    directory = f'../docs/data/histograms/{country}'
    shutil.rmtree(directory, ignore_errors = True)
    HistogramDescriptionPersister(directory).saveHistogramDescriptionsForBatchcodes(
        batchcodes,
        dictByBatchcodeTable4Country,
        progress = lambda count, size, batchcode: print(f'{count}/{size}: {batchcode}'))
