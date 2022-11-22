import os
import time
from WebDriver import getWebDriver, isCaptchaSolved, saveCaptchaImageAs
from selenium.webdriver.common.by import By
from CaptchaReader import getTextInCaptchaImage

#def getTextInCaptchaImage(captchaImageFile):
#    baseDir = "~/AndroidStudioProjects/TextRecognizer"
#    ! cp $captchaImageFile $baseDir/app/src/main/assets/captchas/captcha_image.jpeg
#    ! cd $baseDir;./gradlew connectedAndroidTest
#    textInCaptchaImage = ! adb shell "run-as org.textrecognizer cat /data/data/org.textrecognizer/files/captcha_image.txt"
#    return textInCaptchaImage[0]
    
def solveCaptchaAndStartFileDownload(driver, captchaImageFile):
    saveCaptchaImageAs(driver, captchaImageFile)
    textInCaptchaImage = getTextInCaptchaImage(captchaImageFile)
    display('textInCaptchaImage: ', textInCaptchaImage)
    driver.find_element(By.ID, "verificationCode").send_keys(textInCaptchaImage)
    driver.find_element(By.CSS_SELECTOR, '[name="downloadbut"]').click()

def downloadFile(absoluteFile, driver, maxTries):
    def _downloadFile():
        driver.get('https://vaers.hhs.gov/eSubDownload/index.jsp?fn=' + os.path.basename(absoluteFile))
        solveCaptchaAndStartFileDownload(driver, 'captchaImage.jpeg')

    numTries = 1
    _downloadFile()
    while(not isCaptchaSolved(driver) and (maxTries is None or numTries < maxTries)):
        _downloadFile()
        numTries = numTries + 1

    if isCaptchaSolved(driver):
        _waitUntilDownloadHasFinished(absoluteFile)
        return absoluteFile
    else:
        return None

def _waitUntilDownloadHasFinished(file):
    while not os.path.exists(file):
        time.sleep(2)

def downloadVAERSFile(file, downloadDir):
    driver = getWebDriver(downloadDir, isHeadless = True)
    downloadedFile = downloadFile(
        absoluteFile = downloadDir + "/" + file,
        driver = driver,
        maxTries = None)
    driver.quit()
    return downloadedFile
