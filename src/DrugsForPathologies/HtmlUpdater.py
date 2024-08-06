from bs4 import BeautifulSoup
from HtmlTransformerUtil import HtmlTransformerUtil
from DateProvider import DateProvider
from SymptomsCausedByVaccines.HtmlUtils import getOptionsWithDefaultOption
from SymptomsCausedByVaccines.OptionsSetter import OptionsSetter


def updateHtmlFile(filenameByPathology, htmlFile):
    options = getOptionsWithDefaultOption(
        defaultOptionText = 'Select Pathology',
        values = list(filenameByPathology.keys()),
        filenameByValue = filenameByPathology)
    _saveOptions(
        options = options,
        htmlFile = htmlFile,
        selectElementId = 'pathologySelect')


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
