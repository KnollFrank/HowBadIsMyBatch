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
                options: this.#getOptions(title),
                plugins: [this.#getPlugin()]
            });
    }

    #getPlugin() {
        return {
            beforeDraw: chart => {
                if (chart.config.options.chartArea) {
                    const ctx = chart.ctx;
                    const chartArea = chart.chartArea;
                    const width = chartArea.right - chartArea.left;
                    const height = chartArea.bottom - chartArea.top

                    const green = 'rgba(56, 168, 0, 0.75)';
                    const yellow = 'rgba(254, 178, 76, 0.75)';
                    const red = 'rgba(240, 59, 32, 0.75)';
                    const redHeight = height * 10 / 100;
                    const yellowHeight = height * 15 / 100;
                    const greenHeight = height * 75 / 100;

                    ctx.save();
                    ctx.fillStyle = red;
                    ctx.fillRect(chartArea.left, chartArea.bottom - redHeight, width, redHeight);

                    ctx.fillStyle = yellow;
                    ctx.fillRect(chartArea.left, chartArea.bottom - redHeight - yellowHeight, width, yellowHeight);

                    ctx.fillStyle = green;
                    ctx.fillRect(chartArea.left, chartArea.bottom - redHeight - yellowHeight - greenHeight, width, greenHeight);
                    ctx.restore();
                }
            }
        };
    }

    #getData(data) {
        return {
            datasets: [
                {
                    label: 'Anteil freier Betten',
                    data: data,
                    parsing: {
                        yAxisKey: 'free_beds_divided_by_all_beds_in_percent'
                    },
                    backgroundColor: 'rgba(0, 0, 150, 1)'
                }
            ]
        };
    }

    #getOptions(title) {
        return {
            chartArea: {
            },
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
                    min: 0,
                    max: 100,
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