QUnit.module('DictUtilsTest', function () {

    QUnit.test.each(
        'shouldRetainCommonKeys',
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
            const dictsHavingCommonKeysActual = DictUtils.retainCommonKeys(dicts);

            // Then
            assert.deepEqual(dictsHavingCommonKeysActual, dictsHavingCommonKeys);
        });
});