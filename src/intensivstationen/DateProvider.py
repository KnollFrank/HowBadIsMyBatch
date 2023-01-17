from bs4 import BeautifulSoup
import requests
from datetime import datetime
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import pandas as pd

class DateProvider:
    
    INTENSIVSTATIONEN_DATE_FORMAT = "%d.%m.%Y, %H:%M Uhr"

    def __init__(self):
        self.lastUpdated = None
        self.lastUpdatedDataSource = None

    def needsUpdate(self):
        return self.getLastUpdated() < self.getLastUpdatedDataSource()
        
    def getLastUpdated(self):
        if self.lastUpdated is None:
            htmlContent = requests.get("https://knollfrank.github.io/HowBadIsMyBatch/intensivstationen.html").text
            soup = BeautifulSoup(htmlContent, "lxml")
            dateStr = soup.find(id = "Datenstand").text
            self.lastUpdated = datetime.strptime(dateStr, DateProvider.INTENSIVSTATIONEN_DATE_FORMAT)
        
        return self.lastUpdated

    def getLastUpdatedDataSource(self):
        if self.lastUpdatedDataSource is None:
            html = self._getOriginalHtml()
            lastUpdatedColumn = 'Letzte Änderung'
            dataFrame = self._asDataFrame(html, lastUpdatedColumn)
            self.lastUpdatedDataSource = dataFrame.loc['Landkreis-Daten', lastUpdatedColumn].to_pydatetime()

        return self.lastUpdatedDataSource

    def _getOriginalHtml(self):
        options = Options()
        options.headless = True
        options.add_argument("-profile")
        driver = self._getWebDriver()
        driver.get('https://www.intensivregister.de/#/aktuelle-lage/downloads')
        sleep(10)
        innerHTML = driver.execute_script("return document.body.innerHTML")
        driver.quit()
        return innerHTML

    def _getWebDriver(self):
        return webdriver.Chrome(
            service = ChromeService(executable_path = ChromeDriverManager().install()),
            options = self._getOptions())

    def _getOptions(self):
        options = Options()
        options.headless = True
        return options

    def _asDataFrame(self, html, lastUpdatedColumn):
        dataFrame = pd.read_html(html, parse_dates = [lastUpdatedColumn])[0]
        dataFrame[lastUpdatedColumn] = pd.to_datetime(dataFrame[lastUpdatedColumn], format = "%d.%m.%Y %H:%M Uhr")
        dataFrame.set_index('Name', inplace = True)
        return dataFrame
