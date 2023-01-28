class HistogramView {

    #uiContainer;

    constructor(uiContainer) {
        this.#uiContainer = uiContainer
    }

    displayHistogramsForBatchcode(batchcode) {
        const loadingText = document.createTextNode('Loading...');
        this.#uiContainer.appendChild(loadingText);
        fetch(`data/histograms/${batchcode}.json`)
            .then(response => response.json())
            .then(histoDescrs => {
                loadingText.remove();
                for (const histoDescr of histoDescrs.histograms) {
                    const canvas = document.createElement("canvas");
                    this.#uiContainer.appendChild(canvas);
                    this.#displayHistogram(histoDescr, canvas);
                }
            });
    }

    #displayHistogram(histoDescr, canvas) {
        // FK-TODO: brauchen Slider wie bei intensivstationen
        new Chart(
            canvas,
            {
                type: 'bar',
                data: {
                    datasets: [{
                        label: histoDescr.batchcodes.join(', '),
                        data: histoDescr.histogram
                    }]
                }
            }
        );
    }
}