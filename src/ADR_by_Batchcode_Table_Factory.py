from BatchCodeTableFactory import BatchCodeTableFactory

def create_ADR_by_Batchcode_Table_4USA(internationalVaersCovid19):
    batchCodeTable4USA = BatchCodeTableFactory(internationalVaersCovid19).createBatchCodeTableByCountry('United States')
    return batchCodeTable4USA[['Adverse Reaction Reports']]
