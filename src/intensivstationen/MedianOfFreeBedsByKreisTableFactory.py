import pandas as pd

class MedianOfFreeBedsByKreisTableFactory:
    
    def __init__(self, dataFrame):
        self.dataFrame = dataFrame

    def createMedianOfFreeBedsByKreisTable(self, kreisKey):
        self.dataFrame['free_beds_divided_by_all_beds_in_percent'] = self.dataFrame['betten_frei'] / (self.dataFrame['betten_frei'] + self.dataFrame['betten_belegt']) * 100
        aggregated = self.dataFrame.groupby(kreisKey).agg(
            median_free_beds_in_percent =
                pd.NamedAgg(
                    column = 'free_beds_divided_by_all_beds_in_percent',
                    aggfunc = 'median'))
        return aggregated.sort_values(by = 'median_free_beds_in_percent', ascending = False)