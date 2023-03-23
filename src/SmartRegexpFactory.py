import re


# adapted from function _fnFilterCreateSearch() defined in https://github.com/DataTables/DataTablesSrc/blob/master/js/core/core.filter.js
class SmartRegexpFactory:

    def createSmartRegexp(self, searchTerm):
        return re.compile(
            rf'^{self.assertContainsWords(self.getWords(searchTerm))}.*$',
            flags=re.IGNORECASE)

    def getWords(self, searchTerm):
        return re.split(r'\s+', searchTerm)

    def assertContainsWords(self, words):
        return ''.join([self.assertContainsWord(word) for word in words])

    def assertContainsWord(self, word):
        return f'(?=.*?{word})'
