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
                    label: "frequencies before deletion", // FK-TODO: daterange einfügen
                    data: barChartDescription["frequencies before deletion"]
                },
                {
                    label: "frequencies guessed", // FK-TODO: daterange einfügen
                    data: barChartDescription["frequencies guessed"]
                }
            ]
        };
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
                        text: 'Frequency'
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