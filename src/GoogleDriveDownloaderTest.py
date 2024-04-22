import unittest
from pathlib import Path
import os
from IOUtils import IOUtils
from GoogleDriveDownloader import GoogleDriveDownloader


class GoogleDriveDownloaderTest(unittest.TestCase):

    def test_downloadIfNotYetDownloaded_notYetDownloaded(self):
        # Given
        remoteSrcFile = "https://drive.google.com/file/d/1LstnMvxW4LVxgNvfk5h4AnbvPktMeNSd/view?usp=drive_link"
        localDstFile = 'src/tmp/test.txt'
        IOUtils.silentlyRemoveFile(localDstFile)

        # When
        GoogleDriveDownloader.downloadIfNotYetDownloaded(remoteSrcFile, localDstFile)

        # Then
        self.assertEqual(Path(localDstFile).read_text(), 'test')

    def test_downloadIfNotYetDownloaded_alreadyDownloaded(self):
        # Given
        remoteSrcFile = "https://drive.google.com/file/d/1LstnMvxW4LVxgNvfk5h4AnbvPktMeNSd/view?usp=drive_link"
        localDstFile = 'src/tmp/test.txt'
        content = 'local file content'
        self._createFileWithContent(localDstFile, content);

        # When
        GoogleDriveDownloader.downloadIfNotYetDownloaded(remoteSrcFile, localDstFile)

        # Then
        self.assertEqual(Path(localDstFile).read_text(), content)

    def test_downloadSevenZipFileAndExtract(self):
        # Given
        remoteSevenZipSrcFile = "https://drive.google.com/file/d/14hFKlt48dzDnEjHS_7vYVca5elfzX0l1/view?usp=drive_link"
        localSevenZipDstFile = 'src/tmp/test.7z'
        localDstFolder = os.path.dirname(localSevenZipDstFile)
        IOUtils.silentlyRemoveFile(localSevenZipDstFile)
        IOUtils.silentlyRemoveFolder(localDstFolder + '/test')

        # When
        GoogleDriveDownloader.downloadSevenZipFileAndExtract(remoteSevenZipSrcFile, localSevenZipDstFile)

        # Then
        self.assertEqual(Path(localDstFolder + '/test/test.txt').read_text(), 'test')

    def _createFileWithContent(self, file, content):
        with open(file, 'w') as file:
            file.write(content)

