import shutil
from IOUtils import IOUtils

def saveProportionalReportingRatios(prrByVaccineBySymptom, directory):
    shutil.rmtree(directory, ignore_errors = True)
    for symptom, prrByVaccine in prrByVaccineBySymptom.items():
        IOUtils.saveDictAsJson(prrByVaccine, f'{directory}/{symptom}.json')
