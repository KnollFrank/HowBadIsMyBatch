import tensorflow as tf


class DatasetFactory:
    
    def __init__(self, img_height, img_width, char_to_num, batch_size):
        self.img_height = img_height
        self.img_width = img_width
        self.char_to_num = char_to_num
        self.batch_size = batch_size

    def createDataset(self, x, y):
        dataset = tf.data.Dataset.from_tensor_slices((x, y))
        dataset = dataset.map(self._encode_single_sample, num_parallel_calls=tf.data.AUTOTUNE)
        dataset = dataset.batch(self.batch_size).prefetch(buffer_size=tf.data.AUTOTUNE)
        return dataset

    def _encode_single_sample(self, img_path, label):
        img = tf.io.read_file(img_path)
        img = tf.io.decode_jpeg(img, channels=3)
        img = tf.image.resize(img, [self.img_height, self.img_width])
        # Map the characters in label to numbers
        label = self.char_to_num(tf.strings.unicode_split(label, input_encoding="UTF-8"))
        # Return a dict as our model is expecting two inputs
        return {"image": img, "label": label}
