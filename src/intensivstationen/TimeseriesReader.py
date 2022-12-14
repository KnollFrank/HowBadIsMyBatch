import pandas as pd
from urllib import request


def readTimeseries(download = False):
    timeSeriesFile = 'zeitreihe-tagesdaten.csv'
    if download:
        _downloadTimeseries(timeSeriesFile)

    timeseries = pd.read_csv(
        timeSeriesFile,
        low_memory = False,
        usecols = ['date', 'bundesland', 'gemeindeschluessel', 'betten_belegt', 'betten_frei'],
        parse_dates = ['date'],
        date_parser = lambda dateStr: pd.to_datetime(dateStr, format = "%Y-%m-%d"),
        dtype = {
            'gemeindeschluessel': 'string',
            'bundesland': 'string'
            })
    return timeseries.sort_values(by = 'date', ascending = True)

# download https://diviexchange.blob.core.windows.net/%24web/zeitreihe-tagesdaten.csv or https://www.intensivregister.de/#/aktuelle-lage/downloads
def _downloadTimeseries(timeSeriesFile):
    request.urlretrieve(
        'https://diviexchange.blob.core.windows.net/%24web/zeitreihe-tagesdaten.csv',
        timeSeriesFile)
