import unittest
from BatchcodeOptionsSetter import BatchcodeOptionsSetter
from TestHelper import TestHelper

class BatchcodeOptionsSetterTest(unittest.TestCase):

    def test_setBatchcodeOptions(self):
        # Given
        batchcodeOptionsSetter = BatchcodeOptionsSetter()

        # When
        htmlActual = batchcodeOptionsSetter.setBatchcodeOptions(
            html='''
            <html>
              <body>
                <p>Test<p/>
                <select id="batchCodeSelect" name="batchCode">
                  <option value="old1">old1</option>
                  <option value="old2">old2</option>
                </select>
              </body>
            </html>
            ''',
            options=[
                '<option value="FE6208">FE6208</option>',
                '<option value="039K20A">039K20A</option>',
                '<option value="FF3318">FF3318</option>'])

        # Then
        TestHelper.assertEqualHTML(
            htmlActual,
            '''
            <html>
              <body>
                <p>Test<p/>
                <select id="batchCodeSelect" name="batchCode">
                  <option value="FE6208">FE6208</option>
                  <option value="039K20A">039K20A</option>
                  <option value="FF3318">FF3318</option>
                </select>
              </body>
            </html>
            ''')
