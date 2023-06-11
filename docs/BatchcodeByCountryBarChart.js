class BatchcodeByCountryBarChart {

    #canvas;
    #chart;

    constructor(canvas) {
        this.#canvas = canvas;
    }

    displayChart(barChartDescription) {
        if (this.#chart != null) {
            this.#chart.destroy();
        }
        this.#chart = new Chart(
            this.#canvas,
            {
                type: 'bar',
                data: this.#getData(barChartDescription),
                options: this.#getOptions()
            });
    }

    setData(barChartDescription) {
        const data = this.#getData(barChartDescription);
        this.#chart.config.data = data;
        this.#chart.update();
    }

    #getData(barChartDescription) {
        return {
            labels: barChartDescription.countries,
            datasets: [
                {
                    label: `Known (${this.#dateRange2str(barChartDescription['date range known'])})`,
                    data: barChartDescription["Adverse Reaction Reports known"]
                },
                {
                    label: `Guessed (${this.#dateRange2str(barChartDescription['date range guessed'])})`,
                    data: barChartDescription["Adverse Reaction Reports guessed"]
                }
            ]
        };
    }

    #dateRange2str(dateRange) {
        return `${dateRange.start} - ${dateRange.end}`;
    }

    #getOptions() {
        return {
            plugins: {
                datalabels: {
                    anchor: 'end',
                    align: 'top'
                }
            },
            title: {
                display: true,
                position: 'top'
            },
            scales: {
                y: {
                    ticks: {
                        precision: 0
                    },
                    title: {
                        display: true,
                        text: 'Adverse Reaction Reports'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Country'
                    }
                }
            }
        };
    }
}