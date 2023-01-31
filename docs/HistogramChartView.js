class HistogramChartView {

    #canvas;
    #chart;

    constructor(canvas) {
        this.#canvas = canvas;
    }

    displayChart(histoDescr) {
        if (this.#chart != null) {
            this.#chart.destroy();
        }
        this.#chart = new Chart(
            this.#canvas,
            {
                type: 'bar',
                data: this.#getData(histoDescr),
                options: this.#getOptions()
            });
    }

    setData(histoDescr) {
        const data = this.#getData(histoDescr);
        this.#chart.config.data = data;
        this.#chart.update();
    }

    #getData(histoDescr) {
        const { 'keys': symptoms, 'values': frequencies } = Utils.getKeysAlignedWithValues(histoDescr.histogram);
        return {
            labels: symptoms,
            datasets: [{
                label: histoDescr.batchcodes.join(', '),
                data: frequencies
            }]
        };
    }

    #getOptions() {
        return {
            indexAxis: 'y',
            responsive: true,
            scales: {
                y: {
                    title: {
                        display: true,
                        text: 'Symptom'
                    }
                },
                x: {
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