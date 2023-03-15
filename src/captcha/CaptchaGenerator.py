from PIL import Image, ImageDraw, ImageFont
import random
import string
import shutil


class CaptchaGenerator:

    characters = sorted(set(list(string.ascii_letters + string.digits)))
    captchaLength = 6

    def __init__(self, numCaptchas, dataDir):
        self.numCaptchas = numCaptchas
        self.dataDir = dataDir

    def createAndSaveCaptchas(self):
        self._prepareDataDir()
        for _ in range(self.numCaptchas):
            self._createAndSaveCaptcha()

    def _prepareDataDir(self):
        shutil.rmtree(self.dataDir, ignore_errors = True)
        self.dataDir.mkdir(parents=True, exist_ok=True)

    def _createAndSaveCaptcha(self):
        captchaString = self._createCaptchaString()
        captcha = self._createCaptcha(captchaString)
        captcha.save(f"{str(self.dataDir)}/{captchaString}.jpeg")

    def _createCaptchaString(self):
        return ''.join(random.choice(CaptchaGenerator.characters) for _ in range(CaptchaGenerator.captchaLength))

    def _createCaptcha(self, word):
        image = Image.new("RGB", (360, 96), "#373737")
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("ariali.ttf", size=40)
        draw.text((30, 10), word[0], font=font)
        draw.text((80, 30), word[1], font=font)
        draw.text((135, 10), word[2], font=font)
        draw.text((190, 30), word[3], font=font)
        draw.text((250, 10), word[4], font=font)
        draw.text((295, 30), word[5], font=font)
        return image
