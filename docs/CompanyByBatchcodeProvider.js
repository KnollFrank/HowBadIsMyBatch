class CompanyByBatchcodeProvider {

    static getCompany(batchcode) {
        return fetch(`data/histograms/Global/${batchcode}.json`)
            .then(response => response.json())
            .then(histoDescrs => histoDescrs.Company);
    }
}