def getVaccineOptions(vaccines):
    return ['<option hidden disabled selected value>Select Vaccine</option>'] + _getOptions(vaccines)


def getSymptomOptions(symptoms):
    return ['<option hidden disabled selected value>Select Symptom</option>'] + _getOptions(symptoms)


def _getOptions(values):
    return [_getOption(value) for value in values]


def _getOption(value):
    return '<option value="{value}">{value}</option>'.format(value=value)
