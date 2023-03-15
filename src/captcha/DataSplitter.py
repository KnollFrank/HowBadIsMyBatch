import numpy as np


class DataSplitter:

    def __init__(self, x, y):
        (self.x_train, self.y_train), (x_valid_test, y_valid_test) = DataSplitter._splitData(np.array(x), np.array(y), train_size=0.7)
        (self.x_valid, self.y_valid), (self.x_test, self.y_test) = DataSplitter._splitData(x_valid_test, y_valid_test, train_size=0.5)

    def getTrain(self):
        return (self.x_train, self.y_train)

    def getValid(self):
        return (self.x_valid, self.y_valid)

    def getTest(self):
        return (self.x_test, self.y_test)

    @staticmethod
    def _splitData(x, y, train_size=0.9, shuffle=True):
        size = len(x)
        indices = np.arange(size)
        if shuffle:
            np.random.shuffle(indices)
        train_samples = int(size * train_size)
        x_train, y_train = x[indices[:train_samples]], y[indices[:train_samples]]
        x_test, y_test = x[indices[train_samples:]], y[indices[train_samples:]]
        return (x_train, y_train), (x_test, y_test)
