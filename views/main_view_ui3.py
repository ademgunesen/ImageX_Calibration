# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_view3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1281, 722)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabwidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabwidget.setGeometry(QtCore.QRect(0, 0, 1271, 651))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabwidget.setFont(font)
        self.tabwidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabwidget.setObjectName("tabwidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tab_1.setObjectName("tab_1")
        self.groupBox = QtWidgets.QGroupBox(self.tab_1)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 571, 461))
        self.groupBox.setMaximumSize(QtCore.QSize(1251, 491))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setObjectName("groupBox")
        self.player = QtWidgets.QLabel(self.groupBox)
        self.player.setGeometry(QtCore.QRect(0, 40, 401, 401))
        self.player.setMaximumSize(QtCore.QSize(1201, 401))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.player.setFont(font)
        self.player.setAutoFillBackground(True)
        self.player.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.player.setText("")
        self.player.setScaledContents(True)
        self.player.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.player.setObjectName("player")
        self.gif_1 = QtWidgets.QLabel(self.groupBox)
        self.gif_1.setGeometry(QtCore.QRect(440, 50, 81, 81))
        self.gif_1.setAutoFillBackground(True)
        self.gif_1.setText("")
        self.gif_1.setScaledContents(True)
        self.gif_1.setObjectName("gif_1")
        self.progressing = QtWidgets.QLabel(self.groupBox)
        self.progressing.setGeometry(QtCore.QRect(440, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.progressing.setFont(font)
        self.progressing.setAutoFillBackground(True)
        self.progressing.setText("")
        self.progressing.setObjectName("progressing")
        self.layoutWidget = QtWidgets.QWidget(self.tab_1)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 480, 355, 44))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.select_video = QtWidgets.QPushButton(self.layoutWidget)
        self.select_video.setObjectName("select_video")
        self.gridLayout_6.addWidget(self.select_video, 0, 0, 1, 1)
        self.run_video = QtWidgets.QPushButton(self.layoutWidget)
        self.run_video.setEnabled(False)
        icon = QtGui.QIcon.fromTheme("media-playback-start")
        self.run_video.setIcon(icon)
        self.run_video.setObjectName("run_video")
        self.gridLayout_6.addWidget(self.run_video, 0, 1, 1, 1)
        self.stop_video = QtWidgets.QPushButton(self.layoutWidget)
        self.stop_video.setEnabled(False)
        icon = QtGui.QIcon.fromTheme("media-playback-stop")
        self.stop_video.setIcon(icon)
        self.stop_video.setObjectName("stop_video")
        self.gridLayout_6.addWidget(self.stop_video, 0, 2, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.tab_1)
        self.progressBar.setGeometry(QtCore.QRect(410, 490, 321, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.tabwidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.ErrorGroupBox = QtWidgets.QGroupBox(self.tab_2)
        self.ErrorGroupBox.setGeometry(QtCore.QRect(870, 120, 391, 221))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ErrorGroupBox.setFont(font)
        self.ErrorGroupBox.setObjectName("ErrorGroupBox")
        self.em_label_1 = QtWidgets.QLabel(self.ErrorGroupBox)
        self.em_label_1.setGeometry(QtCore.QRect(10, 30, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.em_label_1.setFont(font)
        self.em_label_1.setObjectName("em_label_1")
        self.em_label_2 = QtWidgets.QLabel(self.ErrorGroupBox)
        self.em_label_2.setGeometry(QtCore.QRect(10, 60, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.em_label_2.setFont(font)
        self.em_label_2.setObjectName("em_label_2")
        self.em_label_3 = QtWidgets.QLabel(self.ErrorGroupBox)
        self.em_label_3.setGeometry(QtCore.QRect(10, 90, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.em_label_3.setFont(font)
        self.em_label_3.setObjectName("em_label_3")
        self.em_label_4 = QtWidgets.QLabel(self.ErrorGroupBox)
        self.em_label_4.setGeometry(QtCore.QRect(10, 120, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.em_label_4.setFont(font)
        self.em_label_4.setObjectName("em_label_4")
        self.em_label_5 = QtWidgets.QLabel(self.ErrorGroupBox)
        self.em_label_5.setGeometry(QtCore.QRect(10, 150, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.em_label_5.setFont(font)
        self.em_label_5.setObjectName("em_label_5")
        self.em_label_6 = QtWidgets.QLabel(self.ErrorGroupBox)
        self.em_label_6.setGeometry(QtCore.QRect(10, 180, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.em_label_6.setFont(font)
        self.em_label_6.setObjectName("em_label_6")
        self.ei_label_1 = QtWidgets.QLabel(self.ErrorGroupBox)
        self.ei_label_1.setGeometry(QtCore.QRect(300, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ei_label_1.setFont(font)
        self.ei_label_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ei_label_1.setAutoFillBackground(True)
        self.ei_label_1.setFrameShape(QtWidgets.QFrame.Box)
        self.ei_label_1.setText("")
        self.ei_label_1.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.ei_label_1.setObjectName("ei_label_1")
        self.ei_label_2 = QtWidgets.QLabel(self.ErrorGroupBox)
        self.ei_label_2.setGeometry(QtCore.QRect(300, 60, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ei_label_2.setFont(font)
        self.ei_label_2.setAutoFillBackground(True)
        self.ei_label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.ei_label_2.setText("")
        self.ei_label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.ei_label_2.setObjectName("ei_label_2")
        self.ei_label_3 = QtWidgets.QLabel(self.ErrorGroupBox)
        self.ei_label_3.setGeometry(QtCore.QRect(300, 120, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ei_label_3.setFont(font)
        self.ei_label_3.setAutoFillBackground(True)
        self.ei_label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.ei_label_3.setText("")
        self.ei_label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.ei_label_3.setObjectName("ei_label_3")
        self.ei_label_4 = QtWidgets.QLabel(self.ErrorGroupBox)
        self.ei_label_4.setGeometry(QtCore.QRect(300, 90, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ei_label_4.setFont(font)
        self.ei_label_4.setAutoFillBackground(True)
        self.ei_label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.ei_label_4.setText("")
        self.ei_label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.ei_label_4.setObjectName("ei_label_4")
        self.ei_label_5 = QtWidgets.QLabel(self.ErrorGroupBox)
        self.ei_label_5.setGeometry(QtCore.QRect(300, 180, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ei_label_5.setFont(font)
        self.ei_label_5.setAutoFillBackground(True)
        self.ei_label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.ei_label_5.setText("")
        self.ei_label_5.setObjectName("ei_label_5")
        self.ei_label_6 = QtWidgets.QLabel(self.ErrorGroupBox)
        self.ei_label_6.setGeometry(QtCore.QRect(300, 150, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ei_label_6.setFont(font)
        self.ei_label_6.setAutoFillBackground(True)
        self.ei_label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.ei_label_6.setText("")
        self.ei_label_6.setObjectName("ei_label_6")
        self.groupBox_1 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_1.setGeometry(QtCore.QRect(10, 10, 231, 241))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_1.setFont(font)
        self.groupBox_1.setObjectName("groupBox_1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.g_image_1 = QtWidgets.QLabel(self.groupBox_1)
        self.g_image_1.setAutoFillBackground(True)
        self.g_image_1.setFrameShape(QtWidgets.QFrame.Box)
        self.g_image_1.setText("")
        self.g_image_1.setScaledContents(True)
        self.g_image_1.setObjectName("g_image_1")
        self.gridLayout_4.addWidget(self.g_image_1, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 260, 231, 241))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.g_image_2 = QtWidgets.QLabel(self.groupBox_2)
        self.g_image_2.setAutoFillBackground(True)
        self.g_image_2.setFrameShape(QtWidgets.QFrame.Box)
        self.g_image_2.setText("")
        self.g_image_2.setScaledContents(True)
        self.g_image_2.setObjectName("g_image_2")
        self.gridLayout_5.addWidget(self.g_image_2, 0, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(280, 10, 231, 241))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.g_image_4 = QtWidgets.QLabel(self.groupBox_4)
        self.g_image_4.setAutoFillBackground(True)
        self.g_image_4.setFrameShape(QtWidgets.QFrame.Box)
        self.g_image_4.setText("")
        self.g_image_4.setScaledContents(True)
        self.g_image_4.setObjectName("g_image_4")
        self.gridLayout_2.addWidget(self.g_image_4, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(280, 260, 231, 241))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.g_image_3 = QtWidgets.QLabel(self.groupBox_3)
        self.g_image_3.setAutoFillBackground(True)
        self.g_image_3.setFrameShape(QtWidgets.QFrame.Box)
        self.g_image_3.setText("")
        self.g_image_3.setScaledContents(True)
        self.g_image_3.setObjectName("g_image_3")
        self.gridLayout_3.addWidget(self.g_image_3, 0, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setGeometry(QtCore.QRect(550, 270, 301, 161))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.T2_label_1 = QtWidgets.QLabel(self.groupBox_6)
        self.T2_label_1.setGeometry(QtCore.QRect(10, 30, 121, 21))
        self.T2_label_1.setObjectName("T2_label_1")
        self.T2_label_2 = QtWidgets.QLabel(self.groupBox_6)
        self.T2_label_2.setGeometry(QtCore.QRect(10, 60, 121, 21))
        self.T2_label_2.setObjectName("T2_label_2")
        self.T2_label_3 = QtWidgets.QLabel(self.groupBox_6)
        self.T2_label_3.setGeometry(QtCore.QRect(10, 90, 121, 21))
        self.T2_label_3.setObjectName("T2_label_3")
        self.T2_label_4 = QtWidgets.QLabel(self.groupBox_6)
        self.T2_label_4.setGeometry(QtCore.QRect(10, 120, 121, 21))
        self.T2_label_4.setObjectName("T2_label_4")
        self.T2_label_5 = QtWidgets.QLabel(self.groupBox_6)
        self.T2_label_5.setGeometry(QtCore.QRect(190, 30, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.T2_label_5.setFont(font)
        self.T2_label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.T2_label_5.setAutoFillBackground(True)
        self.T2_label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.T2_label_5.setText("")
        self.T2_label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.T2_label_5.setObjectName("T2_label_5")
        self.T2_label_7 = QtWidgets.QLabel(self.groupBox_6)
        self.T2_label_7.setGeometry(QtCore.QRect(190, 90, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.T2_label_7.setFont(font)
        self.T2_label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.T2_label_7.setAutoFillBackground(True)
        self.T2_label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.T2_label_7.setText("")
        self.T2_label_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.T2_label_7.setObjectName("T2_label_7")
        self.T2_label_6 = QtWidgets.QLabel(self.groupBox_6)
        self.T2_label_6.setGeometry(QtCore.QRect(190, 60, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.T2_label_6.setFont(font)
        self.T2_label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.T2_label_6.setAutoFillBackground(True)
        self.T2_label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.T2_label_6.setText("")
        self.T2_label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.T2_label_6.setObjectName("T2_label_6")
        self.T2_label_8 = QtWidgets.QLabel(self.groupBox_6)
        self.T2_label_8.setGeometry(QtCore.QRect(190, 120, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.T2_label_8.setFont(font)
        self.T2_label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.T2_label_8.setAutoFillBackground(True)
        self.T2_label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.T2_label_8.setText("")
        self.T2_label_8.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.T2_label_8.setObjectName("T2_label_8")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(550, 40, 301, 151))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.T1_label_1 = QtWidgets.QLabel(self.groupBox_5)
        self.T1_label_1.setGeometry(QtCore.QRect(10, 30, 121, 21))
        self.T1_label_1.setObjectName("T1_label_1")
        self.T1_label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.T1_label_2.setGeometry(QtCore.QRect(10, 60, 121, 21))
        self.T1_label_2.setObjectName("T1_label_2")
        self.T1_label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.T1_label_3.setGeometry(QtCore.QRect(10, 90, 121, 21))
        self.T1_label_3.setObjectName("T1_label_3")
        self.T1_label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.T1_label_4.setGeometry(QtCore.QRect(10, 120, 121, 21))
        self.T1_label_4.setObjectName("T1_label_4")
        self.T1_label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.T1_label_5.setGeometry(QtCore.QRect(190, 30, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.T1_label_5.setFont(font)
        self.T1_label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.T1_label_5.setAutoFillBackground(True)
        self.T1_label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.T1_label_5.setText("")
        self.T1_label_5.setScaledContents(False)
        self.T1_label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.T1_label_5.setObjectName("T1_label_5")
        self.T1_label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.T1_label_7.setGeometry(QtCore.QRect(190, 90, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.T1_label_7.setFont(font)
        self.T1_label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.T1_label_7.setAutoFillBackground(True)
        self.T1_label_7.setFrameShape(QtWidgets.QFrame.Box)
        self.T1_label_7.setText("")
        self.T1_label_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.T1_label_7.setObjectName("T1_label_7")
        self.T1_label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.T1_label_6.setGeometry(QtCore.QRect(190, 60, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.T1_label_6.setFont(font)
        self.T1_label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.T1_label_6.setAutoFillBackground(True)
        self.T1_label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.T1_label_6.setText("")
        self.T1_label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.T1_label_6.setObjectName("T1_label_6")
        self.T1_label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.T1_label_8.setGeometry(QtCore.QRect(190, 120, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.T1_label_8.setFont(font)
        self.T1_label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.T1_label_8.setAutoFillBackground(True)
        self.T1_label_8.setFrameShape(QtWidgets.QFrame.Box)
        self.T1_label_8.setText("")
        self.T1_label_8.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.T1_label_8.setObjectName("T1_label_8")
        self.clear = QtWidgets.QPushButton(self.tab_2)
        self.clear.setEnabled(False)
        self.clear.setGeometry(QtCore.QRect(1150, 500, 101, 31))
        self.clear.setObjectName("clear")
        self.gif_2 = QtWidgets.QLabel(self.tab_2)
        self.gif_2.setGeometry(QtCore.QRect(210, 510, 91, 91))
        self.gif_2.setAutoFillBackground(True)
        self.gif_2.setText("")
        self.gif_2.setScaledContents(True)
        self.gif_2.setObjectName("gif_2")
        self.tabwidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1281, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.menuFile.setFont(font)
        self.menuFile.setObjectName("menuFile")
        self.execute = QtWidgets.QMenu(self.menubar)
        self.execute.setEnabled(False)
        self.execute.setObjectName("execute")
        self.menuThreshold = QtWidgets.QMenu(self.execute)
        self.menuThreshold.setObjectName("menuThreshold")
        self.menuImage_1 = QtWidgets.QMenu(self.menubar)
        self.menuImage_1.setObjectName("menuImage_1")
        self.menuImage_2 = QtWidgets.QMenu(self.menubar)
        self.menuImage_2.setObjectName("menuImage_2")
        MainWindow.setMenuBar(self.menubar)
        self.open_video_file = QtWidgets.QAction(MainWindow)
        self.open_video_file.setObjectName("open_video_file")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.Exit = QtWidgets.QAction(MainWindow)
        self.Exit.setObjectName("Exit")
        self.show_images = QtWidgets.QAction(MainWindow)
        self.show_images.setObjectName("show_images")
        self.actionImage_2 = QtWidgets.QAction(MainWindow)
        self.actionImage_2.setObjectName("actionImage_2")
        self.actionRun = QtWidgets.QAction(MainWindow)
        self.actionRun.setObjectName("actionRun")
        self.action60 = QtWidgets.QAction(MainWindow)
        self.action60.setObjectName("action60")
        self.action65 = QtWidgets.QAction(MainWindow)
        self.action65.setObjectName("action65")
        self.action70 = QtWidgets.QAction(MainWindow)
        self.action70.setObjectName("action70")
        self.action75 = QtWidgets.QAction(MainWindow)
        self.action75.setObjectName("action75")
        self.action80 = QtWidgets.QAction(MainWindow)
        self.action80.setObjectName("action80")
        self.actionSuperior_Anterior_Image1 = QtWidgets.QAction(MainWindow)
        self.actionSuperior_Anterior_Image1.setCheckable(True)
        self.actionSuperior_Anterior_Image1.setObjectName("actionSuperior_Anterior_Image1")
        self.actionLeft_Anterior_Image1 = QtWidgets.QAction(MainWindow)
        self.actionLeft_Anterior_Image1.setCheckable(True)
        self.actionLeft_Anterior_Image1.setObjectName("actionLeft_Anterior_Image1")
        self.actionSuperior_Anterior_Image_2 = QtWidgets.QAction(MainWindow)
        self.actionSuperior_Anterior_Image_2.setCheckable(True)
        self.actionSuperior_Anterior_Image_2.setObjectName("actionSuperior_Anterior_Image_2")
        self.actionLeft_Anterior_Image2 = QtWidgets.QAction(MainWindow)
        self.actionLeft_Anterior_Image2.setCheckable(True)
        self.actionLeft_Anterior_Image2.setChecked(False)
        self.actionLeft_Anterior_Image2.setObjectName("actionLeft_Anterior_Image2")
        self.actionOnce = QtWidgets.QAction(MainWindow)
        self.actionOnce.setObjectName("actionOnce")
        self.Save_TXT_File = QtWidgets.QAction(MainWindow)
        self.Save_TXT_File.setObjectName("Save_TXT_File")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionasd = QtWidgets.QAction(MainWindow)
        self.actionasd.setObjectName("actionasd")
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.Save_TXT_File)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.Exit)
        self.menuThreshold.addAction(self.action60)
        self.menuThreshold.addAction(self.action65)
        self.menuThreshold.addAction(self.action70)
        self.menuThreshold.addAction(self.action75)
        self.menuThreshold.addAction(self.action80)
        self.execute.addAction(self.actionOnce)
        self.execute.addAction(self.menuThreshold.menuAction())
        self.menuImage_1.addAction(self.actionSuperior_Anterior_Image1)
        self.menuImage_1.addAction(self.actionLeft_Anterior_Image1)
        self.menuImage_2.addAction(self.actionSuperior_Anterior_Image_2)
        self.menuImage_2.addAction(self.actionLeft_Anterior_Image2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.execute.menuAction())
        self.menubar.addAction(self.menuImage_1.menuAction())
        self.menubar.addAction(self.menuImage_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabwidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "End-to-End (E2E) Film Analysis"))
        self.groupBox.setTitle(_translate("MainWindow", "Video"))
        self.select_video.setText(_translate("MainWindow", "Select Video"))
        self.run_video.setText(_translate("MainWindow", "Run"))
        self.stop_video.setText(_translate("MainWindow", "Stop"))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_1), _translate("MainWindow", "Video Page"))
        self.ErrorGroupBox.setTitle(_translate("MainWindow", "Error Information"))
        self.em_label_1.setText(_translate("MainWindow", "Left Error mm:"))
        self.em_label_2.setText(_translate("MainWindow", "Anterior Error mm (A/L) Image:"))
        self.em_label_3.setText(_translate("MainWindow", "Superior Error mm:"))
        self.em_label_4.setText(_translate("MainWindow", "Anterior Error mm (A/S) Image:"))
        self.em_label_5.setText(_translate("MainWindow", "Average Anterior Error mm:"))
        self.em_label_6.setText(_translate("MainWindow", "TOTAL TARGETING ERROR mm:"))
        self.groupBox_1.setTitle(_translate("MainWindow", "Image 1"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Image 2"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Image 1 Threshold Area"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Image 2 Threshold Area"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Image 2 Threshold Area Information"))
        self.T2_label_1.setText(_translate("MainWindow", "Centroid Area:"))
        self.T2_label_2.setText(_translate("MainWindow", "Pixels to Left:"))
        self.T2_label_3.setText(_translate("MainWindow", "Pixels to Top:"))
        self.T2_label_4.setText(_translate("MainWindow", "Eccentricity:"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Image 1 Threshold Area Information"))
        self.T1_label_1.setText(_translate("MainWindow", "Centroid Area:"))
        self.T1_label_2.setText(_translate("MainWindow", "Pixels to Left:"))
        self.T1_label_3.setText(_translate("MainWindow", "Pixels to Top:"))
        self.T1_label_4.setText(_translate("MainWindow", "Eccentricity:"))
        self.clear.setText(_translate("MainWindow", "Clear"))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_2), _translate("MainWindow", "Result Page"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.execute.setTitle(_translate("MainWindow", "Execute"))
        self.menuThreshold.setTitle(_translate("MainWindow", "Threshold"))
        self.menuImage_1.setTitle(_translate("MainWindow", "Image 1"))
        self.menuImage_2.setTitle(_translate("MainWindow", "Image 2"))
        self.open_video_file.setText(_translate("MainWindow", "Open Video File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.Exit.setText(_translate("MainWindow", "Exit"))
        self.show_images.setText(_translate("MainWindow", "Show Images"))
        self.actionImage_2.setText(_translate("MainWindow", "Image 2"))
        self.actionRun.setText(_translate("MainWindow", "Run"))
        self.action60.setText(_translate("MainWindow", "60%"))
        self.action65.setText(_translate("MainWindow", "65%"))
        self.action70.setText(_translate("MainWindow", "70%"))
        self.action75.setText(_translate("MainWindow", "75%"))
        self.action80.setText(_translate("MainWindow", "80%"))
        self.actionSuperior_Anterior_Image1.setText(_translate("MainWindow", "Superior/Anterior Image"))
        self.actionLeft_Anterior_Image1.setText(_translate("MainWindow", "Left/Anterior Image"))
        self.actionSuperior_Anterior_Image_2.setText(_translate("MainWindow", "Superior/Anterior Image"))
        self.actionLeft_Anterior_Image2.setText(_translate("MainWindow", "Left/Anterior Image"))
        self.actionOnce.setText(_translate("MainWindow", "Once"))
        self.Save_TXT_File.setText(_translate("MainWindow", "Save TXT File"))
        self.Save_TXT_File.setStatusTip(_translate("MainWindow", "Save File"))
        self.Save_TXT_File.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionasd.setText(_translate("MainWindow", "asd"))