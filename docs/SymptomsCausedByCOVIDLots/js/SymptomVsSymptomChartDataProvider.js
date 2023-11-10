class SymptomVsSymptomChartDataProvider {

    static getChartData({ prrByLotX, prrByLotY }) {
        const { dict1: prrByLotXCommon, dict2: prrByLotYCommon } =
            DictUtils.retainCommonKeys(
                {
                    dict1: prrByLotX,
                    dict2: prrByLotY
                });
        const lots = Object.keys(prrByLotXCommon);
        return {
            labels: lots,
            data:
                lots.map(
                    lot => ({
                        x: prrByLotXCommon[lot],
                        y: prrByLotYCommon[lot]
                    }))
        };
    }
}