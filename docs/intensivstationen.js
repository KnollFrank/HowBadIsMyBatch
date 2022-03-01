function displayIntensiveCareCapacitiesChart(
    { intensiveCareCapacitiesChartView, headingElement, populationElement, kreisText, kreisValue }) {

    headingElement.textContent = kreisText
    fetch(`data/intensivstationen/intensivstationen-${kreisValue}.json`)
        .then(response => response.json())
        .then(json => {
            populationElement.textContent = json.population;
            intensiveCareCapacitiesChartView.displayChart({ data: json.data, title: kreisText });
        });
}
