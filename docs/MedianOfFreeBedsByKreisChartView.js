class MedianOfFreeBedsByKreisChartView {

    #canvas;
    #chart;

    constructor(canvas) {
        this.#canvas = canvas;
    }

    displayChart(data) {
        if (this.#chart != null) {
            this.#chart.destroy();
        }
        const label = 'Median der Anteile freier Betten';
        this.#chart = new Chart(
            this.#canvas,
            {
                type: 'bar',
                data: this.#getData(data, label),
                options: this.#getOptions(label)
            });
    }

    #getData(data, label) {
        return {
            datasets: [
                {
                    label: label,
                    data: data,
                    parsing: {
                        yAxisKey: 'median_free_beds_in_percent'
                    },
                    backgroundColor: 'rgba(0, 255, 0, 1)'
                }
            ]
        };
    }

    #getOptions(label) {
        return {
            plugins: {
                title: {
                    display: true,
                    text: 'some Title'
                },
                tooltip: {
                    // FK-TODO: DRY with FreeBedsChartView.js
                    callbacks: {
                        label: function (context) {
                            let label = context.dataset.label || '';

                            if (label) {
                                label += ': ';
                            }
                            if (context.parsed.y !== null) {
                                label += context.parsed.y.toFixed(1) + "%";
                            }
                            return label;
                        }
                    }
                }
            },
            responsive: true,
            scales: {
                y: {
                    min: 0,
                    max: 100,
                    title: {
                        display: true,
                        text: label
                    },
                    // FK-TODO: DRY with FreeBedsChartView.js
                    ticks: {
                        callback: value => value + "%"
                    }
                }
            },
            parsing: {
                xAxisKey: 'Kreis'
            }
        };
    }
}