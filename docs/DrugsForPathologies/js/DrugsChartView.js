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
                data: this.#getData(drugDescr),
                options: this.#getOptions()
            });
    }

    #getData(drugDescr) {
        return {
            labels: this.#addNumberOfReports2EachDrug(drugDescr['DRUG'], drugDescr['CASES']),
            datasets: [
                {
                    label: 'Recovered',
                    data: this.#divide(drugDescr['RECOVERED'], drugDescr['CASES']),
                    backgroundColor: '#00FF00'
                },
                {
                    label: 'Fatal',
                    data: this.#divide(drugDescr['FATAL'], drugDescr['CASES']),
                    backgroundColor: '#FF0000'
                }
            ]
        };
    }

    #addNumberOfReports2EachDrug(drugList, numberOfReportsList) {
        return Utils
            .zip([drugList, numberOfReportsList])
            .map(([drug, numberOfReports]) => `${drug} (${numberOfReports} reports)`);
    }

    #divide(dividends, divisors) {
        return Utils
            .zip([dividends, divisors])
            .map(([dividend, divisor]) => dividend / divisor);
    }

    #getOptions() {
        return {
            title: {
                display: true,
                position: 'top'
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Drug'
                    }
                },
                y: {
                    ticks: {
                        format: {
                            style: 'percent'
                        }
                    },
                    title: {
                        display: true,
                        text: 'Percentage of reports'
                    }
                }
            }
        };
    }
}