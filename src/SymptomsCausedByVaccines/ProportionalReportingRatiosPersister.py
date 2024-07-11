import shutil
from IOUtils import IOUtils

def saveProportionalReportingRatios(prrBySymptomByDrug, directory):
    shutil.rmtree(directory, ignore_errors = True)
    filenameByDrug = {}
    i = 0
    for drug, prrBySymptom in prrBySymptomByDrug.items():
        i += 1
        filename = f'{i}.json'
        filenameByDrug[drug] = filename
        IOUtils.saveDictAsJson(prrBySymptom, f'{directory}/{filename}')
    IOUtils.saveDictAsJson(filenameByDrug, f'{directory}/filenameByDrug.json')    
