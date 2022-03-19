import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import load_model
import random


def create_data():
    dataset = [i**2 for i in range(-100, 100)]
    return dataset


def evaluate(model, x_test):
    print('=============== evaluate ===============')
    y_test = [1, 0, 0, 1, 1, 0, 0, 0]
    y_test = np.array(y_test)
    loss, acc = model.evaluate(x_test, y_test)
    print('loss', loss)
    print('accuracy:', acc)


def predict(model):
    print('=============== predict ===============')
    x_test = [[1, 2, 3, 5], [1, 2, 3, 6], [3, 5, 2, 1]]
    x_test = np.array(x_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    res = model.predict(x_test)
    print('predict:\n', res)
    return x_test


def train():
    print('=============== train ===============')
    x = [[1, 2, 3, 4], [1, 1, 3, 4], [1, 3, 3, 4], [1, 2, 3, 2], [1, 2, 3, 4]]  # 特征
    y = [1, 0, 0, 0, 1]
    # for elm in x:
    #     if elm == [0, 1, 2, 3, 4, 3, 2, 1]:
    #         y.append(1)
    #     else:
    #         y.append(0)
    # print(y[:20])
    x = np.array(x)
    y_train = np.array(y)
    x_train = np.reshape(x, (x.shape[0], x.shape[1], 1))  # Lstm调用库函数必须要进行维度转换
    model = Sequential()
    model.add(LSTM(100, input_shape=(x_train.shape[1], x_train.shape[2]), return_sequences=True))
    model.add(LSTM(20, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(1))
    model.add(Activation('linear'))
    model.compile(loss="mse", optimizer="rmsprop", metrics=['acc'])
    model.fit(x_train, y_train, epochs=100, batch_size=1)  # 参数依次为特征，标签，训练循环次数，小批量（一次放入训练的数据个数）
    model.save('output/current_without_zundfehler.h5')
    return model


def run():
    model = train()
    # model = load_model('output/current_without_zundfehler.h5')
    x_test = predict(model)
    evaluate(model, x_test)


run()

