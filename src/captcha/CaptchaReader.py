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
        self.modelFilepath = modelFilepath
        self.captchaShape = captchaShape

    def getTextInCaptchaImage(self, captchaImageFile):
        # FK-TODO: refactor
        modelDAO = ModelDAO(inColab = False)
        model = modelDAO.loadModel(self.modelFilepath)
        prediction_model = ModelFactory.createPredictionModel(model)
        charNumConverter = CharNumConverter(CaptchaGenerator.characters)
        datasetFactory = DatasetFactory(self.captchaShape,charNumConverter.char_to_num, batch_size = 64)
        batchImages = self._asSingleSampleBatch(datasetFactory._encode_single_sample(captchaImageFile, 'dummy')['image'])
        preds = prediction_model.predict(batchImages)
        predictionsDecoder = PredictionsDecoder(CaptchaGenerator.captchaLength, charNumConverter.num_to_char)
        pred_texts = predictionsDecoder.decode_batch_predictions(preds)
        return pred_texts[0]

    def _asSingleSampleBatch(self, img):
        array = keras.utils.img_to_array(img)
        array = np.expand_dims(array, axis=0)
        return array
