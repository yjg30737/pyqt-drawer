from PyQt5.QtWidgets import QPushButton, QWidget, QGridLayout
from PyQt5.QtCore import Qt, QPropertyAnimation, QAbstractAnimation
from pyqt_resource_helper import PyQtResourceHelper


class Drawer(QWidget):
    def __init__(self, widget):
        super().__init__()
        self.__initUi(widget)

    def __initUi(self, widget):
        self.__btn = QPushButton()
        self.__btn.setFixedSize(self.__btn.sizeHint().width(), self.__btn.sizeHint().height())
        self.__btn.setCheckable(True)
        self.__btn.toggled.connect(self.__drawerToggled)

        PyQtResourceHelper.setStyleSheet([self.__btn], ['style/button.css'])
        PyQtResourceHelper.setIcon([self.__btn], ['ico/drawer.png'])

        self.__widget = widget
        self.__widget.setFixedWidth(0)

        self.__animation = QPropertyAnimation(self, b"width")
        self.__animation.setStartValue(0)
        self.__animation.setDuration(200)
        self.__animation.setEndValue(200)
        self.__animation.valueChanged.connect(self.__widget.setFixedWidth)

        lay = QGridLayout()
        lay.addWidget(self.__widget, 1, 0, 1, 2)
        lay.addWidget(self.__btn, 0, 0, 1, 1, Qt.AlignTop | Qt.AlignLeft)
        lay.setSpacing(0)

        self.setLayout(lay)

    def __drawerToggled(self, f):
        if f:
            self.__animation.setDirection(QAbstractAnimation.Forward)
        else:
            self.__animation.setDirection(QAbstractAnimation.Backward)
        self.__animation.start()

    def setDuration(self, msecs):
        self.__animation.setDuration(msecs)

    def setEndValue(self, value):
        self.__animation.setEndValue(value)

