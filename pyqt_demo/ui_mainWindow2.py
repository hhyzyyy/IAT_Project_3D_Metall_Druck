# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib import pyplot as plt
from pyqtgraph import PlotWidget
import os
import time
from functools import reduce
import array
import pandas as pd
from kafka import KafkaConsumer
from PyQt5 import QtCore
import numpy as np
import pyqtgraph as pg
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
from scipy.ndimage import gaussian_filter1d
from scipy.signal import medfilt


class Ui_MainWindow(object):
    def __init__(self):
        self.value_voltage = None
        self.value_current = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1125, 771)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.plotWidget_test = PlotWidget(self.groupBox_2)
        self.plotWidget_test.setObjectName("plotWidget_test")
        self.verticalLayout_3.addWidget(self.plotWidget_test)
        self.plotWidget_test2 = PlotWidget(self.groupBox_2)
        self.plotWidget_test2.setObjectName("plotWidget_test2")
        self.verticalLayout_3.addWidget(self.plotWidget_test2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.horizontalLayout_6.addWidget(self.textBrowser_11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.horizontalLayout_3.addWidget(self.textBrowser_5)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.horizontalLayout_3.addWidget(self.textBrowser_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_16.addWidget(self.label_8)
        self.textBrowser_13 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.horizontalLayout_16.addWidget(self.textBrowser_13)
        self.textBrowser_14 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_14.setObjectName("textBrowser_14")
        self.horizontalLayout_16.addWidget(self.textBrowser_14)
        self.verticalLayout_2.addLayout(self.horizontalLayout_16)
        spacerItem = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 9)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        self.horizontalLayout_7.setStretch(0, 7)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.plotWidget_test3 = PlotWidget(self.groupBox_3)
        self.plotWidget_test3.setObjectName("plotWidget_test3")
        self.verticalLayout_7.addWidget(self.plotWidget_test3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_5)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_17.addWidget(self.label_9)
        self.textBrowser_12 = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.horizontalLayout_17.addWidget(self.textBrowser_12)
        self.verticalLayout_8.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_18.addWidget(self.label_10)
        self.textBrowser_15 = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_15.setObjectName("textBrowser_15")
        self.horizontalLayout_18.addWidget(self.textBrowser_15)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.horizontalLayout_18.addWidget(self.textBrowser_4)
        self.verticalLayout_8.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_19.addWidget(self.label_11)
        self.textBrowser_16 = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_16.setObjectName("textBrowser_16")
        self.horizontalLayout_19.addWidget(self.textBrowser_16)
        self.textBrowser_17 = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_17.setObjectName("textBrowser_17")
        self.horizontalLayout_19.addWidget(self.textBrowser_17)
        self.verticalLayout_8.addLayout(self.horizontalLayout_19)
        spacerItem1 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem1)
        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 1)
        self.verticalLayout_8.setStretch(2, 1)
        self.verticalLayout_8.setStretch(3, 7)
        self.horizontalLayout_15.addLayout(self.verticalLayout_8)
        self.horizontalLayout_15.setStretch(0, 7)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.horizontalLayout.setStretch(0, 9)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1125, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.run_signal)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Signalverarbeitung"))
        self.label_7.setText(_translate("MainWindow", "Energie: "))
        self.label_3.setText(_translate("MainWindow", "Lokales Maximum: "))
        self.label_8.setText(_translate("MainWindow", "Lokales Minimum: "))
        self.groupBox_3.setTitle(_translate("MainWindow", "Bildverarbeitung"))
        self.label_9.setText(_translate("MainWindow", "xxx"))
        self.label_10.setText(_translate("MainWindow", "xxxx"))
        self.label_11.setText(_translate("MainWindow", "xxxxx"))
        self.pushButton_3.setText(_translate("MainWindow", "Start Bild"))
        self.pushButton.setText(_translate("MainWindow", "Start Signal"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancel"))

    def run_signal(self):
        self.consumer_current = KafkaConsumer("Current", bootstrap_servers=["localhost:9092"],
                                              auto_offset_reset='latest',
                                              consumer_timeout_ms=6000)
        self.consumer_voltage = KafkaConsumer("Voltage", bootstrap_servers=["localhost:9092"],
                                              auto_offset_reset='latest',
                                              consumer_timeout_ms=6000)
        self.model = load_model('../LSTM/input/model/current_without_zundfehler.h5')
        self.length = 1500  # 横坐标长度
        self.ptr = 0
        self.t = []
        self.output_path = 'output'

        self.data_current = array.array('i')
        self.data_current = np.zeros(self.length).__array__('d')  # 把数组长度定下来
        self.data_voltage = array.array('i')
        self.data_voltage = np.zeros(self.length).__array__('d')  # 把数组长度定下来
        self.number = [0] * self.length
        self.t = ['0'] * self.length

        self.curve_current = self.plotWidget_test.plot(self.data_current, name="mode2")
        self.curve_voltage = self.plotWidget_test2.plot(self.data_voltage, name="mode2")
        self.curve_zundfehler = self.plotWidget_test3.plot(self.data_voltage, name="mode2")

        self.timer_current = pg.QtCore.QTimer()  # 设定定时器
        self.timer_current.timeout.connect(self.update_data_current)  # 定时器信号绑定 update_data 函数
        self.timer_current.start(1)  # 1ms 刷新一次数据

        self.timer_voltage = pg.QtCore.QTimer()  # 设定定时器
        self.timer_voltage.timeout.connect(self.update_data_voltage)  # 定时器信号绑定 update_data 函数
        self.timer_voltage.start(1)  # 1ms 刷新一次数据

        self.timer_zundfehler = pg.QtCore.QTimer()  # 设定定时器
        self.timer_zundfehler.timeout.connect(self.zundfehler_detection)  # 定时器信号绑定 update_data 函数
        self.timer_zundfehler.start(1)  # 1ms 刷新一次数据

        th1 = threading.Thread(target=self.get_data_current)
        th1.start()
        th2 = threading.Thread(target=self.get_data_voltage)
        th2.start()
        # th3 = threading.Thread(target=self.zundfehler_detection)
        # th3.start()

    def write_to_csv(self, num, send_time, value, file_name):
        dataframe = pd.DataFrame({'no.': num, 'send_time': send_time, 'value': value})
        zeit = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        output_file_name = file_name + '_' + zeit + '.csv'
        dataframe.to_csv(os.path.join(self.output_path, output_file_name), index=False, sep=',')
        # print('\n[INFO] .csv file be created: ', output_file_name)

    @staticmethod
    def data_split(sequence, n_timestamp):
        X, y = [], []
        for i in range(len(sequence)):
            end_ix = i + n_timestamp
            if end_ix > len(sequence) - 1:
                break
            seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
            X.append(seq_x)
            y.append(seq_y)
        return np.array(X), np.array(y)

    def zundfehler_detection_thread(self):
        ptr = self.ptr

        ser = pd.Series(self.data_current[-1000:])
        ser = medfilt(ser, 3)
        ser = gaussian_filter1d(ser, 1.2).reshape(-1, 1)

        sc = MinMaxScaler(feature_range=(0, 1))
        data_streaming_scaled = sc.fit_transform(ser)
        x, y = self.data_split(data_streaming_scaled, 10)
        x = x.reshape(x.shape[0], x.shape[1], 1)

        y_predicted = self.model.predict(x)
        # 'De-normalize' the data
        y_predicted_descaled = sc.inverse_transform(y_predicted)
        y_test_descaled = sc.inverse_transform(y)

        residual = y_test_descaled - y_predicted_descaled
        residual = np.squeeze(residual)
        idx = np.argmax(residual)
        print("residual: ", ptr + idx, residual[idx])
        self.curve_zundfehler.setData(residual)

    def zundfehler_detection(self):
        if self.ptr % 800 == 0:
            th = threading.Thread(target=self.zundfehler_detection_thread)
            th.start()

    def get_data_current(self):
        for msg in self.consumer_current:
            value_current = msg.value.decode('utf8').split('&')
            # 序号、时间、值
            self.ptr = int(value_current[0])
            value = float(value_current[-1])

            # if self.value_current[0] % 1000000 == 0 and self.value_current[0] != 0:
            #     self.write_to_csv(num, send_time, value, 'Current')
            #     num, send_time, value = [], [], []

            if len(self.data_current) < self.length:
                self.number.append(self.ptr)
                self.t.append(value_current[1])
                self.data_current.append(value)
            else:
                self.data_current[:-1] = self.data_current[1:]
                self.data_current[-1] = value

                self.number[:-1] = self.number[1:]
                self.number[-1] = self.ptr

                self.t[:-1] = self.t[1:]
                self.t[-1] = value_current[1]
        # self.write_to_csv(num, send_time, value, 'Current')

    def get_data_voltage(self):
        for msg in self.consumer_voltage:
            value_voltage = msg.value.decode('utf8').split('&')
            value = float(value_voltage[-1])

            if len(self.data_voltage) < self.length:
                self.data_voltage.append(value)
            else:
                self.data_voltage[:-1] = self.data_voltage[1:]
                self.data_voltage[-1] = value

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
            print('=' * 70)

    def update_data_voltage(self):
        """ 数据左移 """
        if self.data_voltage is not None:
            self.curve_voltage.setData(self.data_voltage)  # 数据填充到绘制曲线中
            # self.find_extreme_value(self.data_voltage, flag='Voltage')
            self.curve_voltage.setPos(self.ptr, 0)  # 重新设定 x 相关的坐标原点

    def update_data_current(self):
        """ 数据左移 """
        if self.data_current is not None:
            self.curve_current.setData(self.data_current)  # 数据填充到绘制曲线中
            # self.ptr = self.value_current[0]  # x 轴记录点
            # self.find_extreme_value(self.data_current, flag='Current')
            self.curve_current.setPos(self.ptr, 0)  # 重新设定 x 相关的坐标原点