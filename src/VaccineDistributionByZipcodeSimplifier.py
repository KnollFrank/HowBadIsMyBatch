import pandas as pd

class VaccineDistributionByZipcodeSimplifier:

    @staticmethod
    def sumDoses(vaccineDistributionByZipcode):
        return (vaccineDistributionByZipcode
                .groupby(['PROVIDER_NAME', 'ZIPCODE_SHP', 'LOT_NUMBER'])
                .agg(DOSES_SHIPPED = pd.NamedAgg(column = 'DOSES_SHIPPED', aggfunc = 'sum'))
                .reset_index())
