class SevereColumnAdder:
    
    @staticmethod
    def addSevereColumn(dataFrame):
        dataFrame['SEVERE'] = (dataFrame['DIED'] + dataFrame['L_THREAT'] + dataFrame['DISABLE']) > 0
        dataFrame['SEVERE'].replace({True: 1, False: 0}, inplace = True)
        return dataFrame
