import shutil
from IOUtils import IOUtils

def saveProportionalReportingRatios(prrBySymptomByDrug, directory):
    shutil.rmtree(directory, ignore_errors = True)
    drugByFilename = {}
    i = 0
    for drug, prrBySymptom in prrBySymptomByDrug.items():
        i += 1
        drugByFilename[f'{i}.json'] = drug
        IOUtils.saveDictAsJson(prrBySymptom, f'{directory}/{i}.json')
    IOUtils.saveDictAsJson(drugByFilename, f'{directory}/drugByFilename.json')    
