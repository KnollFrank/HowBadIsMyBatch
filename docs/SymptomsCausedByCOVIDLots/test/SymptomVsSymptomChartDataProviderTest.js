QUnit.module('SymptomVsSymptomChartDataProviderTest', function () {

    QUnit.test('shouldProvideChartData', function (assert) {
        // Given
        const prrByLotX = {
            "lotX": 1.0,
            "lotCommon": 2.0
        };
        const prrByLotY = {
            "lotCommon": 3.0,
            "lotY": 4.0
        };

        // When
        const chartData = SymptomVsSymptomChartDataProvider.getChartData({ prrByLotX, prrByLotY });

        // Then
        assert.deepEqual(
            chartData,
            {
                labels: ["lotCommon"],
                data: [
                    {
                        x: 2.0,
                        y: 3.0
                    }
                ]
            });
    });
});