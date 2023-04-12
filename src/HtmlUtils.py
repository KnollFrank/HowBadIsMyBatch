def getBatchcodes(batchCodeTable):
    return batchCodeTable['Batch'].dropna().unique()


def getBatchcodeOptions(batchcodes):
    return ['<option hidden disabled selected value>Select Batch</option>'] + _getBatchcodeOptions(batchcodes)


def _getBatchcodeOptions(batchcodes):
    return [_getBatchcodeOption(batchcode) for batchcode in batchcodes]


def _getBatchcodeOption(batchcode):
    return '<option value="{batchcode}">{batchcode}</option>'.format(batchcode=batchcode)
