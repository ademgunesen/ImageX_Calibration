import sys
import os
import time
from PyQt5.QtGui import QPixmap, QMovie
#importing necessary widgets
from PyQt5.QtWidgets import (QMainWindow, QMessageBox, QFileDialog, QStyle)

#load view
from views.main_view_ui3 import Ui_MainWindow

class MainView(QMainWindow):

    def __init__(self, controller):
        super(MainView, self).__init__()

        self._controller = controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self._ui.select_video.clicked.connect(self._controller.select_video_controller)
        self._ui.run_video.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self._ui.run_video.clicked.connect(lambda: self._controller.play_video_controller(self._ui.combo_box_3.currentText(),
                                                                                        self._ui.combo_box_1.currentText(),
                                                                                        self._ui.combo_box_2.currentText()))
        self._ui.stop_video.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self._ui.stop_video.clicked.connect(self._controller.stop_video_controller)
        self._ui.clear.clicked.connect(self.clear_all_results) 
        
        #menu bar triggered
        self._ui.Exit.triggered.connect(self.close_app)
        self._ui.Save_TXT_File.triggered.connect(self._controller.save_to_file)
        self._ui.actionAbout.triggered.connect(self.warning_help_about)

        #threshold buttons
        self._ui.action60.triggered.connect(lambda: self._controller.thresh_image_controller(60))
        self._ui.action65.triggered.connect(lambda: self._controller.thresh_image_controller(65))
        self._ui.action70.triggered.connect(lambda: self._controller.thresh_image_controller(70))
        self._ui.action75.triggered.connect(lambda: self._controller.thresh_image_controller(75))
        self._ui.action80.triggered.connect(lambda: self._controller.thresh_image_controller(80))

        #for the application to start from the video page
        self._ui.tabwidget.setCurrentIndex(0)
        self._ui.clear.hide()

        #set default variables
        self._ui.combo_box_1.setCurrentIndex(4)
        self._ui.combo_box_2.setCurrentIndex(5)
        self._ui.combo_box_3.setCurrentIndex(1)

        # determine if application is a script file or frozen exe
        image_name = 'Spinner.gif'
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)
        image_path = os.path.join(application_path, image_name)
        self.movie = QMovie(image_path)

    def select_video(self):
        """
        When you press the select button, it shows the things that need to be changed on the screen.            
        """
        self._ui.progressbar.setValue(0)
        self._ui.execute.setEnabled(False)
        self._ui.menuFile.setEnabled(False)

        self._ui.g_image_1.clear()
        self._ui.g_image_2.clear()
        self._ui.g_image_3.clear()
        self._ui.g_image_4.clear()
        self._ui.player.clear()

        self._ui.T1_label_3.clear()
        self._ui.T1_label_4.clear()
        self._ui.T2_label_3.clear()
        self._ui.T2_label_4.clear()        

        path_name, _ = QFileDialog.getOpenFileName(self,"Video Files")
        self._ui.run_video.setEnabled(True)

        return path_name     

    def play_video(self):
        """
        When the run button is pressed, it first shows the things that need to be changed on the screen
        """
        self.clear_all_results()
        self._ui.stop_video.setEnabled(True)
        self._ui.run_video.setEnabled(False)
        self._ui.select_video.setEnabled(False)
        self._ui.execute.setEnabled(False)
        self._ui.menuFile.setEnabled(False)

        self._ui.combo_box_1.setEnabled(False)
        self._ui.combo_box_2.setEnabled(False)
        self._ui.combo_box_3.setEnabled(False)
        
        self._ui.player.setPixmap(self._controller.get_first_frame())
        #self._ui.player.setPixmap(self._controller.get_second_frame())

    def stop_video(self, common_flag):
        """
        It shows the things that need to change on the screen when the stop button is pressed.
        """
        if common_flag == 0:
            print(common_flag)
            self._ui.progressbar.setValue(0)

            self._ui.select_video.setEnabled(True)
            self._ui.run_video.setEnabled(True)
            self._ui.stop_video.setEnabled(False)
            self._ui.execute.setEnabled(False)
            self._ui.menuFile.setEnabled(False)

            self._ui.combo_box_1.setEnabled(True)
            self._ui.combo_box_2.setEnabled(True)
            self._ui.combo_box_3.setEnabled(True)

            self.clear_all_results()

        else:
            print(common_flag)
            self._ui.progressbar.setValue(0)

            self._ui.select_video.setEnabled(True)
            self._ui.run_video.setEnabled(True)
            self._ui.stop_video.setEnabled(False)
            self._ui.execute.setEnabled(False)
            self._ui.menuFile.setEnabled(False)

            self._ui.combo_box_1.setEnabled(True)
            self._ui.combo_box_2.setEnabled(True)
            self._ui.combo_box_3.setEnabled(True)

            self.clear_all_results()
            self.warning_video_taken()

    def show_video_images(self, beam_sum_img):
        """
        When the run button is pressed, it shows the last things that need to be changed on the screen.
        """
        if self._controller.get_running() == True:
            
            self._ui.tabwidget.setCurrentIndex(1)

            self._ui.g_image_1.setPixmap(beam_sum_img)
            self._ui.g_image_2.setPixmap(beam_sum_img)

            self._ui.select_video.setEnabled(True)
            self._ui.run_video.setEnabled(True)
            self._ui.stop_video.setEnabled(False)
            self._ui.execute.setEnabled(True) 

            self._ui.combo_box_1.setEnabled(True)
            self._ui.combo_box_2.setEnabled(True)
            self._ui.combo_box_3.setEnabled(True)

    def after_5_sn_img(self, img):
        """
        Displaying the picture where the points are combined with a line after the points determined in the first frame are determined
        """
        self._ui.player.setPixmap(img)

    def after_select_thresh(self):

        self._ui.gif.setMovie(self.movie)
        self.start_gif_animation()
        self._ui.run_video.setEnabled(True)
        self._ui.clear.setEnabled(True)

    def show_thresh_images(self, list):
        """
        Displaying images and values according to the selected threshold value
        """
        self._ui.menuFile.setEnabled(True)
        self._ui.g_image_3.setPixmap(QPixmap.fromImage(list[0]))
        self._ui.g_image_4.setPixmap(QPixmap.fromImage(list[0]))

        #image1 Threshold Results
        self._ui.T1_label_3.setText(str(list[2]) + 'mm')
        self._ui.T1_label_4.setText(str(list[1]) + 'mm')
        #image2 Trhreshold Results
        self._ui.T2_label_3.setText(str(list[2])+ 'mm')
        self._ui.T2_label_4.setText(str(list[1])+ 'mm')
        #error
        self._ui.ei_label_1.setText(str(list[1]))
        self._ui.ei_label_2.setText(str(list[2]))
        self._ui.ei_label_3.setText(str(list[1]))
        self._ui.ei_label_4.setText(str(list[2]))
        #average anterior error
        self._ui.ei_label_5.setText(str(list[3]))
        #total target error (pisagor)
        self._ui.ei_label_6.setText(str(list[4]))

    def show_first_thresh_image(self, first_img):
        """
        the first frame in the selected video is displayed on the screen
        """
        self._ui.player.setPixmap(first_img)
        
    def set_progressbar(self, count):
        """
        Written for progress bar but not used
        """
        self._ui.progressbar.setValue(count)

    def clear_all_results(self):
        """
        Clearing the values on the screen when the clear button is pressed 
        """
        #images
        self._ui.g_image_1.clear()
        self._ui.g_image_2.clear()

        #threshold images
        self._ui.g_image_3.clear()
        self._ui.g_image_4.clear()

        #image1 Threshold Results
        self._ui.T1_label_3.clear()
        self._ui.T1_label_4.clear()

        #image2 Trhreshold Results
        self._ui.T2_label_3.clear()
        self._ui.T2_label_4.clear()

        self._ui.ei_label_1.clear()
        self._ui.ei_label_2.clear()
        self._ui.ei_label_3.clear()
        self._ui.ei_label_4.clear()
        self._ui.ei_label_5.clear()
        self._ui.ei_label_6.clear()

        self._ui.clear.setEnabled(False)

    def thread_complete(self):
        print("THREAD COMPLETE!")
    
    def warning(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Error")
        msg.setText("Warning!")

        x = msg.exec_()

    def warning_save_variables(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Error")
        msg.setText("All variables were save!")

        x = msg.exec_()

    def warning_video(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Error")
        msg.setText("You have to select a VIDEO!")

        x = msg.exec_()

    def warning_beam_thresh(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Error")
        msg.setText("Threshold area is not detected, new video should be taken or decrease beam threshold!")

        x = msg.exec_()

    def warning_video_taken(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Error")
        msg.setText("Referans points are not detected, new video should be taken or decrease referans point threshold!")

        x = msg.exec_()
        self.close_app()
    
    def warning_help_about(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("About ImageX Calibration")
        msg.setText("ImageX Calibration 1.1\n\nCreated by Vivente Soft\nZeynep iskenderoğlu")
        msg.setStandardButtons(QMessageBox.Ok)

        x = msg.exec_()
    
    def stop_gif(self):

        self.stop_gif_animation()

    def warning_msg(self, flag):
        if flag == 1:
            self.warning_beam_thresh()
    
    def start_gif_animation(self):   
        """
        Start Gif Animation
        """     
        self.movie.start()

    def stop_gif_animation(self):
        """
        Stop Gif Animation
        """ 
        self.movie.stop()

    def close_app(self):
        reply = QMessageBox.question(self, "Window Close", "Are you sure you want to close the window?",
                                    QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            sys.exit()
            
        else:
            pass
    
    def closeEvent(self, event):
            close = QMessageBox.question(self, "QUIT",
                                         "Are you sure want to stop process?",
                                         QMessageBox.Yes | QMessageBox.No)
            if close == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()