from bs4 import BeautifulSoup
from HtmlTransformerUtil import HtmlTransformerUtil
from DateProvider import DateProvider
from SymptomsCausedByVaccines.HtmlUtils import getSymptomOptions, getVaccineOptions
from SymptomsCausedByVaccines.OptionsSetter import OptionsSetter


def updateHtmlFile(symptomsDescr, vaccinesDescr, htmlFile, defaultSelectVaccineOptionText):
    _saveOptions(
        options = getSymptomOptions(
            symptoms = symptomsDescr['symptoms'],
            filenameBySymptom = symptomsDescr['filenameBySymptom']),
        htmlFile = htmlFile,
        selectElementId = 'symptomSelect')
    
    _saveOptions(
        options = getVaccineOptions(
            vaccines = vaccinesDescr['vaccines'],
            filenameByDrug = vaccinesDescr['filenameByDrug'],
            defaultOptionText = defaultSelectVaccineOptionText),
        htmlFile = htmlFile,
        selectElementId = 'vaccineSelect')

def updateHtmlFile4SymptomsCausedByCOVIDLots(symptoms, batches, htmlFile):
    symptomOptions = getSymptomOptions(symptoms)
    for selectElementId in ['symptomSelect', 'symptomSelectX', 'symptomSelectY']:
        _saveOptions(
            options = symptomOptions,
            htmlFile = htmlFile,
            selectElementId = selectElementId)

    _saveOptions(
        options = getVaccineOptions(batches, 'Select Batch'),
        htmlFile = htmlFile,
        selectElementId = 'vaccineSelect')

def _saveOptions(options, htmlFile, selectElementId):
    HtmlTransformerUtil().applySoupTransformerToFile(
        file=htmlFile,
        soupTransformer = lambda soup:
            BeautifulSoup(
                OptionsSetter().setOptions(
                    html = str(soup),
                    selectElementId = selectElementId,
                    options = options),
                'lxml'))

# FK-TODO: move saveLastUpdated2HtmlFile() to src/BatchCodeTableHtmlUpdater.py
def saveLastUpdated2HtmlFile(lastUpdated, htmlFile, lastUpdatedElementId):
    def setLastUpdated(soup):
        soup.find(id = lastUpdatedElementId).string.replace_with(
            lastUpdated.strftime(DateProvider.DATE_FORMAT))
        return soup

    HtmlTransformerUtil().applySoupTransformerToFile(
        file = htmlFile,
        soupTransformer = setLastUpdated)
