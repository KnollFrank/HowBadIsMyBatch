class SymptomVsSymptomChartView {

    #canvas;
    #chart;

    constructor(canvas) {
        this.#canvas = canvas;
    }

    displayChart(symptom1, symptom2) {
        if (this.#chart != null) {
            this.#chart.destroy();
        }
        // FK-TODO: fetch multiple files: https://stackoverflow.com/a/31711496 or https://stackoverflow.com/a/53892713
        PrrByVaccineProvider.getPrrByVaccine(symptom1)
            .then(
                prrByKey1 => {
                    PrrByVaccineProvider.getPrrByVaccine(symptom2)
                        .then(
                            prrByKey2 => {
                                const myData =
                                    Object
                                        .values(prrByKey2)
                                        .map(
                                            val =>
                                            ({
                                                x: val,
                                                y: val
                                            }));
                                const data = {
                                    datasets: [{
                                        label: 'Scatter Dataset',
                                        data: myData,
                                        backgroundColor: 'rgb(255, 99, 132)'
                                    }],
                                };
                                const config = {
                                    type: 'scatter',
                                    data: data,
                                    options: {
                                        scales: {
                                            x: {
                                                type: 'linear',
                                                position: 'bottom'
                                            }
                                        }
                                    }
                                };
                                this.#chart = new Chart(
                                    this.#canvas,
                                    // {
                                    //     type: 'bar',
                                    //     plugins: [ChartDataLabels],
                                    //     data: this.#getData(ADRDescr),
                                    //     options: this.#getOptions()
                                    // }
                                    config);
                            });
                });
    }

    setData(histoDescr) {
        const data = this.#getData(histoDescr);
        this.#chart.config.data = data;
        this.#chart.update();
    }

    #getData(ADRDescr) {
        return {
            labels: [
                'Deaths',
                'Disabilities',
                'Life Threatening Illnesses',
                'Other Adverse Events'
            ],
            datasets: [{
                // FK-TODO: refactor
                label: 'Batch ' + ADRDescr['batchcode'],
                data: [
                    ADRDescr['Deaths'],
                    ADRDescr['Disabilities'],
                    ADRDescr['Life Threatening Illnesses'],
                    ADRDescr['Adverse Reaction Reports'] - (ADRDescr['Deaths'] + ADRDescr['Disabilities'] + ADRDescr['Life Threatening Illnesses'])
                ],
                backgroundColor: '#1a73e8'
            }]
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
                }
            }
        };
    }
}