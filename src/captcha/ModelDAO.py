from tensorflow import keras
import shutil


class ModelDAO:

    def saveModel(self, model, modelFilepath):
        shutil.rmtree(modelFilepath, ignore_errors = True)
        model.save(modelFilepath)

    def loadModel(self, modelFilepath):
        return keras.models.load_model(modelFilepath)
