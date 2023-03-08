import os
import json

class IOUtils:

    @staticmethod
    def saveDataFrameAsExcelFile(dataFrame, file):
        IOUtils.ensurePath(file)
        dataFrame.to_excel(file)

    @staticmethod
    def saveDataFrameAsHtml(dataFrame, file):
        IOUtils.ensurePath(file)
        dataFrame.to_html(
            file,
            index = False,
            table_id = 'batchCodeTable',
            classes = 'display',
            justify = 'unset',
            border = 0)

    @staticmethod
    def saveDataFrameAsJson(dataFrame, file):
        IOUtils.ensurePath(file)
        dataFrame.to_json(
            file,
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
