__author__ = 'Ted'

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
        self.resize(1900, 900)  # 设置下尺寸
        self.plotWidget_ted = pg.PlotWidget(self, title='Current')  # 添加 PlotWidget 控件
        self.plotWidget_ted.setGeometry(QtCore.QRect(50, 50, 1800, 800))  # 设置该控件尺寸和相对位置
        self.plotWidget_ted.showGrid(x=True, y=True)

        # self.data = np.random.normal(size=300)                         # 生成 300 个正态分布的随机数
        self.time, self.data1 = self.get_data()
        # self.data1 = self.data1[:]
        self.length = 2000
        self.data = self.data1[:self.length]

        self.curve = self.plotWidget_ted.plot(self.data1, name="mode2")
        self.ptr = 0

        self.timer = pg.QtCore.QTimer()  # 设定定时器
        self.timer.timeout.connect(self.update_data)  # 定时器信号绑定 update_data 函数
        self.timer.start(1)  # 1ms 刷新一次数据

    @staticmethod
    def get_data():
        file_path = '../input/Voltage_without_spritzern.txt'
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

    def update_data(self):
        """ 数据左移 """
        self.data[:-1] = self.data[1:]
        self.data[-1] = self.data1[self.length:][self.ptr]
        self.curve.setData(self.data)  # 数据填充到绘制曲线中
        self.ptr += 1  # x 轴记录点
        # self.find_extreme_value(self.data, self.ptr)
        self.curve.setPos(self.ptr, 0)  # 重新设定 x 相关的坐标原点


if __name__ == '__main__':
    app = QApplication(sys.argv)  # PyQt5 程序固定写法
    window = Window()  # 将绑定了绘图控件的窗口实例化并展示
    window.show()
    sys.exit(app.exec())  # PyQt5 程序固定写法
