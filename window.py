from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import *
import sys
from ContourCounting import *
from vidContour import *
import cv2
#create window class
class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # title of window
        self.setWindowTitle('PyQt5 Main Window')
        # place window on screen at x=0, y=0
        # window width = 400, height = 400
        self.setGeometry(400, 400, 400, 400)

        openImageButton = QPushButton('Open image', self)
        #Create a button widget
        openImageButton.resize(openImageButton.sizeHint())
        openImageButton.move(50,50)
        #resize button and move it onto the window. sizeHint() method gives a recommended size for the button
        openImageButton.clicked.connect(self.openImage)

        openTrackingButton = QPushButton('Tracking video', self)
        openTrackingButton.resize(openTrackingButton.sizeHint())
        openTrackingButton.move(200,50)
        openTrackingButton.setObjectName("openImageButton")
        openTrackingButton.clicked.connect(self.openTracking)


        self.show()

        openTrackingButton.clicked.connect(self.openImage)

    #if image button is pressed
    def openImage(self):
        print("image button pressed!")
        imageButtonClicked = True
        global fileName
        fileName, _ = QFileDialog.getOpenFileName(self, "Open image",
                QDir.homePath())
        print('In open: ', fileName)
        ContourCounting(fileName)

        if fileName != '':

            pass
    #if video button is pressed
    def openTracking(self):
        print("video button pressed!")
        openTrackingButtonClicked = True
        global fileName
        fileName, _ = QFileDialog.getOpenFileName(self, "Open video",
                QDir.homePath())
        print('In open: ', fileName)
        tracker = vidContour(fileName)


        if fileName != '':

            pass

    def keyPressEvent(self, event):
        # display code of key that was pressed
        print(event.key())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
