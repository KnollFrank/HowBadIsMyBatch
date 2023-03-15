import tensorflow as tf
from tensorflow import keras
import numpy as np


class PredictionsDecoder:

    def __init__(self, captchaLength, num_to_char):
        self.captchaLength = captchaLength
        self.num_to_char = num_to_char

    def decode_batch_predictions(self, pred):
        return self.asStrings(self.ctc_decode(pred))

    def ctc_decode(self, pred):
        input_len = np.ones(pred.shape[0]) * pred.shape[1]
        # Use greedy search. For complex tasks, you can use beam search
        return keras.backend.ctc_decode(pred, input_length=input_len, greedy=True)[0][0][:, :self.captchaLength]

    def asStrings(self, labels):
        return [self.asString(label) for label in labels]

    def asString(self, label):
        return tf.strings.reduce_join(self.num_to_char(label)).numpy().decode("utf-8")
