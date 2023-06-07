class BarChartDescriptionProvider {

    static getBarChartDescription(batchcode) {
        return fetch(`data/barChartDescriptionTables/${batchcode}.json`)
            .then(response => response.json());
    }
}