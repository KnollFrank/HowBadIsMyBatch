class HistoDescrsProvider {

    static getHistoDescrs(batchcode) {
        return fetch(`data/histograms/Global/${batchcode}.json`)
            .then(response => response.json())
    }
}