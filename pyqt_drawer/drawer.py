from PyQt5.QtWidgets import QWidget, QGridLayout
from PyQt5.QtCore import Qt, QPropertyAnimation, QAbstractAnimation
from pyqt_svg_icon_pushbutton import SvgIconPushButton


class Drawer(QWidget):
    def __init__(self, widget, orientation=Qt.Horizontal):
        super().__init__()
        self.__initUi(widget=widget, orientation=orientation)

    def __initUi(self, widget, orientation):
        self.__btn = SvgIconPushButton()
        self.__btn.setFixedSize(self.__btn.sizeHint().width(), self.__btn.sizeHint().height())
        self.__btn.setCheckable(True)
        self.__btn.toggled.connect(self.__drawerToggled)
        self.__btn.setIcon('ico/drawer.svg')

        self.__widget = widget
        self.__animation = ''
        if orientation == Qt.Horizontal:
            self.__widget.setFixedWidth(0)
            self.__animation = QPropertyAnimation(self, b"width")
            self.__animation.valueChanged.connect(self.__widget.setFixedWidth)
        else:
            self.__widget.setFixedHeight(0)
            self.__animation = QPropertyAnimation(self, b"height")
            self.__animation.valueChanged.connect(self.__widget.setFixedHeight)

        self.__animation.setStartValue(0)
        self.__animation.setDuration(200) # default duration
        self.__animation.setEndValue(200) # default end value

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

    def setIcon(self, icon):
        self.__btn.setIcon(icon)

