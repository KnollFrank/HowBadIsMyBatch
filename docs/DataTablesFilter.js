class DataTablesFilter {

    static FilterState = Object.freeze({
        Enabled: Symbol("Enabled"),
        Disabled: Symbol("Disabled")
    })

    static setDataTablesFilter(filterState) {
        document.querySelector(".dataTables_filter").style.display = DataTablesFilter._getStyle(filterState);
    }

    static _getStyle(filterState) {
        switch (filterState) {
            case DataTablesFilter.FilterState.Enabled:
                return "block";
            case DataTablesFilter.FilterState.Disabled:
                return "none";
        }
    }

    static selectDataTablesFilter() {
        const input = document.querySelector(".dataTables_filter input");
        input.focus();
        input.select();
    }
}
