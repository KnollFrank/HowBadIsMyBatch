import html

def getVaccineOptions(vaccines, filenameByDrug, defaultOptionText):
    return getOptionsWithDefaultOption(
        defaultOptionText = defaultOptionText,
        values = vaccines,
        filenameByValue = filenameByDrug)


def getSymptomOptions(symptoms, filenameBySymptom):
    return getOptionsWithDefaultOption(
        defaultOptionText = 'Select Symptom',
        values = symptoms,
        filenameByValue = filenameBySymptom)


def getOptionsWithDefaultOption(defaultOptionText, values, filenameByValue):
    return ['<option hidden disabled selected value>{defaultOptionText}</option>'.format(defaultOptionText = defaultOptionText)] + _getOptions(values, filenameByValue)


def _getOptions(values, filenameByValue):
    return [_getOption(filename = filenameByValue[value], displayValue = value) for value in values]


def _getOption(filename, displayValue):
    return '<option value="{value}">{displayValue}</option>'.format(
        value = filename,
        displayValue = html.escape(str(displayValue)))
