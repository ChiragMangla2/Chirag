import sys
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtWidgets import *

import DUDES
from GUI_Code3 import Ui_mainWindow


# from bs4 import BeautifulSoup

class MainThread(QThread):

    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        DUDES.main()


startExe = MainThread()

class StartGui(QMainWindow):
    def __init__(self):
        super().__init__()

        self.gui = Ui_mainWindow()
        self.gui.setupUi(self)

        self.gui.pushButton.clicked.connect(self.StartTask)
        self.gui.pushButton_2.clicked.connect(self.close)

    def StartTask(self):
        self.gui.label1 = QtGui.QMovie("Resources/Initalising.gif")
        self.gui.label_2.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie("Resources//Digital bar.gif")
        self.gui.label_3.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.label3 = QtGui.QMovie("Resources//Robot 2.gif")
        self.gui.label_4.setMovie(self.gui.label3)
        self.gui.label3.start()

        self.gui.label4 = QtGui.QMovie("Resources//DNA2.gif")
        self.gui.label_5.setMovie(self.gui.label4)
        self.gui.label4.start()

        self.gui.label5 = QtGui.QMovie("Resources//Globe.gif")
        self.gui.label_6.setMovie(self.gui.label5)
        self.gui.label5.start()


        timer=QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        
        startExe.start()

    def showTime(self):
        ct = QTime.currentTime()
        cd = QDate.currentDate()
        label_date = cd.toString(Qt.ISODate)
        label_time = ct.toString('hh:mm:ss')
        self.gui.Time_textBrowser.setText(label_time)
        self.gui.Date_textBrowser.setText(label_date)

    
GuiApp = QApplication(sys.argv)
jarvis_gui = StartGui()
jarvis_gui.show()
exit(GuiApp.exec_())
