from bs4 import BeautifulSoup
from HtmlTransformerUtil import HtmlTransformerUtil
from DateProvider import DateProvider
from DateProvider import DateProvider


def updateBatchCodeTableHtmlFile(batchCodeTableHtmlFile):
    _saveLastUpdatedBatchCodeTable(
        DateProvider().getLastUpdatedDataSource(),
        batchCodeTableHtmlFile)

def _saveLastUpdatedBatchCodeTable(lastUpdated, batchCodeTableHtmlFile):
    def setLastUpdated(soup):
        soup.find(id="last_updated").string.replace_with(
            lastUpdated.strftime(DateProvider.DATE_FORMAT))
        return soup

    HtmlTransformerUtil().applySoupTransformerToFile(
        file=batchCodeTableHtmlFile,
        soupTransformer=setLastUpdated)
