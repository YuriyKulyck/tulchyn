from PyQt5.QtWidgets import *

app = QApplication([])
app.setStyleSheet("""
    QWidget{

        background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0.23 maroon, stop: 0.76 lime,stop: 0.87 crimson);
    }
    QListWidget{
         border: 5.75px solid;
         border-radius: 5.35px;
         border-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0.12 lime, stop: 0.55 aqua,stop: 0.90 gold);
         background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0.15 aquamarine, stop: 0.44 coral,stop: 0.93 olive);
    }
    QPushButton{
        border: 2px solid;
        border-radius: 9.5px;
        border-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 white, stop: 0.4 blue,stop: 1 violet);
        background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0.1 gold, stop: 0.4 lime,stop: 1 blue);
    }
    QLabel{
        border: 3px solid;
        border-radius: 6.5px;
        border-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0.1 indigo, stop: 0.4 crimson,stop: 0.9 lime);
        background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0.05 blue, stop: 0.25 red,stop: 0.85 gold);
    }
    
 
    QPushButton:hover {
        background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 red, stop: 0.4 gold,stop: 1 aqua);
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