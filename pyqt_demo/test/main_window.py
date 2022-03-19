from PyQt5.Qt import *
from ted_plot import Ui_Form


class Pane(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.plot_sth()

    def plot_sth(self):
        self.plotWidget_ted.plot([1, 2, 3, 4, 5], pen='r', symbol='o')


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    window = Pane()
    window.show()

    sys.exit(app.exec_())
