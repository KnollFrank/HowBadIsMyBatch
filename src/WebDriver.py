from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def _getOptions(downloadDir, isHeadless):
    options = Options()
    if isHeadless:
        options.add_argument('--headless=new')
    options.add_experimental_option("prefs", {"download.default_directory" : downloadDir})
    return options

def getWebDriver(downloadDir, isHeadless):
    return webdriver.Chrome(
        service = ChromeService(executable_path = ChromeDriverManager().install()),
        options = _getOptions(downloadDir, isHeadless))

def saveCaptchaImageAs(driver, captchaImageFile):
    captchaImage = driver.find_element(By.CSS_SELECTOR, "img[src='captchaImage']")
    with open(captchaImageFile, 'wb') as file:
        file.write(captchaImage.screenshot_as_png)

def existsElementWithId(driver, id):
    return len(driver.find_elements(By.ID, id)) > 0

def isCaptchaSolved(driver):
    return not existsElementWithId(driver, "wordverify")
