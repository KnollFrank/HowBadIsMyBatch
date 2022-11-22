from bs4 import BeautifulSoup
from HtmlTransformerUtil import HtmlTransformerUtil
from CountryOptionsSetter import CountryOptionsSetter
from DateProvider import DateProvider
from HtmlUtils import getCountryOptions, getCountries
from DateProvider import DateProvider
from BatchCodeTablePersister import createAndSaveBatchCodeTables


def updateBatchCodeTableHtmlFile(internationalVaersCovid19):
    countryOptions = getCountryOptions(getCountries(internationalVaersCovid19))
    saveCountryOptions(countryOptions)
    saveLastUpdatedBatchCodeTable(DateProvider().getLastUpdatedDataSource())
    createAndSaveBatchCodeTables(internationalVaersCovid19, minADRsForLethality=100)


def saveCountryOptions(countryOptions):
    HtmlTransformerUtil().applySoupTransformerToFile(
        file = "../docs/batchCodeTable.html",
        soupTransformer =
            lambda soup:
                BeautifulSoup(
                    CountryOptionsSetter().setCountryOptions(html = str(soup), options = countryOptions),
                    'lxml'))


def saveLastUpdatedBatchCodeTable(lastUpdated):
    def setLastUpdated(soup):
        soup.find(id = "last_updated").string.replace_with(lastUpdated.strftime(DateProvider.DATE_FORMAT))
        return soup

    HtmlTransformerUtil().applySoupTransformerToFile(
        file = "../docs/batchCodeTable.html",
        soupTransformer = setLastUpdated)
    