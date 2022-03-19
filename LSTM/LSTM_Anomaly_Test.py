import threading

from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
from scipy.ndimage import gaussian_filter1d
from scipy.signal import medfilt
from functools import reduce
import sys
from PyQt5.Qt import *
from PyQt5 import QtCore
import numpy as np
import pyqtgraph as pg




class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("IAT_Project")
        self.resize(1500, 700)  # 设置下尺寸
        self.plotWidget = pg.PlotWidget(self, title='Current')  # 添加 PlotWidget 控件
        self.plotWidget.setGeometry(QtCore.QRect(50, 50, 1000, 600))  # 设置该控件尺寸和相对位置
        self.plotWidget.showGrid(x=True, y=True)

        self.model = load_model('input/model/current_without_zundfehler.h5')
        self.time, self.data1 = self.get_data()
        # self.data1 = self.data1[:]
        self.length = 1000
        self.data = self.data1[:self.length]

        self.curve = self.plotWidget.plot(self.data1, name="mode2")
        self.ptr = 0

        self.timer = pg.QtCore.QTimer()  # 设定定时器
        self.timer.timeout.connect(self.update_data)  # 定时器信号绑定 update_data 函数
        self.timer.start(1)  # 1ms 刷新一次数据

    @staticmethod
    def get_data():
        # file_path = r'E:\Huayu\Study\Master\TU_Berlin\2.Semester\IAT_Projekt_06_WS_2122\git\iat-project\input\Datensätze\Kamerasystem 2\V2-Baustahl\Prozessdaten\Current.txt'
        file_path = '../input/Current_without_zundfehler.txt'
        with open(file_path, 'r') as f:
            time, value = [], []
            for idx, line in enumerate(f.readlines()):
                line = line.strip().split()
                time.append(float(line[0]))
                value.append(float(line[1]))
        return time, value

    @staticmethod
    def calc_energy(lt):
        return reduce(lambda x, y: x + y, map(lambda x: x ** 2, lt))

    def find_extreme_value(self, data, ptr):
        if self.ptr % 100 == 0:
            max_idx, min_idx = np.argmax(data), np.argmin(data)
            max_value, min_value = data[max_idx], data[min_idx]
            energy = self.calc_energy(data)
            print('[INFO] time(s): %-8.5f - %d - energy: %d'
                  '\n\t\ttime_min: %-10.5s local min_values: %.2f'
                  '\n\t\ttime_max: %-10.5s local max_values: %.2f'
                  % (self.time[self.length + ptr], ptr, energy, self.time[:self.length + ptr][-(self.length - min_idx)],
                      min_value, self.time[:self.length + ptr][-(self.length - max_idx)], max_value))

    def anomaly_detection(self):
        while True:
            print(self.ptr)
            if self.ptr % 500 == 0:
                print(self.self.data)
                true_data = data_streaming[-1]
                data_streaming = np.array(data_streaming[-11:-1]).reshape(-1, 1)
                dim1, dim2 = data_streaming.shape
                print(data_streaming.shape)
                threshold = 10

                data_streaming = medfilt(data_streaming, 3)
                data_streaming = gaussian_filter1d(data_streaming, 1.2)

                sc = MinMaxScaler(feature_range=(0, 1))
                data_streaming_scaled = sc.fit_transform(data_streaming)

                tmp = []
                seq_x = data_streaming_scaled[:]
                tmp.append(seq_x)
                data_streaming_scaled = np.array(tmp)
                print("data_streaming_scaled.shape", data_streaming_scaled.shape)


                # Get predicted data
                y_predicted = self.model.predict(data_streaming_scaled)
                # 'De-normalize' the data
                y_predicted_descaled = sc.inverse_transform(y_predicted)
                y_test_descaled = sc.inverse_transform(true_data)

                residual = y_test_descaled - y_predicted_descaled
                if residual >= threshold:
                    print(self.time[self.length + ptr])

    def update_data(self):
        """ 数据左移 """
        self.data[:-1] = self.data[1:]
        self.data[-1] = self.data1[self.length:][self.ptr]
        self.curve.setData(self.data)  # 数据填充到绘制曲线中
        self.ptr += 1  # x 轴记录点
        # self.find_extreme_value(self.data, self.ptr)
        self.curve.setPos(self.ptr, 0)  # 重新设定 x 相关的坐标原点


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    th1 = threading.Thread(target=Window.anomaly_detection)
    th1.start()
    sys.exit(app.exec())
