from captcha.ModelDAO import ModelDAO
from captcha.ModelFactory import ModelFactory
from captcha.PredictionsDecoder import PredictionsDecoder
from captcha.CaptchaGenerator import CaptchaGenerator
from captcha.CharNumConverter import CharNumConverter
from captcha.DatasetFactory import DatasetFactory
import numpy as np
from tensorflow import keras

# FK-TODO: DRY with captcha.ipynb
img_width = 241
img_height = 62

class CaptchaReader:

    def __init__(self, modelFilepath):
        self.modelFilepath = modelFilepath

    def getTextInCaptchaImage(self, captchaImageFile):
        modelDAO = ModelDAO(inColab = False)
        model = modelDAO.loadModel(self.modelFilepath)
        prediction_model = ModelFactory.createPredictionModel(model)
        charNumConverter = CharNumConverter(CaptchaGenerator.characters)
        datasetFactory = DatasetFactory(img_height, img_width, charNumConverter.char_to_num, batch_size = 64)
        batchImages = self._asSingleSampleBatch(datasetFactory._encode_single_sample(captchaImageFile, 'dummy')['image'])
        preds = prediction_model.predict(batchImages)
        predictionsDecoder = PredictionsDecoder(CaptchaGenerator.captchaLength, charNumConverter.num_to_char)
        pred_texts = predictionsDecoder.decode_batch_predictions(preds)
        return pred_texts[0]

    def _asSingleSampleBatch(self, img):
        array = keras.utils.img_to_array(img)
        array = np.expand_dims(array, axis=0)
        return array
