# -*- coding: utf-8 -*-
import os
import time
from functools import reduce
import array
import threading
import pandas as pd
from kafka import KafkaConsumer
import sys
from PyQt5.Qt import *
from PyQt5 import QtCore
import numpy as np
import pyqtgraph as pg

from pyqt_demo.ui_mainWindow import Ui_MainWindow


class PlotData:

    def __init__(self):
        self.consumer_current = KafkaConsumer("Current", bootstrap_servers=["localhost:9092"], auto_offset_reset='latest',
                                              consumer_timeout_ms=6000)
        self.consumer_voltage = KafkaConsumer("Voltage", bootstrap_servers=["localhost:9092"], auto_offset_reset='latest',
                                              consumer_timeout_ms=6000)
        self.length = 300  # 横坐标长度
        self.ptr = 0
        self.t = ''
        self.output_path = 'output'

        self.value_voltage = None
        self.value_current = None

        self.data_current = array.array('i')
        self.data_current = np.zeros(self.length).__array__('d')  # 把数组长度定下来
        self.data_voltage = array.array('i')
        self.data_voltage = np.zeros(self.length).__array__('d')  # 把数组长度定下来
        self.number = [0] * self.length
        self.t = ['0'] * self.length

        self.curve_current = Ui_MainWindow().plotWidget_test.plot(self.data_current, name="mode2")
        self.curve_voltage = Ui_MainWindow().plotWidget_test.plot(self.data_voltage, name="mode2")

        self.timer_current = pg.QtCore.QTimer()  # 设定定时器
        self.timer_current.timeout.connect(self.update_data_current)  # 定时器信号绑定 update_data 函数
        self.timer_current.start(1)  # 1ms 刷新一次数据

        self.timer_voltage = pg.QtCore.QTimer()  # 设定定时器
        self.timer_voltage.timeout.connect(self.update_data_voltage)  # 定时器信号绑定 update_data 函数
        self.timer_voltage.start(1)  # 1ms 刷新一次数据

    def write_to_csv(self, num, send_time, value, file_name):
        dataframe = pd.DataFrame({'no.': num, 'send_time': send_time, 'value': value})
        zeit = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        output_file_name = file_name + '_' + zeit + '.csv'
        dataframe.to_csv(os.path.join(self.output_path, output_file_name), index=False, sep=',')
        # print('\n[INFO] .csv file be created: ', output_file_name)

    def get_data_current(self):
        num, send_time, value = [], [], []
        for msg in self.consumer_current:
            self.value_current = msg.value.decode('utf8').split('&')
            # 序号、时间、值
            self.value_current[0] = int(self.value_current[0])
            self.value_current[-1] = float(self.value_current[-1])

            num.append(self.value_current[0])
            send_time.append(self.value_current[1])
            value.append(self.value_current[2])

            if self.value_current[0] % 1000000 == 0 and self.value_current[0] != 0:
                self.write_to_csv(num, send_time, value, 'Current')
                num, send_time, value = [], [], []

            if len(self.data_current) < self.length:
                self.number.append(self.value_current[0])
                self.t.append(self.value_current[1])
                self.data_current.append(self.value_current[-1])
            else:
                self.data_current[:-1] = self.data_current[1:]
                self.data_current[-1] = self.value_current[-1]

                self.number[:-1] = self.number[1:]
                self.number[-1] = self.value_current[0]

                self.t[:-1] = self.t[1:]
                self.t[-1] = self.value_current[1]
        self.write_to_csv(num, send_time, value, 'Current')

    def get_data_voltage(self):
        num, send_time, value = [], [], []
        for msg in self.consumer_voltage:
            self.value_voltage = msg.value.decode('utf8').split('&')
            self.value_voltage[-1] = float(self.value_voltage[-1])

            count = int(self.value_voltage[0])
            num.append(self.value_voltage[0])
            send_time.append(self.value_voltage[1])
            value.append(self.value_voltage[2])

            if count % 1000000 == 0 and count != 0:
                self.write_to_csv(num, send_time, value, 'Voltage')
                num, send_time, value = [], [], []

            if len(self.data_voltage) < self.length:
                self.data_voltage.append(self.value_voltage[-1])
            else:
                self.data_voltage[:-1] = self.data_voltage[1:]
                self.data_voltage[-1] = self.value_voltage[-1]
        self.write_to_csv(num, send_time, value, 'Voltage')

    @staticmethod
    def calc_energy(lt):
        return reduce(lambda x, y: x + y, map(lambda x: x ** 2, lt))

    def find_extreme_value(self, data, flag):
        if self.ptr % 200 == 0:
            max_idx, min_idx = np.argmax(data), np.argmin(data)
            max_value, min_value = data[max_idx], data[min_idx]
            energy = self.calc_energy(data)
            print('[INFO] time(%s): %-8s - %s - energy: %d' % (flag, self.t[-1], self.number[-1], energy))
            print('[INFO] \tmin_time: %-6s - min_value: %-8.3f  max_time:%-6s - max_value: %.3f'
                  % (self.number[min_idx], min_value, self.number[max_idx], max_value))
            # print(self.t[min_idx], self.t[max_idx])
            print('='*70)

    def update_data_voltage(self):
        """ 数据左移 """
        if self.value_voltage is not None:
            self.curve_voltage.setData(self.data_voltage)  # 数据填充到绘制曲线中
            self.find_extreme_value(self.data_voltage, flag='Voltage')
            self.curve_voltage.setPos(self.ptr, 0)  # 重新设定 x 相关的坐标原点

    def update_data_current(self):
        """ 数据左移 """
        if self.value_current is not None:
            self.curve_current.setData(self.data_current)  # 数据填充到绘制曲线中
            self.ptr = self.value_current[0]  # x 轴记录点
            self.find_extreme_value(self.data_current, flag='Current')
            self.curve_current.setPos(self.ptr, 0)  # 重新设定 x 相关的坐标原点
