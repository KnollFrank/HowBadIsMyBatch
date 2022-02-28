const kreisValues =
    ['Flensburg', 'Bamberg', 'Hof', 'Coburg', 'Bayreuth', 'Schwandorf',
        'Regensburg', 'Neumarkt i.d.OPf.', 'Cham', 'Amberg-Sulzbach',
        'Amberg', 'Dingolfing-Landau', 'Straubing-Bogen', 'Rottal-Inn',
        'Regen', 'Passau', 'Landshut', 'Kelheim', 'Weiden i.d.OPf.',
        'Forchheim', 'Kronach', 'Kitzingen', 'Haßberge', 'Rhön-Grabfeld',
        'Bad Kissingen', 'Aschaffenburg', 'Würzburg', 'Schweinfurt',
        'Weißenburg-Gunzenhausen', 'Roth',
        'Neustadt a.d.Aisch-Bad Windsheim', 'Nürnberger Land',
        'Erlangen-Höchstadt', 'Ansbach', 'Nürnberg', 'Fürth', 'Erlangen',
        'Wunsiedel i.Fichtelgebirge', 'Lichtenfels', 'Kulmbach',
        'Freyung-Grafenau', 'Miltenberg', 'Deggendorf', 'Bodenseekreis',
        'Biberach', 'Alb-Donau-Kreis', 'Ulm', 'Zollernalbkreis',
        'Tübingen', 'Reutlingen', 'Waldshut', 'Lörrach', 'Ravensburg',
        'Konstanz', 'Schwarzwald-Baar-Kreis', 'Rottweil', 'Ortenaukreis',
        'Emmendingen', 'Breisgau-Hochschwarzwald', 'Freiburg im Breisgau',
        'Freudenstadt', 'Enzkreis', 'Calw', 'Tuttlingen', 'Sigmaringen',
        'Ingolstadt', 'München', 'Weilheim-Schongau', 'Traunstein',
        'Starnberg', 'Rosenheim', 'Pfaffenhofen a.d.Ilm',
        'Neuburg-Schrobenhausen', 'Mühldorf a.Inn', 'Miesbach',
        'Landsberg am Lech', 'Garmisch-Partenkirchen', 'Fürstenfeldbruck',
        'Freising', 'Erding', 'Eichstätt', 'Dachau',
        'Bad Tölz-Wolfratshausen', 'Berchtesgadener Land', 'Altötting',
        'Straubing', 'Augsburg', 'Saalekreis', 'Mansfeld-Südharz',
        'Jerichower Land', 'Harz', 'Burgenlandkreis', 'Börde',
        'Anhalt-Bitterfeld', 'Altmarkkreis Salzwedel', 'Magdeburg',
        'Salzlandkreis', 'Halle (Saale)', 'Nordsachsen', 'Leipzig',
        'Sächsische Schweiz-Osterzgebirge', 'Meißen', 'Görlitz', 'Bautzen',
        'Dresden', 'Zwickau', 'Dessau-Roßlau', 'Stendal', 'Wittenberg',
        'Erfurt', 'Altenburger Land', 'Greiz', 'Saale-Orla-Kreis',
        'Saale-Holzland-Kreis', 'Saalfeld-Rudolstadt', 'Sonneberg',
        'Weimarer Land', 'Ilm-Kreis', 'Hildburghausen', 'Sömmerda',
        'Gotha', 'Schmalkalden-Meiningen', 'Kyffhäuserkreis',
        'Unstrut-Hainich-Kreis', 'Wartburgkreis', 'Nordhausen',
        'Eichsfeld', 'Weimar', 'Suhl', 'Jena', 'Gera', 'Vogtlandkreis',
        'Mittelsachsen', 'Erzgebirgskreis', 'Chemnitz',
        'Brandenburg an der Havel', 'Berlin', 'St. Wendel',
        'Saarpfalz-Kreis', 'Saarlouis', 'Neunkirchen', 'Merzig-Wadern',
        'Saarbrücken, Regionalverband', 'Oberallgäu', 'Donau-Ries',
        'Unterallgäu', 'Ostallgäu', 'Lindau (Bodensee)', 'Neu-Ulm',
        'Günzburg', 'Dillingen a.d.Donau', 'Aichach-Friedberg',
        'Memmingen', 'Kempten (Allgäu)', 'Kaufbeuren', 'Cottbus',
        'Pforzheim', 'Frankfurt (Oder)', 'Barnim',
        'Landkreis Ludwigslust-Parchim', 'Vorpommern-Greifswald',
        'Landkreis Nordwestmecklenburg', 'Vorpommern-Rügen',
        'Landkreis Rostock', 'Mecklenburgische Seenplatte', 'Schwerink',
        'Rostock, Hanse- und Universitätsstadt', 'Uckermark',
        'Teltow-Fläming', 'Spree-Neiße', 'Prignitz', 'Potsdam-Mittelmark',
        'Ostprignitz-Ruppin', 'Oder-Spree', 'Oberspreewald-Lausitz',
        'Oberhavel', 'Märkisch-Oderland', 'Havelland', 'Elbe-Elster',
        'Dahme-Spreewald', 'Potsdam', 'Rhein-Neckar-Kreis',
        'Main-Spessart', 'Mannheim', 'Remscheid', 'Oberhausen',
        'Mülheim an der Ruhr', 'Mönchengladbach', 'Krefeld', 'Essen',
        'Duisburg', 'Düsseldorf', 'Bremerhaven', 'Solingen', 'Bremen',
        'Wesermarsch', 'Vechta', 'Osnabrück', 'Oldenburg', 'Leer',
        'Grafschaft Bentheim', 'Friesland', 'Emsland', 'Cloppenburg',
        'Wittmund', 'Wuppertal', 'Kleve', 'Mettmann', 'Steinfurt',
        'Recklinghausen', 'Coesfeld', 'Borken', 'Münster', 'Gelsenkirchen',
        'Bottrop', 'Rhein-Sieg-Kreis', 'Rheinisch-Bergischer Kreis',
        'Oberbergischer Kreis', 'Heinsberg', 'Euskirchen',
        'Rhein-Erft-Kreis', 'Düren',
        'Städteregion Aachen (einschl. Stadt Aachen)', 'Leverkusen',
        'Köln', 'Bonn', 'Wesel', 'Viersen', 'Rhein-Kreis Neuss', 'Aurich',
        'Ammerland', 'Wilhelmshaven', 'Helmstedt', 'Goslar', 'Gifhorn',
        'Wolfsburg', 'Salzgitter', 'Braunschweig', 'Hamburg', 'Stormarn',
        'Steinburg', 'Segeberg', 'Schleswig-Flensburg',
        'Rendsburg-Eckernförde', 'Plön', 'Pinneberg', 'Ostholstein',
        'Nordfriesland', 'Herzogtum Lauenburg', 'Dithmarschen',
        'Neumünster', 'Lübeck', 'Neckar-Odenwald-Kreis', 'Northeim',
        'Warendorf', 'Peine', 'Göttingen', 'Oldenburg (Oldenburg)',
        'Emden', 'Delmenhorst', 'Verden', 'Uelzen', 'Stade', 'Heidekreis',
        'Rotenburg (Wümme)', 'Osterholz', 'Lüneburg', 'Lüchow-Dannenberg',
        'Harburg', 'Cuxhaven', 'Celle', 'Schaumburg', 'Nienburg (Weser)',
        'Holzminden', 'Hildesheim', 'Hameln-Pyrmont', 'Diepholz',
        'Region Hannover', 'Wolfenbüttel', 'Bielefeld', 'Kiel',
        'Heidelberg', 'Alzey-Worms', 'Zweibrücken', 'Worms', 'Speyer',
        'Pirmasens', 'Neustadt an der Weinstraße', 'Mainz',
        'Ludwigshafen am Rhein', 'Landau in der Pfalz', 'Donnersbergkreis',
        'Kaiserslautern', 'Trier-Saarburg', 'Vulkaneifel',
        'Eifelkreis Bitburg-Prüm', 'Bernkastel-Wittlich', 'Trier',
        'Westerwaldkreis', 'Rhein-Lahn-Kreis', 'Rhein-Hunsrück-Kreis',
        'Neuwied', 'Frankenthal (Pfalz)', 'Germersheim', 'Kusel',
        'Gütersloh', 'Rastatt', 'Karlsruhe', 'Baden-Baden', 'Ostalbkreis',
        'Heidenheim', 'Main-Tauber-Kreis', 'Schwäbisch Hall',
        'Hohenlohekreis', 'Heilbronn', 'Heilbronn, Universitätsstadt',
        'Rems-Murr-Kreis', 'Ludwigsburg', 'Göppingen', 'Esslingen',
        'Böblingen', 'Stuttgart', 'Südwestpfalz', 'Mainz-Bingen',
        'Südliche Weinstraße', 'Mayen-Koblenz', 'Cochem-Zell',
        'Bad Dürkheim', 'Bad Kreuznach', 'Bergstraße', 'Wiesbaden',
        'Offenbach am Main', 'Frankfurt am Main', 'Darmstadt', 'Unna',
        'Soest', 'Siegen-Wittgenstein', 'Märkischer Kreis',
        'Hochsauerlandkreis', 'Ennepe-Ruhr-Kreis', 'Herne', 'Hamm',
        'Hagen', 'Dortmund', 'Bochum', 'Paderborn', 'Minden-Lübbecke',
        'Lippe', 'Höxter', 'Birkenfeld', 'Darmstadt-Dieburg', 'Groß-Gerau',
        'Olpe', 'Herford', 'Hochtaunuskreis', 'Ahrweiler', 'Koblenz',
        'Werra-Meißner-Kreis', 'Waldeck-Frankenberg', 'Schwalm-Eder-Kreis',
        'Kassel', 'Hersfeld-Rotenburg', 'Fulda', 'Vogelsbergkreis',
        'Altenkirchen (Westerwald)', 'Limburg-Weilburg',
        'Marburg-Biedenkopf', 'Main-Taunus-Kreis', 'Odenwaldkreis',
        'Offenbach', 'Main-Kinzig-Kreis', 'Wetteraukreis', 'Gießen',
        'Lahn-Dill-Kreis', 'Rheingau-Taunus-Kreis', 'Ebersberg',
        'Schwabach', 'Tirschenreuth'];

function displayIntensiveCareCapacitiesCharts(content) {
    for (i = 0; i < 5 /*kreisValues.length*/; i++) {
        displayIntensiveCareCapacitiesChart(content, kreisValues[i]);
    }
}

function displayIntensiveCareCapacitiesChart(content, kreis) {
    const { chartViewElement, canvas } = UIUtils.createChartViewElementWithHeading(kreis);
    content.appendChild(chartViewElement);
    withCsvDo(
        `data/intensivstationen/intensivstationen-${kreis}.csv`,
        csv =>
            new IntensiveCareCapacitiesChartView().displayChart(
                {
                    data: csv,
                    canvas: canvas,
                    title: kreis
                }));
}

function withCsvDo(file, csvConsumer) {
    Papa.parse(
        file,
        {
            header: true,
            dynamicTyping: true,
            download: true,
            complete: results => csvConsumer(results.data)
        });
}
