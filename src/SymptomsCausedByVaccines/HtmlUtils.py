def getVaccineOptions(vaccines):
    return _getOptionsWithDefaultOption(defaultOptionText = 'Select Vaccine', values = vaccines)


def getSymptomOptions(symptoms):
    return _getOptionsWithDefaultOption(defaultOptionText = 'Select Symptom', values = symptoms)


def _getOptionsWithDefaultOption(defaultOptionText, values):
    return ['<option hidden disabled selected value>{defaultOptionText}</option>'.format(defaultOptionText = defaultOptionText)] + _getOptions(values)


def _getOptions(values):
    return [_getOption(value) for value in values]


def _getOption(value):
    return '<option value="{value}">{value}</option>'.format(value=value)
