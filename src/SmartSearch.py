import re


class SmartSearch:

    def __init__(self, searchTerm):
        self.regexp = _SmartRegexpFactory().createSmartRegexp(searchTerm)

    def matches(self, str):
        return True if re.match(self.regexp, str, flags=re.IGNORECASE) else False


class _SmartRegexpFactory:

    def createSmartRegexp(self, searchTerm):
        return rf'^{self.assertContainsWords(self.getWords(searchTerm))}.*$'

    def getWords(self, searchTerm):
        return re.split(r'\s+', searchTerm)

    def assertContainsWords(self, words):
        return ''.join([self.assertContainsWord(word) for word in words])

    def assertContainsWord(self, word):
        return f'(?=.*?{word})'
