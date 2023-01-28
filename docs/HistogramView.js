class HistogramView {

    #uiContainer;

    constructor(uiContainer) {
        this.#uiContainer = uiContainer
    }

    displayHistogramsForBatchcode(batchcode) {
        // FK-TODO: zeige "Loading..." bis Daten geladen sind.
        fetch(`data/histograms/${batchcode}.json`)
            .then(response => response.json())
            .then(histoDescrs => {
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
                        // FK-TODO: alle histoDescr.batchcodes zu einem String zusammenfassen
                        label: histoDescr.batchcodes[0],
                        data: histoDescr.histogram
                    }]
                }
            }
        );
    }
}