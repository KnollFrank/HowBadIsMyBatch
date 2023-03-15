import tensorflow as tf


class DatasetFactory:
    
    def __init__(self, captchaShape, char_to_num, batch_size):
        self.captchaShape = captchaShape
        self.char_to_num = char_to_num
        self.batch_size = batch_size

    def createDataset(self, x, y):
        dataset = tf.data.Dataset.from_tensor_slices((x, y))
        dataset = dataset.map(self._encodeImageAndLabel, num_parallel_calls=tf.data.AUTOTUNE)
        dataset = dataset.batch(self.batch_size).prefetch(buffer_size=tf.data.AUTOTUNE)
        return dataset

    def _encodeImageAndLabel(self, imageFilename, label):
        return {
            "image": DatasetFactory.encodeImage(imageFilename, self.captchaShape),
            "label": self.char_to_num(tf.strings.unicode_split(label, input_encoding="UTF-8"))}
    
    @staticmethod
    def encodeImage(imageFilename, captchaShape):
        img = tf.io.read_file(imageFilename)
        img = tf.io.decode_jpeg(img, channels=3)
        img = tf.image.resize(img, [captchaShape.height, captchaShape.width])
        return img
