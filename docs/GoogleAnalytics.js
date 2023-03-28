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

    static countrySelected(country) {
        gtag("event",
            "select_item",
            {
                item_list_id: "countrySelect",
                items: [
                    {
                        item_id: country,
                    }
                ]
            });
    }
}
