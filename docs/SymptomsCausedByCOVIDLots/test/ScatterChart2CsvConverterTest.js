QUnit.module('ScatterChart2CsvConverterTest', function () {

    QUnit.test('convertScatterChart2Csv', function (assert) {
        // Given
        const scatterChartDescr = {
            symptomX: 'Adult failure to thrive',
            symptomY: 'Acariasis',
            batches: ['002A21A', '002A21B'],
            data: [
                {
                    x: 2.1,
                    y: 3.1
                },
                {
                    x: 4.1,
                    y: 5.1
                }
            ]
        };

        // When
        const csv = ScatterChart2CsvConverter.convertScatterChart2Csv(scatterChartDescr);

        // Then
        const csvExpected =
            `"Batch","PRR ratio of Batch for Adult failure to thrive","PRR ratio of Batch for Acariasis"
"002A21A",2.1,3.1
"002A21B",4.1,5.1`;
        assert.equal(csv, csvExpected);
    });
});