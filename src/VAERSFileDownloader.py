import os
import time
from WebDriver import getWebDriver, isCaptchaSolved, saveCaptchaImageAs
from selenium.webdriver.common.by import By
from captcha.CaptchaReader import CaptchaReader
from zipUtils import unzipAndRemove
from captcha.CaptchaShape import CaptchaShape


#def getTextInCaptchaImage(captchaImageFile):
#    baseDir = "~/AndroidStudioProjects/TextRecognizer"
#    ! cp $captchaImageFile $baseDir/app/src/main/assets/captchas/captcha_image.jpeg
#    ! cd $baseDir;./gradlew connectedAndroidTest
#    textInCaptchaImage = ! adb shell "run-as org.textrecognizer cat /data/data/org.textrecognizer/files/captcha_image.txt"
#    return textInCaptchaImage[0]
    
def updateVAERSFiles(years, workingDirectory):
    for year in years:
        _downloadVAERSFileAndUnzip(f'{year}VAERSData.zip', workingDirectory)
    _downloadVAERSFileAndUnzip('NonDomesticVAERSData.zip', workingDirectory)
    
def _downloadVAERSFileAndUnzip(file, workingDirectory):
    downloadedFile = _downloadVAERSFile(file, workingDirectory + "/VAERS/tmp")
    unzipAndRemove(
        zipFile = downloadedFile,
        dstDir = workingDirectory + '/VAERS/')

def _downloadVAERSFile(file, downloadDir):
    driver = getWebDriver(downloadDir, isHeadless = True)
    downloadedFile = _downloadFile(
        absoluteFile = downloadDir + "/" + file,
        driver = driver,
        maxTries = None)
    driver.quit()
    return downloadedFile

def _downloadFile(absoluteFile, driver, maxTries):
    captchaReader = _createCaptchaReader()
    def downloadFile():
        driver.get('https://vaers.hhs.gov/eSubDownload/index.jsp?fn=' + os.path.basename(absoluteFile))
        _solveCaptchaAndStartFileDownload(driver, captchaReader, 'captchaImage.jpeg')

    numTries = 1
    downloadFile()
    while(not isCaptchaSolved(driver) and (maxTries is None or numTries < maxTries)):
        downloadFile()
        numTries = numTries + 1

    if isCaptchaSolved(driver):
        _waitUntilDownloadHasFinished(absoluteFile)
        return absoluteFile
    else:
        return None

def _createCaptchaReader():
    working_directory = os.path.dirname(__file__)
    return CaptchaReader(modelFilepath = f'{working_directory}/captcha/MobileNetV3Small',
                         captchaShape = CaptchaShape())

def _solveCaptchaAndStartFileDownload(driver, captchaReader, captchaImageFile):
    saveCaptchaImageAs(driver, captchaImageFile)
    textInCaptchaImage = captchaReader.getTextInCaptchaImage(captchaImageFile)
    print('textInCaptchaImage:', textInCaptchaImage)
    driver.find_element(By.ID, "verificationCode").send_keys(textInCaptchaImage)
    driver.find_element(By.CSS_SELECTOR, '[name="downloadbut"]').click()

def _waitUntilDownloadHasFinished(file):
    while not os.path.exists(file):
        time.sleep(2)