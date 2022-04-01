function displayIntensiveCareCapacitiesChart(
    { intensiveCareCapacitiesChartView, sliderElement, headingElement, populationElement, kreisText, kreisValue }) {

    headingElement.textContent = kreisText
    fetch(`data/intensivstationen/intensivstationen-${kreisValue}.json`)
        .then(response => response.json())
        .then(json => _displayIntensiveCareCapacitiesChart({ intensiveCareCapacitiesChartView, sliderElement, populationElement, kreisText, json }));
}

function _displayIntensiveCareCapacitiesChart({ intensiveCareCapacitiesChartView, sliderElement, populationElement, kreisText, json }) {
    populationElement.textContent = new Intl.NumberFormat().format(json.population);
    intensiveCareCapacitiesChartView.displayChart({ data: json.data, title: kreisText });
    createSlider(
        {
            sliderElement: sliderElement,
            range: {
                min: 0,
                max: json.data.length - 1
            },
            orientation: 'horizontal',
            onUpdate: ([start, end]) => intensiveCareCapacitiesChartView.setData(json.data.slice(start, end + 1))
        });
}

function displayFreeBedsChart({ freeBedsChartView, sliderElement, kreisText, kreisValue }) {
    fetch(`data/intensivstationen/intensivstationen-${kreisValue}.json`)
        .then(response => response.json())
        .then(json => _displayFreeBedsChart({ freeBedsChartView, sliderElement, kreisText, json }));
}

function _displayFreeBedsChart({ freeBedsChartView, sliderElement, kreisText, json }) {
    const data = getDataDicts(json.data);
    freeBedsChartView.displayChart(
        {
            data: data,
            title: kreisText
        });
    createSlider(
        {
            sliderElement: sliderElement,
            range: {
                min: 0,
                max: data.length - 1
            },
            orientation: 'horizontal',
            onUpdate: ([start, end]) => freeBedsChartView.setData(data.slice(start, end + 1))
        });
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
        {
            sliderElement: sliderElement,
            range: {
                min: 0,
                max: data.length - 1
            },
            orientation: 'vertical',
            height: canvas.style.height,
            onUpdate: ([start, end]) => medianOfFreeBedsByKreisChartView.setData(data.slice(start, end + 1))
        });
}

function createSlider({ sliderElement, range, orientation, height = null, onUpdate }) {
    if ('noUiSlider' in sliderElement) {
        sliderElement.noUiSlider.destroy();
    }
    noUiSlider.create(
        sliderElement,
        {
            start: [range.min, range.max],
            connect: true,
            range: range,
            step: 1,
            orientation: orientation
        });
    sliderElement.noUiSlider.on('update', onUpdate);
    if (height != null) {
        sliderElement.style.height = height;
    }
}
