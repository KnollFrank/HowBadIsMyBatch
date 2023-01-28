class HistogramView {

    #uiContainer;

    constructor(uiContainer) {
        this.#uiContainer = uiContainer
    }

    displayHistogramsForBatchcode(batchcode) {
        fetch(`data/histograms/${batchcode}.json`)
            .then(response => response.json())
            .then(histoDescr => {
                const canvas = document.createElement("canvas");
                this.#uiContainer.appendChild(canvas);
                this.#displayChart(histoDescr, canvas);
            });
    }

    #displayChart(histoDescr, canvas) {
        // FK-TODO: brauchen Slider wie bei intensivstationen
        new Chart(
            canvas,
            {
                type: 'bar',
                data: {
                    datasets: [{
                        label: histoDescr.batchcode,
                        data: histoDescr.histograms[0].histogram
                    }]
                }
            }
        );
    }
}