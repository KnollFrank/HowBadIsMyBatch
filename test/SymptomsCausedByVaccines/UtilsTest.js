QUnit.module('UtilsTest', function () {

    QUnit.test('convertDict2CSV', function (assert) {
        // Given
        const dict = {
            "MM,R": 26.17432376240791,
            "VARCEL": 10.549534724816644
        };

        // When
        const csv = Utils.convertDict2CSV(dict);

        // Then
        assert.equal(csv, '"MM,R","VARCEL"\n26.17432376240791,10.549534724816644');
    });
});