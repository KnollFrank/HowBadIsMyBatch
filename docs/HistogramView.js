class HistogramView {

    constructor() {
    }

    show(batchcode, div) {
        fetch(`data/histograms/${batchcode}.json`)
            .then(response => response.json())
            .then(json => {
                const data = json.histograms[3].histogram;
                new Chart(
                    div.querySelector('#symptomByBatchcodeHisto'),
                    {
                        type: 'bar',
                        data: {
                            datasets: [{
                                label: 'Acquisitions by year',
                                data: data
                            }]
                        }
                    }
                );
            });
    }
}