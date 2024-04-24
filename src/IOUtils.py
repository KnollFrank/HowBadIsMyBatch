import os
from pathlib import Path
import shutil
import simplejson as json


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
            index=False,
            table_id='batchCodeTable',
            classes='display',
            justify='unset',
            border=0)

    @staticmethod
    def saveDataFrameAsJson(dataFrame, file):
        IOUtils.ensurePath(file)
        dataFrame.to_json(
            file,
            orient="split",
            index=False)

    @staticmethod
    def saveDictAsJson(dict, file):
        IOUtils.ensurePath(file)
        with open(file, 'w') as outfile:
            json.dump(dict, outfile, ignore_nan=True, sort_keys=True)

    @staticmethod
    def ensurePath(file):
        directory = os.path.dirname(file)
        if not os.path.exists(directory):
            os.makedirs(directory)

    @staticmethod
    def silentlyRemoveFile(file):
        Path(file).unlink(missing_ok=True)

    @staticmethod
    def silentlyRemoveFolder(folder):
        shutil.rmtree(folder, ignore_errors=True)
