import pandas as pd

class ColumnsAdder:

    def __init__(self, kreise):
        self.kreise = kreise

    def addKreisAndBundeslandAndEinwohnerzahlColumns(self, dataFrame):
        dataFrame = self.addKreisAndEinwohnerzahlColumns(dataFrame)
        return self._addBundeslandColumn(dataFrame)
        
    def addKreisAndEinwohnerzahlColumns(self, dataFrame):
        dataFrame_kreise = pd.merge(dataFrame, self.kreise, how = 'left', left_on = 'gemeindeschluessel', right_index = True)
        dataFrame['Kreis'] = dataFrame_kreise['Kreis']
        dataFrame['Einwohnerzahl'] = dataFrame_kreise['Einwohnerzahl']
        return dataFrame

    def _addBundeslandColumn(self, dataFrame):
        return pd.merge(
            dataFrame,
            self._createBundeslandByKeyTable(),
            how = 'left',
            left_on = 'bundesland',
            right_index = True)

    def _createBundeslandByKeyTable(self):
        return self.kreise[self.kreise.index.str.len() == 2][['Bundesland']]
