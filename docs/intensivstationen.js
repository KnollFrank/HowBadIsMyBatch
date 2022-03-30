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
                    data: getDataDicts(json.data),
                    title: kreisText
                }));
}

function getDataDicts(data) {
    const dataDicts = get_free_beds_divided_by_all_beds_in_percent_dataDicts(data);
    add_median_free_beds_in_percent(dataDicts);
    return dataDicts;
}

function get_free_beds_divided_by_all_beds_in_percent_dataDicts(data) {
    return data.map(({ date, betten_frei, betten_belegt }) =>
    (
        {
            "date": date,
            "free_beds_divided_by_all_beds_in_percent": betten_frei / (betten_frei + betten_belegt) * 100
        }
    ));
}

function add_median_free_beds_in_percent(dataDicts) {
    const median_free_beds_in_percent =
        Utils.median(
            dataDicts.map(dataDict => dataDict.free_beds_divided_by_all_beds_in_percent));
    for (const dataDict of dataDicts) {
        dataDict["median_free_beds_in_percent"] = median_free_beds_in_percent;
    }
}

function displayMedianOfFreeBedsByKreisChart(canvas, slider) {
    fetch(`data/intensivstationen/medianOfFreeBedsByKreisTable.json`)
        .then(response => response.json())
        .then(json => _displayMedianOfFreeBedsByKreisChart(canvas, slider, json));
}

function _displayMedianOfFreeBedsByKreisChart(canvas, sliderElement, data) {
    const medianOfFreeBedsByKreisChartView = new MedianOfFreeBedsByKreisChartView(canvas);
    medianOfFreeBedsByKreisChartView.displayChart(data);
    createSlider(
        sliderElement,
        {
            min: 0,
            max: data.length - 1
        },
        ([start, end]) => medianOfFreeBedsByKreisChartView.setData(data.slice(start, end + 1)));
}

function createSlider(sliderElement, range, onUpdate) {
    noUiSlider.create(
        sliderElement,
        {
            start: [range.min, range.max],
            connect: true,
            range: range,
            step: 1,
            orientation: 'horizontal'
        });
    sliderElement.noUiSlider.on('update', onUpdate);
}
