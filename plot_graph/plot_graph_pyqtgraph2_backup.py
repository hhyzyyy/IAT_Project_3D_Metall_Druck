import array
import threading
import pyqtgraph as pg
import numpy as np


def Serial():
    dat = 100
    i = 0
    while True:
        dat += 1
        dat = 50 * np.sin(dat)

        if len(data) < historyLength:
            data.append(dat)
        else:
            data[:-1] = data[1:]  # 前移
            data[-1] = dat

        i += 1


def plotData():
    curve.setData(data)


if __name__ == "__main__":
    app = pg.mkQApp()  # 建立app
    win = pg.GraphicsWindow()  # 建立窗口
    win.setWindowTitle(u'pyqtgraph逐点画波形图')
    win.resize(800, 500)  # 小窗口大小
    data = array.array('i')  # 可动态改变数组的大小,double型数组
    historyLength = 200  # 横坐标长度
    a = 0
    data = np.zeros(historyLength).__array__('d')  # 把数组长度定下来
    p = win.addPlot()  # 把图p加入到窗口中
    p.showGrid(x=True, y=True)  # 把X和Y的表格打开
    p.setRange(xRange=[0, historyLength], yRange=[0, 255], padding=0)
    p.setLabel(axis='left', text='y / V')  # 靠左
    p.setLabel(axis='bottom', text='x / point')
    p.setTitle('Current')  # 表格的名字
    curve = p.plot()  # 绘制一个图形
    curve.setData(data)

    th1 = threading.Thread(target=Serial)  # 目标函数一定不能带（）被这个BUG搞了好久
    th1.start()
    timer = pg.QtCore.QTimer()
    timer.timeout.connect(plotData)  # 定时刷新数据显示
    timer.start(50)  # 多少ms调用一次
    app.exec_()
