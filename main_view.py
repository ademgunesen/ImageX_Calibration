import sys
import os
import time
import numpy as np

from PyQt5.Qt import *
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPainter, QPen, QMovie
from PyQt5.QtCore import QPointF
from threading import Thread
from PIL import Image, ImageQt

#load view
from views.main_view_ui3 import Ui_MainWindow

from PyQt5.QtWidgets import (QMainWindow, QMessageBox, QApplication, QVBoxLayout,
    QLabel, QPushButton, QWidget, QLineEdit, QTextEdit, QProgressBar,QFileDialog, QStyle, QAction)

path = 'C:/Users/viven/Desktop/GUIProjects/ImageX_Project/'

class MainView(QMainWindow):
    def __init__(self, controller):
        """
        gui de görünen, işlem gerketiren widgetların(butonlar) tanımlanması ve birbirine bağlanması
        """
        super().__init__()

        self._controller = controller

        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        # click buttons & connect widgets to controller
        self._ui.select_video.clicked.connect(self._controller.select_video_controller)
        self._ui.run_video.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self._ui.run_video.clicked.connect(self._controller.play_video_controller)
        self._ui.stop_video.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self._ui.stop_video.clicked.connect(self._controller.stop_video_controller)
        self._ui.clear.clicked.connect(self.clear_all_results)   
     
        #menu bar triggered
        self._ui.Exit.triggered.connect(self.close_app)
        self._ui.Save_TXT_File.triggered.connect(self.save_file)
        #self._ui.actionPrint.triggered.connect(self.printVariables)

        #threshold buttons
        self._ui.action60.triggered.connect(lambda: self._controller.thresh_image_controller(60))
        self._ui.action65.triggered.connect(lambda: self._controller.thresh_image_controller(65))
        self._ui.action70.triggered.connect(lambda: self._controller.thresh_image_controller(70))
        self._ui.action75.triggered.connect(lambda: self._controller.thresh_image_controller(75))
        self._ui.action80.triggered.connect(lambda: self._controller.thresh_image_controller(80))

        self._ui.tabwidget.setCurrentIndex(0)
        #define gift path
        self.movie = QMovie(path + "resources/img/Spinner.gif")

    # Start Animation
    def start_animation(self):
        self.movie.start()
  
    # Stop Animation
    def stop_animation(self):
        self.movie.stop()

    def select_video(self):
        """
        select butonun basılınca ekranda değişmesi gereken şeyleri gösteriyor
        """
        #self._ui.progressBar.setValue(0)

        self._ui.g_image_1.clear()
        self._ui.g_image_2.clear()
        self._ui.g_image_3.clear()
        self._ui.g_image_4.clear()
        self._ui.player.clear()

        self._ui.T1_label_5.clear()
        self._ui.T1_label_6.clear()
        self._ui.T2_label_5.clear()
        self._ui.T2_label_6.clear()

        path_name, _ = QFileDialog.getOpenFileName(self,"Video Files")

        if path_name != '':
            self._ui.run_video.setEnabled(True)
        #else:
            #self.warningMsg()

        return path_name

    def play_video(self):
        """
        run butonun basılınca ilk başta ekranda değişmesi gereken şeyleri gösteriyor
        """
        self._ui.stop_video.setEnabled(True)
        self._ui.run_video.setEnabled(False)
        self._ui.select_video.setEnabled(False)
        self._ui.progressing.setText("Executing!")

        self._ui.gif.setMovie(self.movie)

        self.start_animation()

        '''#progress bar için
        while self._ui.progressBar.value() != 100:
            print(self._controller.get_count())
            self._ui.progressBar.setValue(self._controller.get_count())
            time.sleep(1)
            if self._ui.progressBar.value() == 100:
                #self._controller.stopVideoCntr()
                break
        '''

    def show_video_images(self):
        """
        run butonun basılınca en son olarak ekranda değişmesi gereken şeyleri gösteriyor
        """
        self._ui.execute.setEnabled(True)
        self._ui.progressing.setText("Completed!")

        self._ui.tabwidget.setCurrentIndex(1)

        self._ui.g_image_1.setPixmap(QtGui.QPixmap(self._controller.get_images_path() + "/beam_sum.jpg"))
        self._ui.g_image_2.setPixmap(QtGui.QPixmap(self._controller.get_images_path() + "/beam_sum.jpg"))

        self._ui.select_video.setEnabled(True)
        self._ui.run_video.setEnabled(False)
        self._ui.stop_video.setEnabled(False)

    def progressbar(self):#
        while self._ui.progressBar.value() != 100:
            self._ui.progressBar.setValue(self._controller.get_count())
            if self._ui.progressBar.value() == 100:
                #self._controller.stopVideoCntr()
                break

        while self._ui.progressBar.value() < 100:
            #update progressBar value
            print(self._ui.progressBar.value())

            self._ui.progressBar.setValue(self._controller.get_count())

            if self._controller.get_running() == False:
                break

        while self._ui.progressBar.value() == 0:
            print(self._controller.get_count())

            self._ui.progressBar.setValue(self._controller.get_count())

            if self._ui.progressBar.value() ==100:
                break

        #self.diplayVideoResults()

    def stop_video(self):
        """
        stop butonuna basılnca ekranda değişmesi gereken şeyleri gösteriyor
        """
        #self._ui.progressBar.setValue(0)
        self._ui.progressing.setText("Stopped!")

        self._ui.select_video.setEnabled(True)
        self._ui.run_video.setEnabled(False)
        self._ui.stop_video.setEnabled(False)

        self._ui.g_image_1.clear()
        self._ui.g_image_2.clear()

        self.stop_animation()

    def show_thresh_images(self):
        """
        seçilen threahold değerine göre image ve değerler gösteriliyor
        """
        self._ui.clear.setEnabled(True)

        self._ui.g_image_3.setPixmap(QPixmap.fromImage(self._controller.get_binary_img()))
        self._ui.g_image_4.setPixmap(QPixmap.fromImage(self._controller.get_binary_img()))

        #image1 Threshold Results
        self._ui.T1_label_5.setText(str(self._controller.get_x_mm()))
        self._ui.T1_label_6.setText(str(self._controller.get_y_mm()))

        self._ui.T2_label_5.setText(str(self._controller.get_x_mm()))
        self._ui.T2_label_6.setText(str(self._controller.get_y_mm()))
        """
        self._ui.T1_label_7.setText(str(self._controller.get_x_mm()))
        self._ui.T1_label_8.setText(str(self._controller.get_x_mm()))

        #image2 Trhreshold Results

        self._ui.T2_label_7.setText(str(self._controller.get_x_mm()))
        self._ui.T2_label_8.setText(str(self._controller.get_x_mm()))

        self._ui.ei_label_1.setText(str(self._controller.get_x_mm()))
        self._ui.ei_label_2.setText(str(self._controller.get_x_mm()))
        self._ui.ei_label_3.setText(str(self._controller.get_x_mm()))
        self._ui.ei_label_4.setText(str(self._controller.get_x_mm()))
        self._ui.ei_label_5.setText(str(self._controller.get_x_mm()))
        self._ui.ei_label_6.setText(str(self._controller.get_x_mm()))
        """

    def show_first_thresh_image(self):
        """
        seçilen videodaki ilk framei ekranda gösteriyor
        """
        self._ui.player.setPixmap(self._controller.get_first_frame())

    def clear_all_results(self):
        """
        clear butonuna basılınca ekrandaki değerlerin temizlenmesi
        """
        #for dot pixels
        """
        self._ui.dot_pixel_1.hide()
        self._ui.dot_pixel_2.hide()
        self._ui.dot_pixel_3.hide()
        """
        #images
        self._ui.g_image_3.clear()
        self._ui.g_image_4.clear()

        #image1 Threshold Results
        self._ui.T1_label_5.clear()
        self._ui.T1_label_6.clear()
        self._ui.T1_label_7.clear()
        self._ui.T1_label_8.clear()

        #image2 Trhreshold Results
        self._ui.T2_label_5.clear()
        self._ui.T2_label_6.clear()
        self._ui.T2_label_7.clear()
        self._ui.T2_label_8.clear()

        self._ui.ei_label_1.clear()
        self._ui.ei_label_2.clear()
        self._ui.ei_label_3.clear()
        self._ui.ei_label_4.clear()
        self._ui.ei_label_5.clear()
        self._ui.ei_label_6.clear()

        self._ui.clear.setEnabled(False)

    def display_message(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Error")
        msg.setText("You have to select and run a video!")

        x = msg.exec_()

    def warning_message(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Error")
        msg.setText("You have to select a VIDEO!")

        x = msg.exec_()

    def save_file(self):
        with open('test.txt', 'w') as f:
            my_text = self._ui.ei_label_1.toPlainText()#label değil text olmalı. Neyin save edileceğini öğren
            f.write(my_text)

    def close_app(self):
        reply = QMessageBox.question(self, "Window Close", "Are you sure you want to close the window?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            sys.exit()
            
        else:
            pass
