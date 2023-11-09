class SymptomVsSymptomChartView {

    #canvas;
    #chart;

    constructor(canvas) {
        this.#canvas = canvas;
    }

    // FK-TODO: refactor
    loadAndDisplayChart(symptomX, symptomY) {
        Promise
            .all([symptomX, symptomY].map(symptom => PrrByVaccineProvider.getPrrByVaccine(symptom)))
            .then(
                ([prrByLotX, prrByLotY]) => {
                    const { labels, data } = SymptomVsSymptomChartDataProvider.getChartData({ prrByLotX, prrByLotY });
                    this.#displayChart(symptomX, symptomY, labels, data);
                });
    }

    setData(histoDescr) {
        const data = this.#getData(histoDescr);
        this.#chart.config.data = data;
        this.#chart.update();
    }

    #displayChart(symptomX, symptomY, labels, data) {
        if (this.#chart != null) {
            this.#chart.destroy();
        }
        const config = {
            type: 'scatter',
            data: this.#getData(labels, data),
            options: this.#getOptions(symptomX, symptomY)
        };
        this.#chart = new Chart(this.#canvas, config);
    }

    #getData(labels, data) {
        return {
            datasets:
                [
                    {
                        labels: labels,
                        data: data,
                        backgroundColor: 'rgb(0, 0, 255)'
                    }
                ]
        };
    }

    #getOptions(symptomX, symptomY) {
        return {
            scales: {
                x: {
                    type: 'linear',
                    position: 'bottom',
                    title: {
                        display: true,
                        text: 'PRR ratio of Batch for ' + symptomX
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'PRR ratio of Batch for ' + symptomY
                    }
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
        };
    }
}