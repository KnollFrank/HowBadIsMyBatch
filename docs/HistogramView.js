class HistogramView {

    #uiContainer;

    constructor(uiContainer) {
        this.#uiContainer = uiContainer
    }

    displayHistogramsForBatchcode(batchcode) {
        this
            .#loadHistoDescrsForBatchcode(batchcode)
            .then(histoDescrs => this.#displayHistograms(histoDescrs));
    }

    #loadHistoDescrsForBatchcode(batchcode) {
        const loadingText = document.createTextNode('Loading...');
        this.#uiContainer.appendChild(loadingText);
        return fetch(`data/histograms/${batchcode}.json`)
            .then(response => {
                loadingText.remove();
                return response.json();
            })
    }

    #displayHistograms(histoDescrs) {
        this.#uiContainer.appendChild(document.createTextNode(histoDescrs.batchcode));
        for (const histoDescr of histoDescrs.histograms) {
            this.#uiContainer.appendChild(this.#createHistogram(histoDescr).canvas);
        }
    }

    #createHistogram(histoDescr) {
        // FK-TODO: brauchen Slider wie bei intensivstationen
        const canvas = document.createElement("canvas");
        const { 'keys': symptoms, 'values': frequencies } = Utils.getKeysAlignedWithValues(histoDescr.histogram);
        return new Chart(
            canvas,
            {
                type: 'bar',
                data: {
                    labels: symptoms,
                    datasets: [{
                        label: histoDescr.batchcodes.join(', '),
                        data: frequencies
                    }]
                },
                options: {
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
                            title: {
                                display: true,
                                text: 'Frequency'
                            }
                        }
                    },
                }
            }
        );
    }
}