from captcha.ModelDAO import ModelDAO
from captcha.ModelFactory import ModelFactory
from captcha.PredictionsDecoder import PredictionsDecoder
from captcha.CaptchaGenerator import CaptchaGenerator
from captcha.CharNumConverter import CharNumConverter
from captcha.DatasetFactory import DatasetFactory
import numpy as np
from tensorflow import keras


class CaptchaReader:

    def __init__(self, modelFilepath, captchaShape):
        self.captchaShape = captchaShape
        self.predictionModel = self._createPredictionModel(modelFilepath)

    def getTextInCaptchaImage(self, captchaImageFile):
        return self._getTextsInCaptchaImage(self._getCaptchaImage(captchaImageFile))[0]

    def _getCaptchaImage(self, captchaImageFile):
        return self._asSingleSampleBatch(DatasetFactory.encodeImage(captchaImageFile, self.captchaShape))

    def _asSingleSampleBatch(self, img):
        return np.expand_dims(keras.utils.img_to_array(img), axis=0)

    def _getTextsInCaptchaImage(self, captchaImage):
        preds = self.predictionModel.predict(captchaImage)
        return PredictionsDecoder(CaptchaGenerator.captchaLength, CharNumConverter(CaptchaGenerator.characters).num_to_char).decode_batch_predictions(preds)

    def _createPredictionModel(self,modelFilepath):
        return ModelFactory.createPredictionModel(ModelDAO().loadModel(modelFilepath))
