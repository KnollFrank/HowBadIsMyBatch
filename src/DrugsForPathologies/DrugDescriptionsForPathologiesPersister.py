import shutil
from IOUtils import IOUtils

def saveDrugDescriptionsForPathologies(drugDescrByPathology, directory):
    shutil.rmtree(directory, ignore_errors = True)
    filenameByPathology = {}
    i = 0
    for pathology, drugDescr in drugDescrByPathology.items():
        i += 1
        filenameByPathology[pathology] = f'{i}'
        drugDescr['PATHOLOGY'] = pathology
        IOUtils.saveDictAsJson(drugDescr, f'{directory}/{i}.json')
    return filenameByPathology    
