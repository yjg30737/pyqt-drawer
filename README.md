# pyqt-drawer
PyQt Drawer

## Requirements
PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-drawer.git --upgrade```

## Feature
* ```Drawer(widget: QWidget, orientation)``` Constructor. Default orientation is set to Qt.Horizontal. Giving Qt.Vertical is enabled, but not recommended. (There is a bug related to vertical animation starting point, i will fix it)
* Being able to set duration with ```drawer.setDuration(msc)```
* Being able to set end value with ```drawer.setEndValue(size)```

## Example
Code Example
```python
from PyQt5.QtWidgets import QMainWindow, QListWidget, QApplication
from pyqt_drawer.drawer import Drawer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        listWidget = QListWidget()
        listWidget.addItems(
            ['Age of Empires II: Definitive Edition', 'American Truck Simulator', 'Arma 3', "Assassin's Creed"])
        drawer = Drawer(listWidget) # widget to show/hide
        drawer.setDuration(200) # set duration (200 mseconds)
        drawer.setEndValue(listWidget.sizeHint().width()) # set end value with listwidget's appropriate maximum width
        self.setCentralWidget(drawer)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
```

Result

https://user-images.githubusercontent.com/55078043/145942243-9b4d2f47-ed6a-4eaa-a092-5d1dd18211cb.mp4


