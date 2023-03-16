from tensorflow import keras
import shutil


class ModelDAO:

    def saveModel(self, model):
        shutil.rmtree(model.name, ignore_errors = True)
        model.save(model.name)

    def loadModel(self, modelFilepath):
        return keras.models.load_model(modelFilepath)
