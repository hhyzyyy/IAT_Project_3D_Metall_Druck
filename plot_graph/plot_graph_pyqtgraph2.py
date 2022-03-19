import array
import threading
import pyqtgraph as pg
import numpy as np
from kafka_test import KafkaConsumer


def get_data():
    for msg in consumer:
        value = msg.value_current.decode('utf8')
        print("%s-%d-%d value=%s" % (msg.topic1, msg.partition, msg.offset, value))
        value = value.split('&')

        if len(data) < historyLength:
            data.append(float(value[-1]))
        else:
            data[:-1] = data[1:]
            data[-1] = float(value[-1])


def plotData():
    curve.setData(data)


if __name__ == "__main__":
    app = pg.mkQApp()  # 建立app
    win = pg.GraphicsWindow()  # 建立窗口
    win.setWindowTitle('Iat_Project')
    win.resize(800, 500)  # 小窗口大小
    data = array.array('i')  # 可动态改变数组的大小,double型数组
    historyLength = 200  # 横坐标长度
    data = np.zeros(historyLength).__array__('d')  # 把数组长度定下来
    p = win.addPlot()  # 把图p加入到窗口中
    p.showGrid(x=True, y=True)  # 把X和Y的表格打开
    p.setRange(xRange=[0, historyLength], yRange=[0, 255], padding=0)
    p.setLabel(axis='left', text='y / V')  # 靠左
    p.setLabel(axis='bottom', text='x / point')
    p.setTitle('Current')  # 表格的名字
    curve = p.plot(name='mode2')  # 绘制一个图形
    curve.setData(data)

    consumer = KafkaConsumer("Current", bootstrap_servers=["localhost:9092"], auto_offset_reset='latest', consumer_timeout_ms=6000)

    th1 = threading.Thread(target=get_data)  # 目标函数一定不能带（）被这个BUG搞了好久
    th1.start()
    timer = pg.QtCore.QTimer()
    timer.timeout.connect(plotData)  # 定时刷新数据显示
    timer.start(1)  # 多少ms调用一次
    app.exec_()
