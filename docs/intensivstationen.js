function displayIntensiveCareCapacitiesChart(
    { intensiveCareCapacitiesChartView, headingElement, populationElement, kreisText, kreisValue }) {

    headingElement.textContent = kreisText
    fetch(`data/intensivstationen/intensivstationen-${kreisValue}.json`)
        .then(response => response.json())
        .then(json => {
            populationElement.textContent = new Intl.NumberFormat().format(json.population);
            intensiveCareCapacitiesChartView.displayChart({ data: json.data, title: kreisText });
        });
}

function displayFreeBedsChart({ freeBedsChartView, kreisText, kreisValue }) {
    fetch(`data/intensivstationen/intensivstationen-${kreisValue}.json`)
        .then(response => response.json())
        .then(json =>
            freeBedsChartView.displayChart(
                {
                    data: get_free_beds_divided_by_all_beds_in_percent(json.data),
                    title: kreisText
                }));
}

function get_free_beds_divided_by_all_beds_in_percent(data) {
    return data.map(({ date, betten_frei, betten_belegt }) =>
    (
        {
            "date": date,
            "free_beds_divided_by_all_beds_in_percent": betten_frei / (betten_frei + betten_belegt) * 100
        }
    ));
}
