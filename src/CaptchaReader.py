import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from PIL import Image
import numpy as np
import io

# copied from value of characters variable in captcha_ocr.ipynb or captcha_ocr_trainAndSaveModel.ipynb
characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f']

img_width = 241
img_height = 62

downsample_factor = 4

# copied from value of max_length variable in captcha_ocr.ipynb or captcha_ocr_trainAndSaveModel.ipynb
max_length = 6

char_to_num = layers.StringLookup(
    vocabulary=list(characters),
    mask_token=None)

num_to_char = layers.StringLookup(
    vocabulary=char_to_num.get_vocabulary(),
    mask_token=None, invert=True)

def encode_single_sample(img_path):
    # 1. Read image
    img = tf.io.read_file(img_path)
    # 2. Decode and convert to grayscale
    img = tf.io.decode_png(img, channels=1)
    # 3. Convert to float32 in [0, 1] range
    img = tf.image.convert_image_dtype(img, tf.float32)
    # 4. Resize to the desired size
    img = tf.image.resize(img, [img_height, img_width])
    # 5. Transpose the image because we want the time
    # dimension to correspond to the width of the image.
    img = tf.transpose(img, perm=[1, 0, 2])
    # 7. Return a dict as our model is expecting two inputs
    return asSingleSampleBatch(img)

def asSingleSampleBatch(img):
    array = keras.utils.img_to_array(img)
    array = np.expand_dims(array, axis=0)
    return array

def decode_batch_predictions(pred):
    input_len = np.ones(pred.shape[0]) * pred.shape[1]
    # Use greedy search. For complex tasks, you can use beam search
    results = keras.backend.ctc_decode(pred, input_length=input_len, greedy=True)[0][0][:, :max_length]
    # Iterate over the results and get back the text
    output_text = []
    for res in results:
        res = tf.strings.reduce_join(num_to_char(res)).numpy().decode("utf-8")
        output_text.append(res)
    return output_text

def _getModel():
    print("loading model...")
    model = load_model()
    model.summary()
    return model

def load_model():
    model = keras.models.load_model('model')
    return keras.models.Model(
        model.get_layer(name="image").input,
        model.get_layer(name="dense2").output)

def getTextInCaptchaImage(captchaImageFile):
    batchImages = encode_single_sample(captchaImageFile)
    preds = _getModel().predict(batchImages, use_multiprocessing=True)
    return decode_batch_predictions(preds)[0]
