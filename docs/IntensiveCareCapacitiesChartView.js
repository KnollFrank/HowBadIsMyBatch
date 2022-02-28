class IntensiveCareCapacitiesChartView {

    displayChart({ data, canvas, title }) {
        new Chart(
            canvas,
            {
                type: 'bar',
                data: this.#getData(data),
                options: this.#getOptions(title)
            });
    }

    #getData(data) {
        return {
            datasets: [
                {
                    label: 'Belegte Betten',
                    data: data,
                    parsing: {
                        yAxisKey: 'betten_belegt'
                    },
                    backgroundColor: 'rgba(255, 0, 0, 1)',
                },
                {
                    label: 'Freie Betten',
                    data: data,
                    parsing: {
                        yAxisKey: 'betten_frei'
                    },
                    backgroundColor: 'rgba(0, 255, 0, 1)',
                }
            ]
        };
    }

    #getOptions(title) {
        return {
            plugins: {
                title: {
                    display: true,
                    text: title
                },
            },
            responsive: true,
            scales: {
                x: {
                    stacked: true,
                    type: 'time',
                    time: {
                        unit: 'month'
                    }
                },
                y: {
                    stacked: true
                }
            },
            parsing: {
                xAxisKey: 'date'
            }
        };
    }
}