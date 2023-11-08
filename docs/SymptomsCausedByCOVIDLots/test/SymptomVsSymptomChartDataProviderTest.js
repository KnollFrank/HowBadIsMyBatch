QUnit.module('SymptomVsSymptomChartDataProviderTest', function () {

    QUnit.test.each(
        'shouldRetainCommonLots',
        [
            [
                {
                    prrByLotX: {
                        "lotX": 1.0
                    },
                    prrByLotY: {
                        "lotY": 2.0
                    }
                },
                {
                    prrByLotX: {
                    },
                    prrByLotY: {
                    }
                }
            ],
            [
                {
                    prrByLotX: {
                        "lotX": 1.0,
                        "lotCommon": 2.0
                    },
                    prrByLotY: {
                        "lotCommon": 3.0,
                        "lotY": 4.0
                    }
                },
                {
                    prrByLotX: {
                        "lotCommon": 2.0
                    },
                    prrByLotY: {
                        "lotCommon": 3.0
                    }
                }
            ]
        ],
        (assert, [dataSets, mergedDataSets]) => {
            // Given

            // When
            const mergedDataSetsActual = SymptomVsSymptomChartDataProvider.retainCommonLots(dataSets);

            // Then
            assert.deepEqual(mergedDataSetsActual, mergedDataSets);
        });
});