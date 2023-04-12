def getBatchcodes(batchCodeTable):
    return batchCodeTable['Batch'].dropna().unique()


def getBatchcodeOptions(batchcodes):
    return [_getBatchcodeOption(batchcode) for batchcode in batchcodes]


def _getBatchcodeOption(batchcode):
    return '<option value="{batchcode}">{batchcode}</option>'.format(batchcode=batchcode)
