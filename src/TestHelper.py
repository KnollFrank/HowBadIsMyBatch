import pandas as pd


class TestHelper:

    @staticmethod
    def createDataFrame(columns, data, dtypes={}, **kwargs):
        return pd.DataFrame(columns=columns, data=data, **kwargs).astype(dtypes)

    @staticmethod
    def createSeries(indexName, **kwargs):
        series = pd.Series(**kwargs)
        series.index.name = indexName
        return series

    # adapted from https://stackoverflow.com/questions/8006909/pretty-print-assertequal-for-html-strings
    @staticmethod
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
            soup = bs(mystr, 'lxml')
            pretty = soup.prettify()
            p.append(pretty)
        if p[0] != p[1]:
            for line in difflib.unified_diff(p[0].splitlines(), p[1].splitlines(), fromfile=file1, tofile=file2):
                print(line)
            print(p[0], ' != ', p[1])
            raise Exception('Not equal %s %s' % (file1, file2))
