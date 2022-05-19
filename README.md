# pyqt-drawer
PyQt drawer.

You can set the widget to drawer.

Opening, closing drawer involved animations of size change and drawer/parent window's opacity.

## Requirements
PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-drawer`

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-svg-button.git">pyqt-svg-button</a>

## Feature
* `Drawer(parent, widget: QWidget, orientation)` Constructor.
    * `parent` is parent window.
    * `widget` is the widget you want to set in the drawer.
    * `orientation` is orientation of drawer. Available values are Qt.Horizontal, Qt.Vertical. 
* Being able to set size/opacity duration with `drawer.setDuration(msc)`
* Being able to set end size value with `drawer.setEndValue(size)`.

## Example
Code Example
```python
from PyQt5.QtWidgets import QMainWindow, QListWidget, QApplication, QWidget, QGridLayout
from pyqt_drawer.drawer import Drawer
from pyqt_timer.settingsDialog import SettingsDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        listWidget = QListWidget()
        listWidget.addItems(
            ['Age of Empires II: Definitive Edition', 'American Truck Simulator', 'Arma 3', "Assassin's Creed"])
        drawer = Drawer(self, listWidget) # widget to show/hide
        drawer.setDuration(200) # set duration (200 milliseconds)
        drawer.setEndValue(listWidget.sizeHint().width())  # set end value with listWidget's appropriate maximum width
        
        lay = QGridLayout()
        lay.addWidget(SettingsDialog(), 0, 0, 1, 1)
        lay.addWidget(drawer, 0, 0, 1, 1)
        lay.setContentsMargins(0, 0, 0, 0)
        mainWidget = QWidget()
        mainWidget.setLayout(lay)
        self.setCentralWidget(mainWidget)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec_()
```

Result

https://user-images.githubusercontent.com/55078043/169175912-bce19b71-2246-46aa-9435-5b108ae72c62.mp4
