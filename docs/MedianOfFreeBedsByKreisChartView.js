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

    setData(data) {
        this.#chart.config.data.datasets[0].data = data;
        this.#chart.update();
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
                    text: label
                },
                tooltip: {
                    callbacks: {
                        label: UIUtils.getLabelWithPercent
                    }
                }
            },
            responsive: true,
            scales: {
                y: UIUtils.getPercentageScale(label)
            },
            parsing: {
                xAxisKey: 'Kreis'
            }
        };
    }
}