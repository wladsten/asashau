from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui

app = QApplication([])

win=QWidget()
win.resize(700,500)
win.setWindowTitle('cat')
win.show()

label_p=QLabel('')
label_p.hide()
pixmapimage=QPixmap('ghota.jpg')
pixmapimage= pixmapimage.scaled(400,400, Qt.KeepAspectRatio)
label_p.setPixmap(pixmapimage)
label_p.show()

label=QLabel('ми ехать в асашай')
label.hide()

tor=QPushButton('Борат')


w=QVBoxLayout()
w.addWidget(label_p)
w.addWidget(label)
w.addWidget(tor)
win.setLayout(w)

def asashau():
    label.show()
tor.clicked.connect(asashau)
app.exec_()
