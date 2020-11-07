import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel

def showGui():
    app = QApplication(sys.argv)
    window = QWidget()
    layout = QVBoxLayout()
    app.setStyle('Fusion')
    layout.addWidget(QPushButton('Top'))
    layout.addWidget(QPushButton('Save'))
    window.setLayout(layout)
    window.show()
    return app.exec_()