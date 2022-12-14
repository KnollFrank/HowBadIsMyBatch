from bs4 import BeautifulSoup
import requests
from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
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
        # put the root directory your default profile path here, you can check it by opening Firefox and then pasting 'about:profiles' into the url field 
        options.add_argument("/home/frankknoll/snap/firefox/common/.mozilla/firefox/1j6r2yp6.default")
        driver = webdriver.Firefox(options = options)
        driver.get('https://www.intensivregister.de/#/aktuelle-lage/downloads')
        sleep(10)
        innerHTML = driver.execute_script("return document.body.innerHTML")
        driver.quit()
        return innerHTML

    def _asDataFrame(self, html, lastUpdatedColumn):
        dataFrame = pd.read_html(html, parse_dates = [lastUpdatedColumn])[0]
        dataFrame[lastUpdatedColumn] = pd.to_datetime(dataFrame[lastUpdatedColumn], format = "%d.%m.%Y %H:%M Uhr")
        dataFrame.set_index('Name', inplace = True)
        return dataFrame
