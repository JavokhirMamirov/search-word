from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow

from ux import loading_screen

class LoadingScreen(QMainWindow, loading_screen.Ui_MainWindow):
    def __init__(self, obj):
        super(LoadingScreen, self).__init__()
        self.setupUi(self)
        self.setParent(obj)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.movie = QtGui.QMovie(":/newPrefix/images/loading.gif")
        self.label_loading.setMovie(self.movie)
        self.hide()

    def startAnimation(self):
        self.movie.start()
        self.show()

    def resizeWindow(self,width, height):
        self.resize(width, height)

    def stopAnimation(self):
        self.movie.stop()
        self.close()


