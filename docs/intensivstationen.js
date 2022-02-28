function displayIntensiveCareCapacitiesChart(intensiveCareCapacitiesChartView, headingElement, kreisText, kreisValue) {
    headingElement.textContent = kreisText;
    withCsvDo(
        `data/intensivstationen/intensivstationen-${kreisValue}.csv`,
        csv => intensiveCareCapacitiesChartView.displayChart({ data: csv, title: kreisText }));
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
