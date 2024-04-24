class CompanyByBatchcodeProvider {

    static getCompany(batchcode) {
        return HistoDescrsProvider
            .getHistoDescrs(batchcode)
            .then(histoDescrs => histoDescrs.Company);
    }
}