from tensorflow.keras.datasets import mnist
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

class n_net:
    # Импорт датасета
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()

    # Созданание модели сети
    model = keras.Sequential([layers.Dense(512, activation="relu"), layers.Dense(10, activation="softmax")])
    test_data = test_images

    # Параметры модели сети
    model.compile(optimizer="rmsprop",
                  loss="sparse_categorical_crossentropy",
                  metrics=["accuracy"])

    # Стандартизация данных
    train_images = train_images.reshape((60000, 28 * 28))
    train_images = train_images.astype('float32') / 256
    test_images = test_images.reshape((10000, 28 * 28))
    test_images = test_images.astype('float32') / 256

    # Обычение модели
    model.fit(train_images, train_labels, epochs=10, batch_size=128)

    def test(self):
        self.test_digits = self.test_images[0:10]
        predictions = self.model.predict(self.test_digits)
        [print(i, round(predictions[3][i], 3)) for i in range(10)]


    def result(self, array):
        s = np.zeros((28, 28))
        array = list(reversed(array))
        for i in range(28):
            for j in range(28):
                s[i][j] = array[27 - j][i]
        array = s
        array = array.reshape((1, 28 * 28))
        array = array.astype('float32')
        predictions = self.model.predict(array)
        return predictions