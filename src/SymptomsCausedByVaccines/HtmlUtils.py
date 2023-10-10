def getVaccineOptions(vaccines):
    return ['<option hidden disabled selected value>Select Vaccine</option>'] + _getVaccineOptions(vaccines)


def _getVaccineOptions(vaccines):
    return [_getVaccineOption(vaccine) for vaccine in vaccines]


def _getVaccineOption(vaccine):
    return '<option value="{vaccine}">{vaccine}</option>'.format(vaccine=vaccine)
