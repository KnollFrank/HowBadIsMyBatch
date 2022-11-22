import zipfile
import os


def unzip(zipFile, dstDir):
    with zipfile.ZipFile(zipFile, 'r') as zip_ref:
        zip_ref.extractall(dstDir)


def unzipAndRemove(zipFile, dstDir):
    unzip(zipFile, dstDir)
    os.remove(zipFile)
