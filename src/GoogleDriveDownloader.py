import gdown
import py7zr
import os


class GoogleDriveDownloader:

    @staticmethod
    def downloadIfNotYetDownloaded(remoteSrcFile, localDstFile):
        if not os.path.exists(localDstFile):
            gdown.download(url = remoteSrcFile, output = localDstFile, fuzzy = True)

    @staticmethod
    def downloadSevenZipFileAndExtract(remoteSevenZipSrcFile, localSevenZipDstFile):
        GoogleDriveDownloader.downloadIfNotYetDownloaded(remoteSevenZipSrcFile, localSevenZipDstFile);
        with py7zr.SevenZipFile(localSevenZipDstFile, mode='r') as sevenZipFile:
            sevenZipFile.extractall(path = os.path.dirname(localSevenZipDstFile))