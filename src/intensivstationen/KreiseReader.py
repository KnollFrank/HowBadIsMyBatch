import pandas as pd
from urllib import request

def readKreise(download = False):
    kreiseFile = '04-kreise.xlsx'
    if download:
        _downloadKreise(kreiseFile)
    
    kreise = pd.read_excel(
        kreiseFile,
        sheet_name = 'Kreisfreie Städte u. Landkreise',
        header = 5,
        index_col = 0)
    kreise = kreise.rename(columns = {'2': 'Bundesland', 3: 'Kreis', 6: 'Einwohnerzahl'})[['Bundesland', 'Kreis', 'Einwohnerzahl']]
    kreise.index.set_names("Key", inplace = True)
    return kreise

# download https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Administrativ/04-kreise.xlsx?__blob=publicationFile or https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Administrativ/04-kreise.html
def _downloadKreise(kreiseFile):
    request.urlretrieve(
        'https://www.destatis.de/DE/Themen/Laender-Regionen/Regionales/Gemeindeverzeichnis/Administrativ/04-kreise.xlsx?__blob=publicationFile',
        kreiseFile)
