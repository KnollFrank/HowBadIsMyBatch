def getKreisOptions(kreisValues):
    return [getKreisOption(kreis) for kreis in kreisValues]

def getKreisOption(kreis):
    return f'<option value="{kreis}">{kreis}</option>'
