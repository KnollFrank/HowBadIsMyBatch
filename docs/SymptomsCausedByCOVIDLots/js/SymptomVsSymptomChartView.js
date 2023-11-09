class SymptomVsSymptomChartView {

    #canvas;
    #chart;

    constructor(canvas) {
        this.#canvas = canvas;
    }

    // FK-TODO: refactor
    displayChart(symptomX, symptomY) {
        if (this.#chart != null) {
            this.#chart.destroy();
        }
        // FK-TODO: fetch multiple files: https://stackoverflow.com/a/31711496 or https://stackoverflow.com/a/53892713
        PrrByVaccineProvider.getPrrByVaccine(symptomX)
            .then(
                prrByLotX => {
                    PrrByVaccineProvider.getPrrByVaccine(symptomY)
                        .then(
                            prrByLotY => {
                                const chartData = SymptomVsSymptomChartDataProvider.getChartData({ prrByLotX, prrByLotY });
                                const data = {
                                    datasets: [{
                                        labels: chartData.labels,
                                        data: chartData.data,
                                        backgroundColor: 'rgb(0, 0, 255)'
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
                                        },
                                        plugins: {
                                            legend: {
                                                display: false
                                            },
                                            tooltip: {
                                                callbacks: {
                                                    label: function (context) {
                                                        return 'Batch: ' + context.dataset.labels[context.dataIndex];
                                                    }
                                                }
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