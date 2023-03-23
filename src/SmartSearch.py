import re
from SmartRegexpFactory import SmartRegexpFactory


class SmartSearch:

    def __init__(self, searchTerm):
        self.smartRegexp = SmartRegexpFactory().createSmartRegexp(searchTerm)

    def matches(self, str):
        return True if self.smartRegexp.match(str) else False
