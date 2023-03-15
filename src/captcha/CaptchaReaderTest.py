import unittest
from captcha.CaptchaReader import CaptchaReader
from captcha.CaptchaShape import CaptchaShape
import os

class CaptchaReaderTest(unittest.TestCase):

    def setUp(self):
        self.working_directory = os.path.dirname(__file__)

    def test_getTextInCaptchaImage(self):
        # Given
        textInCaptchaImage = '1Ad47a'
        captchaReader = CaptchaReader(
            modelFilepath = f'{self.working_directory}/MobileNetV3Small',
            captchaShape = CaptchaShape())

        # When
        textInCaptchaImageActual = captchaReader.getTextInCaptchaImage(f'{self.working_directory}/captchas/VAERS/{textInCaptchaImage}.jpeg')

        # Then
        self.assertEqual(textInCaptchaImageActual, textInCaptchaImage)
