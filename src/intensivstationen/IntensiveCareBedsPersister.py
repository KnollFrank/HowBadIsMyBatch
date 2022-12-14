from IntensiveCareBedsProvider import getIntensiveCareBeds
from IOUtils import IOUtils

def getAndPersistIntensiveCareBeds4AlleKreise(timeSeries, intensivstationenDataDir, kreisValues):
    getAndPersistIntensiveCareBeds(timeSeries, intensivstationenDataDir)
    for kreis in kreisValues:
        getAndPersistIntensiveCareBeds(
            timeSeries,
            intensivstationenDataDir = intensivstationenDataDir,
            kreis = kreis)

def getAndPersistIntensiveCareBeds(timeSeries, intensivstationenDataDir, kreis = None):
    intensiveCareBeds = getIntensiveCareBeds(timeSeries, kreis)
    display(kreis)
    _saveAsJson(intensiveCareBeds, _getFilename(intensivstationenDataDir, kreis))


def _saveAsJson(intensiveCareBeds, file):
    IOUtils.saveDictAsJson(
        {
            'population': int(intensiveCareBeds.iloc[0]['Einwohnerzahl']),
            'data': _intensiveCareBeds2Dict(intensiveCareBeds),
        },
        file)


def _intensiveCareBeds2Dict(intensiveCareBeds):
    df = intensiveCareBeds[['date', 'betten_belegt', 'betten_frei']].copy()
    df['date'] = df['date'].dt.strftime('%Y-%m-%d')
    return df.to_dict(orient = "records")


def _getFilename(intensivstationenDataDir, kreis):
    return f'{intensivstationenDataDir}/intensivstationen-{_getSuffix(kreis)}.json'


def _getSuffix(kreis):
    return kreis if kreis is not None else 'de'
