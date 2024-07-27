class DrugsChartView {

    #canvas;
    #chart;

    constructor(canvas) {
        this.#canvas = canvas;
    }

    displayChart(drugDescr) {
        if (this.#chart != null) {
            this.#chart.destroy();
        }
        this.#chart = new Chart(
            this.#canvas,
            {
                type: 'bar',
                plugins: [ChartDataLabels],
                data: this.#getData(drugDescr),
                options: this.#getOptions()
            });
    }

    setData(histoDescr) {
        const data = this.#getData(histoDescr);
        this.#chart.config.data = data;
        this.#chart.update();
    }

    #getData(drugDescr) {
        return {
            labels: drugDescr['DRUG'],
            datasets: [{
                label: 'Fatal',
                data: this.#divide(drugDescr['FATAL'], drugDescr['CASES']),
                backgroundColor: '#FF0000'
            },
            {
                label: 'Recovered',
                data: this.#divide(drugDescr['RECOVERED'], drugDescr['CASES']),
                backgroundColor: '#00FF00'
            }]
        };
    }

    #divide(dividends, divisors) {
        return Utils
            .zip([dividends, divisors])
            .map(([dividend, divisor]) => dividend / divisor);
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
                }
            }
        };
    }
}