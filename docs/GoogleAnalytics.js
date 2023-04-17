class GoogleAnalytics {

    static click_batchcode(batchcode) {
        gtag(
            'event',
            'click_batchcode',
            {
                'batchcode': batchcode
            });
    }
}
