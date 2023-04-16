class HistoDescrsProvider {

    static getHistoDescrs(batchcode) {
        return fetch(`data/histograms/Global/${batchcode}.json`)
            .then(response => response.json())
            .then(histoDescrs => {
                histoDescrs.histograms.sort((histoDescr1, histoDescr2) => histoDescr1.batchcodes.length - histoDescr2.batchcodes.length);
                histoDescrs.histogram = histoDescrs.histograms[0].histogram;
                delete histoDescrs.histograms;
                return histoDescrs;
            });
    }
}