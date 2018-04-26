from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
        QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget, QMainWindow)
import sys
import cv2

class App(QWidget):


    def __init__(self):
        HEIGHT= 400
        WIDTH =300

        super(App, self).__init__(parent = None)
        self.title = 'Fluotify'
        self.resize(HEIGHT,WIDTH)
        #self.videoWidget = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        VideoPlayer= QVideoWidget()
        self.mediaPlayer = QMediaPlayer(self)

        self.videoWidget = QVideoWidget(self)
        self.videoWidget.move(0, 0)
        self.videoWidget.resize(220, 300)
        self.videoWidget.show()

        self.openButton = QPushButton("Open...", self)
        self.openButton.clicked.connect(self.openFile)
        self.openButton.move(10, self.height()-50)
        self.openButton.show()

        self.playButton = QPushButton(self)
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)
        self.playButton.move(100, self.height()-50)

        self.positionSlider = QSlider(Qt.Horizontal, self)
        self.positionSlider.move(200, self.height()-50)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)
        self.positionSlider.resize(200,20)

        self.errorLabel = QLabel(self)
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Maximum)

        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)

        self.show()

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",
                QDir.homePath())
        print('In open: ', fileName)

        if fileName != '':
            qmc = QMediaContent(QUrl.fromLocalFile(fileName))
            self.mediaPlayer.setMedia(qmc)
            self.playButton.setEnabled(True)
            cv2.

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())



class CheckBox(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        self.show()



if __name__ == '__main__':


    app = QApplication(sys.argv)
    window = App()

    window.show()

    sys.exit(app.exec_())
