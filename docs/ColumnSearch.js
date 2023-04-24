// adapted from https://datatables.net/examples/api/multi_filter_select.html
class ColumnSearch {

    #column;
    #select;

    constructor(column) {
        this.#column = column;
        const self = this;
        $('<br/>').appendTo($(this.#column.header()));
        this.#select = $('<select></select>')
            .appendTo($(this.#column.header()))
            .on(
                'change',
                function () {
                    const val = $.fn.dataTable.util.escapeRegex($(this).val());
                    self.#column
                        .search(val ? '^' + val + '$' : '', true, false)
                        .draw();
                });
    }

    columnContentUpdated() {
        this.#select.empty();
        this.#select.append('<option value=""></option>');
        const self = this;
        this.#column
            .data()
            .unique()
            .sort()
            .each(function (d, _) {
                self.#select.append('<option value="' + d + '">' + d + '</option>');
            });
    }
}