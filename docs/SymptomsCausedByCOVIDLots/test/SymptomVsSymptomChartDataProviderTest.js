QUnit.module('SymptomVsSymptomChartDataProviderTest', function () {

    QUnit.test.each(
        'shouldRetainCommonLots',
        [
            [
                {
                    dict1: {
                        "lotX": 1.0
                    },
                    dict2: {
                        "lotY": 2.0
                    }
                },
                {
                    dict1: {
                    },
                    dict2: {
                    }
                }
            ],
            [
                {
                    dict1: {
                        "lotX": 1.0,
                        "lotCommon": 2.0
                    },
                    dict2: {
                        "lotCommon": 3.0,
                        "lotY": 4.0
                    }
                },
                {
                    dict1: {
                        "lotCommon": 2.0
                    },
                    dict2: {
                        "lotCommon": 3.0
                    }
                }
            ]
        ],
        (assert, [dicts, dictsHavingCommonKeys]) => {
            // Given

            // When
            const dictsHavingCommonKeysActual = SymptomVsSymptomChartDataProvider.retainCommonKeys(dicts);

            // Then
            assert.deepEqual(dictsHavingCommonKeysActual, dictsHavingCommonKeys);
        });

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