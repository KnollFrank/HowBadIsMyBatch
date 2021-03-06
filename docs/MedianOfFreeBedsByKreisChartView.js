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
        const label = 'Median freier Betten';
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
                        xAxisKey: 'median_free_beds_in_percent'
                    },
                    backgroundColor: 'rgba(0, 255, 0, 1)'
                }
            ]
        };
    }

    #getOptions(label) {
        return {
            indexAxis: 'y',
            plugins: {
                title: {
                    display: true,
                    text: label
                },
                tooltip: {
                    callbacks: {
                        label: UIUtils.getXLabelWithPercent
                    }
                }
            },
            responsive: true,
            scales: {
                y: {
                    title: {
                        display: true,
                        text: 'Landkreis'
                    }
                },
                x: UIUtils.getPercentageScale(label)
            },
            parsing: {
                yAxisKey: 'Kreis'
            }
        };
    }
}