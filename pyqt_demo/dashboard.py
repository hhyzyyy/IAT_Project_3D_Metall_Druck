# -*- coding: UTF-8 -*-

"""
author:  Huayu Hu
date:    2022/1/20
contact: huayu.hu@outlook.com
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from pyqt_demo import ui_mainWindow5


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainW = QMainWindow()
    ui = ui_mainWindow5.Ui_MainWindow()
    ui.setupUi(mainW)
    mainW.show()
    sys.exit(app.exec_())
