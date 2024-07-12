import shutil
from IOUtils import IOUtils

def saveProportionalReportingRatios(prrBySymptomByDrug, directory):
    shutil.rmtree(directory, ignore_errors = True)
    filenameByDrug = {}
    i = 0
    for drug, prrBySymptom in prrBySymptomByDrug.items():
        i += 1
        filenameByDrug[drug] = f'{i}'
        IOUtils.saveDictAsJson(prrBySymptom, f'{directory}/{i}.json')
    return filenameByDrug    
