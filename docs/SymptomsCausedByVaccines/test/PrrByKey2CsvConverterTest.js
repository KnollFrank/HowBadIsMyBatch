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
                heading: '# Symptom: Acute hepatitis C',
                columns: {
                    keyColumn: 'Vaccine',
                    prrColumn: 'Proportional Reporting Ratio'
                },
                prrByKey: prrByKey
            });

        // Then
        const csvExpected =
            `# Symptom: Acute hepatitis C

"Vaccine","Proportional Reporting Ratio"
"MM,R",26.17432376240791
"VARCEL",10.549534724816644`;
        assert.equal(csv, csvExpected);
    });
});