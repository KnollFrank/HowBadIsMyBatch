class IntensiveCareCapacitiesChartView {

    #canvas;
    #chart;

    constructor(canvas) {
        this.#canvas = canvas;
    }

    displayChart({ data, title }) {
        if (this.#chart != null) {
            this.#chart.destroy();
        }
        this.#chart = new Chart(
            this.#canvas,
            {
                type: 'bar',
                data: this.#getData(data),
                options: this.#getOptions(title)
            });
    }

    setData(data) {
        this.#chart.config.data.datasets[0].data = data;
        this.#chart.config.data.datasets[1].data = data;
        this.#chart.update();
    }

    #getData(data) {
        return {
            datasets: [
                {
                    label: 'Belegte Betten',
                    data: data,
                    parsing: {
                        yAxisKey: 'betten_belegt'
                    },
                    backgroundColor: 'rgba(255, 0, 0, 1)'
                },
                {
                    label: 'Freie Betten',
                    data: data,
                    parsing: {
                        yAxisKey: 'betten_frei'
                    },
                    backgroundColor: 'rgba(0, 255, 0, 1)'
                }
            ]
        };
    }

    #getOptions(title) {
        return {
            plugins: {
                title: {
                    display: true,
                    text: title
                },
            },
            responsive: true,
            scales: {
                x: {
                    stacked: true,
                    type: 'time',
                    time: {
                        tooltipFormat: 'DD.MM.YYYY',
                        unit: 'month',
                        displayFormats: {
                            'month': 'MMM YYYY'
                        }
                    }
                },
                y: {
                    stacked: true
                }
            },
            parsing: {
                xAxisKey: 'date'
            }
        };
    }
}