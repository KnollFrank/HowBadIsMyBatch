from bs4 import BeautifulSoup
from HtmlTransformerUtil import HtmlTransformerUtil
from BatchcodeOptionsSetter import BatchcodeOptionsSetter
from HtmlUtils import getBatchcodeOptions, getBatchcodes
from SymptomsCausedByVaccines.HtmlUpdater import saveLastUpdated2HtmlFile


def updateBatchCodeTableHtmlFile(batchCodeTable, batchCodeTableHtmlFile, lastUpdated):
    batchcodeOptions = getBatchcodeOptions(getBatchcodes(batchCodeTable.sort_values(by = 'Adverse Reaction Reports', ascending = False)))
    _saveBatchcodeOptions(batchcodeOptions, batchCodeTableHtmlFile)
    saveLastUpdated2HtmlFile(
        lastUpdated = lastUpdated,
        htmlFile = batchCodeTableHtmlFile,
        lastUpdatedElementId = 'last_updated')

def _saveBatchcodeOptions(batchcodeOptions, batchCodeTableHtmlFile):
    HtmlTransformerUtil().applySoupTransformerToFile(
        file=batchCodeTableHtmlFile,
        soupTransformer = lambda soup:
            BeautifulSoup(
                BatchcodeOptionsSetter().setBatchcodeOptions(
                    html=str(soup),
                    options=batchcodeOptions),
                'lxml'))
