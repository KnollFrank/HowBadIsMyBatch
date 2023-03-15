import unittest
from CaptchaReader import getTextInCaptchaImage


class CaptchaReaderTest(unittest.TestCase):

    def test_getTextInCaptchaImage(self):
        # Given
        textInCaptchaImage = '1Ad47a'

        # When
        textInCaptchaImageActual = getTextInCaptchaImage(f'src/captchas/VAERS/{textInCaptchaImage}.jpeg')

        # Then
        self.assertEqual(textInCaptchaImageActual, textInCaptchaImage)
