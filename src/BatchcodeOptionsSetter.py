from SymptomsCausedByVaccines.OptionsSetter import OptionsSetter


class BatchcodeOptionsSetter:

    def setBatchcodeOptions(self, html, options):
        return OptionsSetter().setOptions(html, 'batchCodeSelect', options)
