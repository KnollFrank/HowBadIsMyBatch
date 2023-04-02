class GoogleAnalytics {

    static click_batchcode(batchcode) {
        gtag(
            'event',
            'click_batchcode',
            {
                'batchcode': batchcode
            });
    }

    static view_search_results(search_term) {
        gtag(
            'event',
            'view_search_results',
            {
                'search_term': search_term
            });
    }
}
