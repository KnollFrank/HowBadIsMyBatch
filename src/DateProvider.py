from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime


class DateProvider:

    DATE_FORMAT = "%B %d, %Y"

    def __init__(self):
        self.lastUpdated = None
        self.lastUpdatedDataSource = None

    def needsUpdate(self):
        return self.getLastUpdated() < self.getLastUpdatedDataSource()

    def getLastUpdated(self):
        if self.lastUpdated is None:
            self.lastUpdated = self.__getLastUpdated(
                url="https://knollfrank.github.io/HowBadIsMyBatch/HowBadIsMyBatch.html",
                getDateStr=lambda soup: soup.find(id="last_updated").text)

        return self.lastUpdated

    def getLastUpdatedDataSource(self):
        if self.lastUpdatedDataSource is None:
            def getDateStr(soup):
                lastUpdated = soup.find(string=re.compile("Last updated"))
                return re.search('Last updated: (.+).', lastUpdated).group(1)

            self.lastUpdatedDataSource = self.__getLastUpdated(
                url="https://vaers.hhs.gov/data/datasets.html",
                getDateStr=getDateStr)

        return self.lastUpdatedDataSource

    def __getLastUpdated(self, url, getDateStr):
        htmlContent = requests.get(url).text
        soup = BeautifulSoup(htmlContent, "lxml")
        dateStr = getDateStr(soup)
        return datetime.strptime(dateStr, DateProvider.DATE_FORMAT)
