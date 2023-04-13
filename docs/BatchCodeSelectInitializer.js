class BatchCodeSelectInitializer {

    static initialize({batchCodeSelect, batchCodeDetails}) {
        batchCodeSelect.select2({ minimumInputLength: 4 });
        batchCodeSelect.on(
            'select2:select',
            function (event) {
                const batchcode = event.params.data.id;
                new HistogramView(batchCodeDetails).displayHistogramView(batchcode);
                GoogleAnalytics.click_batchcode(batchcode);
            });
        batchCodeSelect.select2('open');
    }
}
