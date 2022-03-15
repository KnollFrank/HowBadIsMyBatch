class FreeBedsChartView {

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
                type: 'line',
                data: this.#getData(data),
                options: this.#getOptions(title)
            });
    }

    #getData(data) {
        return {
            datasets: [
                {
                    label: 'Anteil freier Betten',
                    data: data,
                    parsing: {
                        yAxisKey: 'free_beds_divided_by_all_beds'
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
                tooltip: {
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
                x: {
                    type: 'time',
                    time: {
                        unit: 'month'
                    }
                },
                y: {
                    // min: 0,
                    // max: 100,
                    title: {
                        display: true,
                        text: "Anteil freier Betten"
                    },
                    ticks: {
                        callback: value => value + "%"
                    }
                }
            },
            parsing: {
                xAxisKey: 'date'
            }
        };
    }
}