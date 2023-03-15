from pathlib import Path


class GoogleDriveManager:
  
  _googleDriveFolder = Path('/content/gdrive')
  _baseFolder = _googleDriveFolder / 'MyDrive/CAPTCHA/models/'

  @staticmethod
  def mount():
    from google.colab import drive
    drive.mount(str(GoogleDriveManager._googleDriveFolder))

  @staticmethod
  def uploadFolderToGoogleDrive(folder):
    pass
    # FK-FIXME:
    # !zip -r {folder}.zip {folder}/
    # !cp {folder}.zip {GoogleDriveManager._baseFolder}

  @staticmethod
  def downloadFolderFromGoogleDrive(folder):
    pass
    # FK-FIXME:
    # !cp {GoogleDriveManager._baseFolder}/{folder}.zip .
    # !rm -rf {folder}
    # !unzip {folder}.zip
