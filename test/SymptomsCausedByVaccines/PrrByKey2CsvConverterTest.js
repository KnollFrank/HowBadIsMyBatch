QUnit.module('PrrByKey2CsvConverterTest', function () {

    QUnit.test('convertPrrByKey2Csv', function (assert) {
        // Given
        const prrByKey = {
            "MM,R": 26.17432376240791,
            "VARCEL": 10.549534724816644
        };

        // When
        const csv = PrrByKey2CsvConverter.convertPrrByKey2Csv(
            {
                prrByKey: prrByKey,
                keyColumn: 'Vaccine',
                prrColumn: 'Proportional Reporting Ratio'
            });

        // Then
        const csvExpected =
            `"Vaccine","Proportional Reporting Ratio"
"MM,R",26.17432376240791
"VARCEL",10.549534724816644`;
        assert.equal(csv, csvExpected);
    });
});