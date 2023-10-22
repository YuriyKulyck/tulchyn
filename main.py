from PyQt5.QtWidgets import *

app = QApplication([])
app.setStyleSheet("""
    QWidget{

        background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 2 green, stop: 0.4 lime,stop: 1 indigo);
    }
    QPushButton{
    border: 2px solid;
    border-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 white, stop: 0.4 blue,stop: 1 violet);
        background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 white, stop: 0.4 brown,stop: 1 violet);
    }
    Qlabel{
        border: 3px solid;
        border-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 white, stop: 0.4 bright,stop: 1 lime);
        background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 white, stop: 0.4 bright,stop: 1 gold);
    }
""")
window = QWidget()
window.resize(950, 750)

mainline = QHBoxLayout()
h1 = QHBoxLayout()
v1 = QVBoxLayout()
v2 = QVBoxLayout()

photo = QLabel("Фото:")
fould = QPushButton("Папка")
listfould = QListWidget()

button0 = QPushButton("Вліво")
button1 = QPushButton("Вправо")
button2 = QPushButton("Дзеркало")
button3 = QPushButton("Різкість")
button4 = QPushButton("Чорно/білий фон")

mainline.addLayout(v1, stretch=2)
mainline.addLayout(v2, stretch=4)

v1.addWidget(fould)
v1.addWidget(listfould)


v2.addWidget(photo)
v2.addLayout(h1)

h1.addWidget(button0)
h1.addWidget(button1)
h1.addWidget(button2)
h1.addWidget(button3)
h1.addWidget(button4)

window.setLayout(mainline)
window.show()
app.exec()