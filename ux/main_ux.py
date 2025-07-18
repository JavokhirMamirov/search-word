# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1342, 737)
        font = QtGui.QFont()
        font.setKerning(True)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/images/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(128, 100))
        MainWindow.setAnimated(True)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("QScrollBar:horizontal {\n"
"    border: none;\n"
"    background:rgb(234, 237, 252);\n"
"    height: 8px;\n"
"    margin: 0px 0px 0 0px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background:  rgb(119, 126, 255);\n"
"    min-width: 25px;\n"
"    border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background:  rgb(119, 126, 255);\n"
"    width: 10px;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(119, 126, 255);\n"
"    width: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background:rgb(234, 237, 252) ;\n"
"    width: 8px;\n"
"    margin: 0px 0 0px 0;\n"
"    border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {    \n"
"    background:  rgb(119, 126, 255);\n"
"    min-height: 25px;\n"
"    border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background:  rgb(119, 126, 255);\n"
"     height: 20px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background:  rgb(119, 126, 255);\n"
"     height: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setStyleSheet("\n"
"    background-color: rgb(234, 237, 252);\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_file_upload = QtWidgets.QWidget()
        self.page_file_upload.setObjectName("page_file_upload")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_file_upload)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.page_file_upload)
        self.frame.setMinimumSize(QtCore.QSize(800, 500))
        self.frame.setMaximumSize(QtCore.QSize(1000, 600))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(119, 126, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(453, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.next_btn = QtWidgets.QPushButton(self.frame_2)
        self.next_btn.setMinimumSize(QtCore.QSize(120, 36))
        self.next_btn.setMaximumSize(QtCore.QSize(120, 36))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.next_btn.setFont(font)
        self.next_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.next_btn.setStyleSheet("#next_btn{\n"
"background: #777EFF;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"#next_btn:hover{\n"
"    background: rgb(119, 157, 254);\n"
"}\n"
"")
        self.next_btn.setObjectName("next_btn")
        self.horizontalLayout_2.addWidget(self.next_btn)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_6.setStyleSheet("border-radius: 10px;\n"
"background: #F6F9FF;\n"
"border-radius: 24px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(125, 125))
        self.label_2.setMaximumSize(QtCore.QSize(125, 125))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/images/drag.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.upload_btn = QtWidgets.QPushButton(self.frame_6)
        self.upload_btn.setMinimumSize(QtCore.QSize(213, 44))
        self.upload_btn.setMaximumSize(QtCore.QSize(213, 44))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.upload_btn.setFont(font)
        self.upload_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.upload_btn.setStyleSheet("#upload_btn{\n"
"background: #777EFF;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"#upload_btn:hover{\n"
"    background: rgb(119, 157, 254);\n"
"}\n"
"")
        self.upload_btn.setObjectName("upload_btn")
        self.horizontalLayout_7.addWidget(self.upload_btn)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.gridLayout_3.addWidget(self.frame_6, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame_4)
        self.scrollArea = QtWidgets.QScrollArea(self.frame_3)
        self.scrollArea.setStyleSheet("QScrollBar:horizontal {\n"
"    border: none;\n"
"    background:rgb(234, 237, 252);\n"
"    height: 8px;\n"
"    margin: 0px 0px 0 0px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background:  rgb(119, 126, 255);\n"
"    min-width: 25px;\n"
"    border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background:  rgb(119, 126, 255);\n"
"    width: 10px;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(119, 126, 255);\n"
"    width: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background:rgb(234, 237, 252) ;\n"
"    width: 8px;\n"
"    margin: 0px 0 0px 0;\n"
"    border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {    \n"
"    background:  rgb(119, 126, 255);\n"
"    min-height: 25px;\n"
"    border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background:  rgb(119, 126, 255);\n"
"     height: 20px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background:  rgb(119, 126, 255);\n"
"     height: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.verticalLayout.addWidget(self.frame_3)
        self.gridLayout_2.addWidget(self.frame, 1, 1, 2, 2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 104, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 3, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(233, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 2, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(234, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 1, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 101, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem8, 0, 2, 1, 1)
        self.stackedWidget.addWidget(self.page_file_upload)
        self.page_main = QtWidgets.QWidget()
        self.page_main.setObjectName("page_main")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page_main)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_8 = QtWidgets.QFrame(self.page_main)
        self.frame_8.setMinimumSize(QtCore.QSize(390, 0))
        self.frame_8.setMaximumSize(QtCore.QSize(390, 16777215))
        self.frame_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_10 = QtWidgets.QFrame(self.frame_8)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.return_file_upload = QtWidgets.QPushButton(self.frame_10)
        self.return_file_upload.setMinimumSize(QtCore.QSize(180, 36))
        self.return_file_upload.setMaximumSize(QtCore.QSize(180, 36))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.return_file_upload.setFont(font)
        self.return_file_upload.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.return_file_upload.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.return_file_upload.setStyleSheet("#return_file_upload{\n"
"background: #777EFF;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"#return_file_upload:hover{\n"
"    background: rgb(119, 157, 254);\n"
"}\n"
"")
        self.return_file_upload.setObjectName("return_file_upload")
        self.horizontalLayout_4.addWidget(self.return_file_upload)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.verticalLayout_2.addWidget(self.frame_10)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.frame_8)
        self.scrollArea_2.setStyleSheet("#scrollArea_2{\n"
"    border:none;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background:rgb(234, 237, 252);\n"
"    height: 8px;\n"
"    margin: 0px 0px 0 0px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background:  rgb(119, 126, 255);\n"
"    min-width: 25px;\n"
"    border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background:  rgb(119, 126, 255);\n"
"    width: 10px;\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(119, 126, 255);\n"
"    width: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background:rgb(234, 237, 252) ;\n"
"    width: 8px;\n"
"    margin: 0px 0 0px 0;\n"
"    border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {    \n"
"    background:  rgb(119, 126, 255);\n"
"    min-height: 25px;\n"
"    border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background:  rgb(119, 126, 255);\n"
"     height: 20px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background:  rgb(119, 126, 255);\n"
"     height: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 388, 629))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea_2)
        self.horizontalLayout_3.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.page_main)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_4.setContentsMargins(15, 15, 15, 15)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_12 = QtWidgets.QFrame(self.frame_9)
        self.frame_12.setStyleSheet("#frame_12{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"}\n"
"")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_4.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_13 = QtWidgets.QFrame(self.frame_12)
        self.frame_13.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_13.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_13.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_13)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 32))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("#lineEdit{\n"
"border: 1px solid #D9D9D9;\n"
"border-radius: 6px;\n"
"color:#666;\n"
"}\n"
"\n"
"#lineEdit:hover{\n"
"    border: 1px solid #758BFD;\n"
"}\n"
"\n"
"#lineEdit:focus{\n"
"    border: 1px solid #758BFD;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_5.addWidget(self.lineEdit)
        self.search_btn = QtWidgets.QPushButton(self.frame_13)
        self.search_btn.setMinimumSize(QtCore.QSize(120, 32))
        self.search_btn.setMaximumSize(QtCore.QSize(120, 32))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.search_btn.setFont(font)
        self.search_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.search_btn.setStyleSheet("#search_btn{\n"
"background: #777EFF;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"#search_btn:hover{\n"
"    background: rgb(119, 157, 254);\n"
"}\n"
"")
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout_5.addWidget(self.search_btn)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.verticalLayout_4.addWidget(self.frame_13)
        self.tabWidget = QtWidgets.QTabWidget(self.frame_12)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QTabWidget{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QTabWidget::pane {\n"
"  background-color: rgb(255, 255, 255);\n"
"border: 1px solid #D9D9D9;\n"
"border-radius: 8px;\n"
"margin-top:10px;\n"
"}\n"
"QWidget{\n"
"border-radius: 8px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"  background-color: rgb(255, 255, 255);\n"
"     padding: 15px;\n"
"    width:200px;\n"
"} \n"
"\n"
"QTabBar::tab:selected { \n"
" border-bottom: 2px solid #758BFD;\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tab.setObjectName("tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_5.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_5.setSpacing(1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.scrollArea_chostata = QtWidgets.QScrollArea(self.tab)
        self.scrollArea_chostata.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea_chostata.setWidgetResizable(True)
        self.scrollArea_chostata.setObjectName("scrollArea_chostata")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 886, 544))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollArea_chostata.setWidget(self.scrollAreaWidgetContents_3)
        self.gridLayout_5.addWidget(self.scrollArea_chostata, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_6.setSpacing(1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.tab_2)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 886, 544))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_6.addWidget(self.scrollArea_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_7.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_7.setSpacing(1)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 886, 544))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_5)
        self.gridLayout_7.addWidget(self.scrollArea_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.gridLayout_4.addWidget(self.frame_12, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame_9)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)
        self.stackedWidget.addWidget(self.page_main)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "So\'zshunoslik"))
        self.label.setText(_translate("MainWindow", "Fayl yuklash"))
        self.next_btn.setText(_translate("MainWindow", "Keyingi"))
        self.upload_btn.setText(_translate("MainWindow", "Yuklash"))
        self.return_file_upload.setText(_translate("MainWindow", "Yangi fayl yuklash"))
        self.search_btn.setText(_translate("MainWindow", "Qidirish"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Chastota"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Fayl bo\'yicha"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Kontekst"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
