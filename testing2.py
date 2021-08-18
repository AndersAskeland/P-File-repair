import random
from PySide2 import QtCore, QtGui, QtWidgets

class SlidingStackedWidget(QtWidgets.QStackedWidget):
    def __init__(self, parent=None):
        super(SlidingStackedWidget, self).__init__(parent)

        self.m_direction = QtCore.Qt.Horizontal
        self.m_speed = 500
        self.m_animationtype = QtCore.QEasingCurve.OutCubic
        self.m_now = 0
        self.m_next = 0
        self.m_wrap = False
        self.m_pnow = QtCore.QPoint(0, 0)
        self.m_active = False

    # x 
    @QtCore.Slot()
    def slideInPrev(self):
        now = self.currentIndex()
        if self.m_wrap or now > 0:
            self.slideInIdx(now - 1)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        slidingStacked = SlidingStackedWidget()
        button_prev = QtWidgets.QPushButton(
            "Previous", pressed=slidingStacked.slideInPrev
        )
        button_next = QtWidgets.QPushButton(
            "Next", pressed=slidingStacked.slideInNext
        )
        hlay = QtWidgets.QHBoxLayout()
        hlay.addWidget(button_prev)
        hlay.addWidget(button_next)
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        lay = QtWidgets.QVBoxLayout(central_widget)
        lay.addLayout(hlay)
        lay.addWidget(slidingStacked)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())