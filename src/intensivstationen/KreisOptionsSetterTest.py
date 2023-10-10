import unittest
from intensivstationen.KreisOptionsSetter import KreisOptionsSetter
from TestHelper import TestHelper


class KreisOptionsSetterTest(unittest.TestCase):

    def test_setKreisOptions(self):
        # Given
        kreisOptionsSetter = KreisOptionsSetter()

        # When
        htmlActual = kreisOptionsSetter.setKreisOptions(
            html='''
            <html>
              <body>
                <p>Test<p/>
                <select id="kreisSelect" name="kreis">
                  <option selected="" value="de">Alle Landkreise</option>
                  <option value="Ahrweiler">Ahrweiler</option>
                  <option value="Wiesbaden, Landeshauptstadt">Wiesbaden, Landeshauptstadt</option>
                  <option value="Aichach-Friedberg">Aichach-Friedberg</option>
                </select>
              </body>
            </html>
            ''',
            options=[
                '<option selected="" value="de">Alle Landkreise</option>',
                '<option value="Ahrweiler">Ahrweiler</option>',
                '<option value="Aichach-Friedberg">Aichach-Friedberg</option>'])

        # Then
        TestHelper.assertEqualHTML(
            htmlActual,
            '''
            <html>
              <body>
                <p>Test<p/>
                <select id="kreisSelect" name="kreis">
                  <option selected="" value="de">Alle Landkreise</option>
                  <option value="Ahrweiler">Ahrweiler</option>
                  <option value="Aichach-Friedberg">Aichach-Friedberg</option>
                </select>
              </body>
            </html>
            ''')
