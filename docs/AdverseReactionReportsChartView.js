class AdverseReactionReportsChartView {

    #canvas;
    #chart;

    constructor(canvas) {
        this.#canvas = canvas;
    }

    displayChart(ADRDescr) {
        if (this.#chart != null) {
            this.#chart.destroy();
        }
        this.#chart = new Chart(
            this.#canvas,
            {
                // FK-TODO: use a Polar Area Chart ('polarArea') or bar chart
                type: 'bar',
                data: this.#getData(ADRDescr),
                options: this.#getOptions()
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
                label: ADRDescr['batchcode'],
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
            title: {
                display: true,
                text: 'Adverse Reaction Report for Batch FE6208',
                position: 'top'
            }
        };
    }
}