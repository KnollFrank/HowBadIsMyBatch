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
                plugins: [this.#getBackgroundTrafficLightsPlugin()]
            });
    }

    #getBackgroundTrafficLightsPlugin() {
        function fillRect({ chart, startInPercent, endInPercent, color }) {
            const ctx = chart.ctx;
            const chartArea = chart.chartArea;
            const chartWidth = chartArea.right - chartArea.left;
            const chartHeight = chartArea.bottom - chartArea.top
            const y = chartArea.bottom - chartHeight * endInPercent / 100;
            const height = chartHeight * (endInPercent - startInPercent) / 100;
            ctx.fillStyle = color;
            ctx.fillRect(chartArea.left, y, chartWidth, height);
        }

        function drawTrafficLights(chart) {
            const RED = 'rgba(240, 59, 32, 0.75)';
            const YELLOW = 'rgba(254, 178, 76, 0.75)';
            const GREEN = 'rgba(56, 168, 0, 0.75)';
            chart.ctx.save();
            fillRect({ chart: chart, startInPercent: 0, endInPercent: 10, color: RED });
            fillRect({ chart: chart, startInPercent: 10, endInPercent: 25, color: YELLOW });
            fillRect({ chart: chart, startInPercent: 25, endInPercent: 100, color: GREEN });
            chart.ctx.restore();
        }

        return {
            beforeDraw: chart => {
                if (chart.config.options.chartArea) {
                    drawTrafficLights(chart);
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