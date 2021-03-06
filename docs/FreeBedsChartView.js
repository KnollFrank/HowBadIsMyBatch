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
        const label = 'freie Betten';
        this.#chart = new Chart(
            this.#canvas,
            {
                type: 'line',
                data: this.#getData(data, label),
                options: this.#getOptions(title, label),
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
            const RED = 'rgba(240, 59, 32, 0.75)'; // #F03B20
            const YELLOW = 'rgba(254, 178, 76, 0.75)'; // #FEB24C
            const GREEN = 'rgba(56, 168, 0, 0.75)'; // #38A800
            chart.ctx.save();
            fillRect({ chart: chart, startInPercent: 0, endInPercent: 10, color: RED });
            fillRect({ chart: chart, startInPercent: 10, endInPercent: 25, color: YELLOW });
            fillRect({ chart: chart, startInPercent: 25, endInPercent: 100, color: GREEN });
            chart.ctx.restore();
        }

        return { beforeDraw: drawTrafficLights };
    }

    setData(data) {
        this.#chart.config.data.datasets[0].data = data;
        this.#chart.config.data.datasets[1].data = data;
        this.#chart.update();
    }

    #getData(data, label) {
        return {
            datasets: [
                {
                    label: label,
                    data: data,
                    parsing: {
                        yAxisKey: 'free_beds_divided_by_all_beds_in_percent'
                    },
                    backgroundColor: 'rgba(0, 0, 150, 1)'
                },
                {
                    label: 'Median freier Betten',
                    data: data,
                    parsing: {
                        yAxisKey: 'median_free_beds_in_percent'
                    },
                    backgroundColor: 'rgba(0, 150, 150, 1)'
                }
            ]
        };
    }

    #getOptions(title, label) {
        return {
            plugins: {
                title: {
                    display: true,
                    text: title
                },
                tooltip: {
                    callbacks: {
                        label: UIUtils.getYLabelWithPercent
                    }
                }
            },
            responsive: true,
            scales: {
                x: {
                    type: 'time',
                    time: {
                        tooltipFormat: 'DD.MM.YYYY',
                        unit: 'month',
                        displayFormats: {
                            'month': 'MMM YYYY'
                        }
                    }
                },
                y: UIUtils.getPercentageScale(label)
            },
            parsing: {
                xAxisKey: 'date'
            }
        };
    }
}