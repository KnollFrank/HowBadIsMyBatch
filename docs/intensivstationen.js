function displayIntensiveCareCapacitiesChart(intensiveCareCapacitiesChartView, headingElement, kreisText, kreisValue) {
    headingElement.textContent = kreisText;
    fetch(`data/intensivstationen/intensivstationen-${kreisValue}.json`)
        .then(response => response.json())
        .then(json => intensiveCareCapacitiesChartView.displayChart({ data: json, title: kreisText }));
}
