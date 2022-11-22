from bs4 import BeautifulSoup

class HtmlTransformerUtil:
    
    def applySoupTransformerToFile(self, file, soupTransformer):
        self._writeSoup(soupTransformer(self._readSoup(file)), file)

    def _readSoup(self, file):
        with open(file) as fp:
            soup = BeautifulSoup(fp, 'lxml')
        return soup

    def _writeSoup(self, soup, file):
        with open(file, "w") as fp:
            fp.write(str(soup))    
