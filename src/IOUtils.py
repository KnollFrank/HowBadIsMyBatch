import os
import json

class IOUtils:

    @staticmethod
    def saveDataFrame(dataFrame, file):
        # IOUtils.saveDataFrameAsExcelFile(dataFrame, file)
        # IOUtils.saveDataFrameAsHtml(dataFrame, file)
        IOUtils.saveDataFrameAsJson(dataFrame, file)

    @staticmethod
    def saveDataFrameAsExcelFile(dataFrame, file):
        IOUtils.ensurePath(file)
        dataFrame.to_excel(file + '.xlsx')

    @staticmethod
    def saveDataFrameAsHtml(dataFrame, file):
        IOUtils.ensurePath(file)
        dataFrame.to_html(
            file + '.html',
            index = False,
            table_id = 'batchCodeTable',
            classes = 'display',
            justify = 'unset',
            border = 0)

    @staticmethod
    def saveDataFrameAsJson(dataFrame, file):
        IOUtils.ensurePath(file)
        dataFrame.to_json(
            file + '.json',
            orient = "split",
            index = False)

    @staticmethod
    def saveDictAsJson(dict, file):
        IOUtils.ensurePath(file)
        with open(file, 'w') as outfile:
            json.dump(dict, outfile)

    @staticmethod
    def ensurePath(file):
        directory = os.path.dirname(file)
        if not os.path.exists(directory):
            os.makedirs(directory)
