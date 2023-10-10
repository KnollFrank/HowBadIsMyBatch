import unittest
from intensivstationen.KreisOptionsSetter import KreisOptionsSetter

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
        assertEqualHTML(
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

# FK-TODO: delegate to use TestHelper.assertEqualHTML()
# adapted from https://stackoverflow.com/questions/8006909/pretty-print-assertequal-for-html-strings
def assertEqualHTML(string1, string2, file1='', file2=''):
    u'''
    Compare two unicode strings containing HTML.
    A human friendly diff goes to logging.error() if they
    are not equal, and an exception gets raised.
    '''
    from bs4 import BeautifulSoup as bs
    import difflib

    def short(mystr):
        max = 20
        if len(mystr) > max:
            return mystr[:max]
        return mystr
    p = []
    for mystr, file in [(string1, file1), (string2, file2)]:
        if not isinstance(mystr, str):
            raise Exception(u'string ist not unicode: %r %s' %
                            (short(mystr), file))
        soup = bs(mystr)
        pretty = soup.prettify()
        p.append(pretty)
    if p[0] != p[1]:
        for line in difflib.unified_diff(p[0].splitlines(), p[1].splitlines(), fromfile=file1, tofile=file2):
            display(line)
        display(p[0], ' != ', p[1])
        raise Exception('Not equal %s %s' % (file1, file2))
