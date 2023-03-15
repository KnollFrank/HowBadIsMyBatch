from tensorflow import keras
from captcha.GoogleDriveManager import GoogleDriveManager
import shutil


class ModelDAO:

    def __init__(self, inColab):
        self.inColab = inColab

    def saveModel(self, model):
        shutil.rmtree(model.name, ignore_errors = True)
        model.save(model.name)
        if self.inColab:
            GoogleDriveManager.uploadFolderToGoogleDrive(model.name)

    def loadModel(self, modelFilepath):
        if self.inColab:
            GoogleDriveManager.downloadFolderFromGoogleDrive(modelFilepath)
        return keras.models.load_model(modelFilepath)
