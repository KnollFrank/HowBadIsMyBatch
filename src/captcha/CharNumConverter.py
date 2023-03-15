from tensorflow.keras import layers

class CharNumConverter:

    def __init__(self, characters):
        self.char_to_num = layers.StringLookup(vocabulary=list(characters), mask_token=None)
        self.num_to_char = layers.StringLookup(
            vocabulary=self.char_to_num.get_vocabulary(),
            mask_token=None,
            invert=True)