import pandas as pd
from DataFrameNormalizer import DataFrameNormalizer


class VaersDescrReader:
    
    def __init__(self, dataDir):
        self.dataDir = dataDir

    def readVaersDescrsForYears(self, years):
        return [self.readVaersDescrForYear(year) for year in years]

    def readVaersDescrForYear(self, year):
        return {
                    'VAERSDATA': self._readVAERSDATA('{dataDir}/{year}VAERSDATA.csv'.format(dataDir = self.dataDir, year = year)),
                    'VAERSVAX': self._readVAERSVAX('{dataDir}/{year}VAERSVAX.csv'.format(dataDir = self.dataDir, year = year)),
                    'VAERSSYMPTOMS': self._readVAERSSYMPTOMS('{dataDir}/{year}VAERSSYMPTOMS.csv'.format(dataDir = self.dataDir, year = year))
               }

    def readNonDomesticVaersDescr(self):
        return {
                    'VAERSDATA': self._readVAERSDATA(self.dataDir + '/NonDomesticVAERSDATA.csv'),
                    'VAERSVAX': self._readVAERSVAX(self.dataDir + '/NonDomesticVAERSVAX.csv'),
                    'VAERSSYMPTOMS': self._readVAERSSYMPTOMS(self.dataDir + '/NonDomesticVAERSSYMPTOMS.csv')
               }

    def _readVAERSDATA(self, file):
        VAERSDATA = self._read_csv(
            file = file,
            usecols = ['VAERS_ID', 'RECVDATE', 'DIED', 'L_THREAT', 'DISABLE', 'HOSPITAL', 'ER_VISIT', 'VAX_DATE', 'SPLTTYPE'],
            parse_dates = ['RECVDATE', 'VAX_DATE'],
            date_parser = lambda dateStr: pd.to_datetime(dateStr, format = '%m/%d/%Y'))
        DataFrameNormalizer._convertColumnsOfDataFrame_Y_to_1_else_0(
            VAERSDATA,
            ['DIED', 'L_THREAT', 'DISABLE', 'HOSPITAL', 'ER_VISIT'])
        return VAERSDATA

    def _readVAERSVAX(self, file):
        VAERSVAX = self._read_csv(
            file = file,
            usecols = ['VAERS_ID', 'VAX_DOSE_SERIES', 'VAX_TYPE', 'VAX_MANU', 'VAX_LOT'],
            dtype =
                {
                    'VAX_DOSE_SERIES': 'string',
                    'VAX_LOT': 'string'
                })
        DataFrameNormalizer.removeUnknownBatchCodes(VAERSVAX)
        DataFrameNormalizer.convertVAX_LOTColumnToUpperCase(VAERSVAX)
        return VAERSVAX


    def _readVAERSSYMPTOMS(self, file):
        return self._read_csv(
            file = file,
            usecols = ['VAERS_ID', 'SYMPTOM1', 'SYMPTOM2', 'SYMPTOM3', 'SYMPTOM4', 'SYMPTOM5'])

    def _read_csv(self, file, **kwargs):
        return pd.read_csv(
            file,
            index_col = 'VAERS_ID',
            encoding = 'latin1',
            low_memory = False,
            **kwargs)
