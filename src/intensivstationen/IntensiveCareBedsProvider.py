import pandas as pd


def getIntensiveCareBeds(timeSeries, kreis = None):
    if kreis is not None:
        return timeSeries[timeSeries['Kreis'] == kreis][['date', 'betten_belegt', 'betten_frei', 'Einwohnerzahl']]
    else:
        return timeSeries.groupby('date').agg(**{
                        'betten_belegt': pd.NamedAgg(column = 'betten_belegt', aggfunc = 'sum'),
                        'betten_frei':   pd.NamedAgg(column = 'betten_frei',   aggfunc = 'sum'),
                        'Einwohnerzahl': pd.NamedAgg(column = 'Einwohnerzahl', aggfunc = 'sum')
                    }).reset_index()