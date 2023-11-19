



from PIL import Image, ImageFilter, ImageEnhance
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import *
import os


def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap


app = QApplication([])
app.setStyleSheet("""
    QWidget{

        background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0.23 maroon, stop: 0.76 lime,stop: 0.87 crimson);
    }
    QListWidget{
         border: 5.75px solid;
         border-radius: 5.35px;
         border-color:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0.12 lime, stop: 0.55 aqua,stop: 0.90 gold);
         background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0.15 aqua, stop: 0.44 coral,stop: 0.93 olive);
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
    QLabel:hover {
        background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 blue, stop: 0.4 violet,stop: 1 crimson);
    }
    QListWidget:hover {
        background:qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0 maroon, stop: 0.4 lime,stop: 1 indigo);
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
button5 = QPushButton("Вліво")
button6 = QPushButton("Вправо")
button7 = QPushButton("Дзеркало")

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


class WorkPhoto:
    def __init__(self):
        self.image = None
        self.folder = None
        self.filename = None

    def load(self):
        imagePath = os.path.join(self.folder, self.filename)
        self.image = Image.open(imagePath)

    def showImage(self):
        pixel = pil2pixmap(self.image)
        pixel = pixel.scaled(800, 600, Qt.KeepAspectRatio)
        photo.setPixmap(pixel)

    def rotate_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.showImage()

    def rotate_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.showImage()

    def mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.showImage()

    def sharper(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.showImage()

    def endolist(self):
        self.image = self.image.convert(("L"))
        self.showImage()

    def contrast(self):
        self.image = ImageEnhance.Contrast(self.image).enhance(2.2)
        self.showImage()


urban = WorkPhoto()


def open_folder():
    urban.folder = QFileDialog.getExistingDirectory()
    files = os.listdir(urban.folder)
    listfould.clear()
    listfould.addItems(files)


def showChosenImage():
    urban.filename = listfould.currentItem().text()
    urban.load()
    urban.showImage()


listfould.currentRowChanged.connect(showChosenImage)

button0.clicked.connect(urban.rotate_left)
button1.clicked.connect(urban.rotate_right)
button2.clicked.connect(urban.mirror)
button3.clicked.connect(urban.sharper)
button4.clicked.connect(urban.endolist)
fould.clicked.connect(open_folder)
window.setLayout(mainline)
window.show()
app.exec()

#
