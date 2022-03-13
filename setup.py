from setuptools import setup, find_packages

setup(
    name='pyqt-drawer',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_drawer.style': ['button.css'], 'pyqt_drawer.ico': ['drawer.svg']},
    description='PyQt drawer',
    url='https://github.com/yjg30737/pyqt-drawer.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-resource-helper @ git+https://git@github.com/yjg30737/pyqt-resource-helper.git@main'
        'pyqt-svg-icon-pushbutton @ git+https://git@github.com/yjg30737/pyqt-svg-icon-pushbutton.git@main'
    ]
)