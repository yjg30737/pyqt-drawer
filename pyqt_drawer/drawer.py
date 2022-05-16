from PyQt5.QtWidgets import QWidget, QGridLayout, QGraphicsOpacityEffect
from PyQt5.QtCore import Qt, QPropertyAnimation, QAbstractAnimation
from pyqt_svg_icon_pushbutton import SvgIconPushButton


class Drawer(QWidget):
    def __init__(self, parent, widget, orientation=Qt.Horizontal):
        super().__init__()
        self.__initUi(parent, widget=widget, orientation=orientation)

    def __initUi(self, parent, widget, orientation):
        self.__parent = parent
        self.__parent.installEventFilter(self)

        self.__btn = SvgIconPushButton()
        self.__btn.setCheckable(True)
        self.__btn.toggled.connect(self.__drawerToggled)
        self.__btn.setIcon('ico/drawer.svg')
        self.__btn.setPadding(5)

        self.__widget = widget

        align = ''

        # init size animation
        self.__sizeAnimation = ''
        if orientation == Qt.Horizontal:
            self.__widget.setFixedWidth(0)
            align = Qt.AlignLeft
            self.__sizeAnimation = QPropertyAnimation(self, b"width")
            self.__sizeAnimation.valueChanged.connect(self.__widget.setFixedWidth)
        else:
            self.__widget.setFixedHeight(0)
            align = Qt.AlignTop
            self.__sizeAnimation = QPropertyAnimation(self, b"height")
            self.__sizeAnimation.valueChanged.connect(self.__widget.setFixedHeight)
        self.__sizeAnimation.setStartValue(0)
        self.__sizeAnimation.setDuration(200)  # default duration
        self.__sizeAnimation.setEndValue(200)  # default end value

        # init opacity animation
        self.__opacityAnimation = QPropertyAnimation(self, b"opacity")
        self.__widget.setGraphicsEffect(QGraphicsOpacityEffect(opacity=0.0))
        self.__opacityAnimation.valueChanged.connect(self.__setOpacity)

        self.__opacityAnimation.setStartValue(0.0)
        self.__opacityAnimation.setDuration(200)
        self.__opacityAnimation.setEndValue(1.0)

        # todo init parent opacity animation
        # self.__parentOpacityAnimation = QPropertyAnimation(self, b"parentopacity")
        # self.__parentOpacityAnimation.valueChanged.connect(self.__setParentOpacity)

        # self.__parentOpacityAnimation.setStartValue(1.0)
        # self.__parentOpacityAnimation.setDuration(200)
        # self.__parentOpacityAnimation.setEndValue(0.8)

        lay = QGridLayout()
        lay.addWidget(self.__btn, 0, 0, 1, 1, Qt.AlignTop | Qt.AlignLeft)
        lay.addWidget(self.__widget, 0, 0, 1, 2, align)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)

        self.setLayout(lay)

    def __drawerToggled(self, f):
        if f:
            self.__sizeAnimation.setDirection(QAbstractAnimation.Forward)
            self.__opacityAnimation.setDirection(QAbstractAnimation.Forward)
            # self.__parentOpacityAnimation.setDirection(QAbstractAnimation.Forward)
            self.__btn.hide()
        else:
            self.__sizeAnimation.setDirection(QAbstractAnimation.Backward)
            self.__opacityAnimation.setDirection(QAbstractAnimation.Backward)
            # self.__parentOpacityAnimation.setDirection(QAbstractAnimation.Backward)
            self.__btn.show()
        self.__sizeAnimation.start()
        self.__opacityAnimation.start()
        # self.__parentOpacityAnimation.start()

    def __setOpacity(self, opacity):
        opacity_effect = QGraphicsOpacityEffect(opacity=opacity)
        self.__widget.setGraphicsEffect(opacity_effect)

    # def __setParentOpacity(self, opacity):
    #     opacity_effect = QGraphicsOpacityEffect(opacity=opacity)
    #     self.__parent.setGraphicsEffect(opacity_effect)

    def setDuration(self, msecs):
        self.__sizeAnimation.setDuration(msecs)
        self.__opacityAnimation.setDuration(msecs)
        # self.__parentOpacityAnimation.setDuration(msecs)

    def setEndValue(self, value):
        self.__sizeAnimation.setEndValue(value)

    def setIcon(self, icon):
        self.__btn.setIcon(icon)

    def eventFilter(self, obj, e):
        if isinstance(obj, type(self.__parent)):
            if e.type() == 3:
                if self.__sizeAnimation.currentValue() == self.__sizeAnimation.endValue():
                    self.__btn.toggle()
        return super().eventFilter(obj, e)