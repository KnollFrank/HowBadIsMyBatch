def getKreisOptionsAndAlleLandkreise(kreisValues):
    return ['<option selected="" value="de">Alle Landkreise</option>']  + getKreisOptions(kreisValues)

def getKreisOptions(kreisValues):
    return [getKreisOption(kreis) for kreis in kreisValues]

def getKreisOption(kreis):
    return f'<option value="{kreis}">{kreis}</option>'
