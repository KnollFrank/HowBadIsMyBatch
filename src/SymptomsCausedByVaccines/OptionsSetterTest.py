import unittest
from SymptomsCausedByVaccines.OptionsSetter import OptionsSetter
from TestHelper import TestHelper


class OptionsSetterTest(unittest.TestCase):

    def test_setOptions(self):
        # Given
        optionsSetter = OptionsSetter()

        # When
        htmlActual = optionsSetter.setOptions(
            html='''
            <html>
              <body>
                <p>Test<p/>
                <select id="vaccineSelect" name="vaccine">
                  <option value="old1">old1</option>
                </select>
              </body>
            </html>
            ''',
            selectElementId = 'vaccineSelect',
            options=[
                '<option value="6VAX-F">6VAX-F</option>',
                '<option value="ADEN">ADEN</option>'])

        # Then
        TestHelper.assertEqualHTML(
            htmlActual,
            '''
            <html>
              <body>
                <p>Test<p/>
                <select id="vaccineSelect" name="vaccine">
                  <option value="6VAX-F">6VAX-F</option>
                  <option value="ADEN">ADEN</option>
                </select>
              </body>
            </html>
            ''')
