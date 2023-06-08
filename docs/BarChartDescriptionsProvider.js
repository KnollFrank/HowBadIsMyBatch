class BarChartDescriptionsProvider {

    static getBarChartDescriptions() {
        return fetch('data/barChartDescriptionTable.json').then(response => response.json());
    }
}