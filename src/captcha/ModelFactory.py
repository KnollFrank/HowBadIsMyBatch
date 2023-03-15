from captcha.CTCLayer import CTCLayer
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


class ModelFactory:
    
    predictionModelInputLayerName = "image"
    predictionModelOutputLayerName = "dense2"

    def __init__(self, captchaShape, char_to_num):
        self.captchaShape = captchaShape
        self.char_to_num = char_to_num

    # see https://www.tensorflow.org/api_docs/python/tf/keras/applications/resnet/ResNet101
    def createResNet101(self):
        return self._createModel(
            baseModelFactory = lambda input_tensor: tf.keras.applications.resnet.ResNet101(
                input_tensor = input_tensor,
                weights = 'imagenet',
                include_top = False),
            preprocess_input = tf.keras.applications.resnet.preprocess_input,
            name = 'ResNet101')

    def createMobileNetV2(self):
        return self._createModel(
            baseModelFactory = lambda input_tensor: tf.keras.applications.MobileNetV2(
                input_tensor = input_tensor,
                weights = 'imagenet',
                include_top = False),
            preprocess_input = tf.keras.applications.mobilenet_v2.preprocess_input,
            name = 'MobileNetV2')

    def createMobileNetV3Small(self):
        return self._createModel(
            baseModelFactory = lambda input_tensor: tf.keras.applications.MobileNetV3Small(
                input_tensor = input_tensor,
                minimalistic = True,
                weights = 'imagenet',
                include_top = False),
            preprocess_input = tf.keras.applications.mobilenet_v3.preprocess_input,
            name = 'MobileNetV3Small')
            
    @staticmethod
    def createPredictionModel(model):
        return keras.models.Model(
            model.get_layer(name=ModelFactory.predictionModelInputLayerName).input,
            model.get_layer(name=ModelFactory.predictionModelOutputLayerName).output)

    def _createModel(self, baseModelFactory, preprocess_input, name):
        # Inputs to the model
        input_image = layers.Input(
            shape = (self.captchaShape.height, self.captchaShape.width, 3),
            name = ModelFactory.predictionModelInputLayerName,
            dtype = "float32")
        labels = layers.Input(name="label", shape=(None,), dtype="float32")
        
        image = preprocess_input(input_image)
        # Transpose the image because we want the time dimension to correspond to the width of the image.
        image = tf.keras.layers.Permute(dims=[2, 1, 3])(image)
        base_model = baseModelFactory(image)
        x = layers.Reshape(
            target_shape=(base_model.output_shape[1], base_model.output_shape[2] * base_model.output_shape[3]),
            name="reshape")(base_model.output)
        x = layers.Dense(64, activation="relu", name="dense1")(x)
        x = layers.Dropout(0.2)(x)

        # RNNs
        x = layers.Bidirectional(
            layers.LSTM(
                128,
                return_sequences=True,
                dropout=0.25,
                unroll=False,
                name="LSTM1"))(x)
        x = layers.Bidirectional(
            layers.LSTM(
                64,
                return_sequences=True,
                dropout=0.25,
                unroll=False,
                name="LSTM2"))(x)

        # Output layer
        x = layers.Dense(
            len(self.char_to_num.get_vocabulary()) + 1,
            activation="softmax",
            name=ModelFactory.predictionModelOutputLayerName)(x)

        # Add CTC layer for calculating CTC loss at each step
        output = CTCLayer(name="ctc_loss")(labels, x)

        model = keras.models.Model(
            inputs=[input_image, labels],
            outputs=output,
            name=name)
        # "The model is optimized by a stochastic gradient descent (SGD) strategy with an initial learning rate of 0.004, weight decay of 0.00004 and momentum of 0.9."
        # from tensorflow.keras.optimizers import SGD
        # model.compile(optimizer=SGD(learning_rate=0.004, "weight_decay=0.00004," momentum=0.9)
        model.compile(optimizer=keras.optimizers.Adam())
        return model
