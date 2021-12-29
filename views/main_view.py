import sys
import os
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QMovie
#importing necessary widgets
from PyQt5.QtWidgets import (QMainWindow, QMessageBox, QFileDialog, QStyle)
#load view
from views.main_view_ui3 import Ui_MainWindow


#All widgets that appear in Qt designer are in this section.
class MainView(QMainWindow):
    def __init__(self, controller):
        """
        Defining and linking widgets that require action that appear in the gui
        """
        super().__init__()
        
        #view controller connection 
        self._controller = controller

        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        # click buttons & connect widgets to controller
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

        #threshold buttons
        self._ui.action60.triggered.connect(lambda: self._controller.thresh_image_controller(60))
        self._ui.action65.triggered.connect(lambda: self._controller.thresh_image_controller(65))
        self._ui.action70.triggered.connect(lambda: self._controller.thresh_image_controller(70))
        self._ui.action75.triggered.connect(lambda: self._controller.thresh_image_controller(75))
        self._ui.action80.triggered.connect(lambda: self._controller.thresh_image_controller(80))

        #for the application to start from the video page
        self._ui.tabwidget.setCurrentIndex(0)
        self._ui.progressBar.hide()
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

        self.movie1 = QMovie(image_path)
        self.movie2 = QMovie(image_path)

    def start_gif1_animation(self):   
        """
        Start Gif Animation
        """     
        self.movie1.start()

    def start_gif2_animation(self):
        """
        Start Gif Animation
        """ 
        self.movie2.start()
  
    def stop_gif1_animation(self):
        """
        Start Gif Animation
        """ 
        self.movie1.stop()

    def stop_gif2_animation(self):
        """
        Start Gif Animation
        """ 
        self.movie2.stop()

    def select_video(self):
        """
        When you press the select button, it shows the things that need to be changed on the screen.            
        """
        #self._ui.progressBar.setValue(0)

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

        if path_name != '':
            self._ui.run_video.setEnabled(True)
        #else:
            #self.warningMsg()

        return path_name

    def play_video(self):
        """
        When the run button is pressed, it first shows the things that need to be changed on the screen
        """
        self.clear_all_results()
        self._ui.stop_video.setEnabled(True)
        self._ui.run_video.setEnabled(False)
        self._ui.select_video.setEnabled(False)
        self._ui.progressing.setText("Executing!")

        self._ui.gif_1.setMovie(self.movie1)
    
        self.start_gif1_animation()

        self._ui.combo_box_1.setEnabled(False)
        self._ui.combo_box_2.setEnabled(False)
        self._ui.combo_box_3.setEnabled(False)

        #self.clear_all_results()# farklı bir fonksiyon yaz ya da ihtiyaca bak

    def show_video_images(self):
        """
        When the run button is pressed, it shows the last things that need to be changed on the screen.
        """
        self._ui.execute.setEnabled(True)
        self._ui.progressing.setText("Completed!")
        self.stop_gif1_animation()

        self._ui.tabwidget.setCurrentIndex(1)

        self._ui.g_image_1.setPixmap(QtGui.QPixmap((self._controller.get_beam_sum_img())))
        self._ui.g_image_2.setPixmap(QtGui.QPixmap((self._controller.get_beam_sum_img())))

        self._ui.select_video.setEnabled(True)
        self._ui.run_video.setEnabled(True)
        self._ui.stop_video.setEnabled(False) 

        self._ui.combo_box_1.setEnabled(True)
        self._ui.combo_box_2.setEnabled(True)
        self._ui.combo_box_3.setEnabled(True)

    def set_progresbar(self, count):
        """
        Written for progress bar but not used
        """
        self._ui.progressBar.setValue(count)
                
    def stop_video(self):
        """
        It shows the things that need to change on the screen when the stop button is pressed.
        """
        self._ui.progressing.setText("Stopped!")

        self._ui.select_video.setEnabled(True)
        self._ui.run_video.setEnabled(False)
        self._ui.stop_video.setEnabled(False)

        self._ui.g_image_1.clear()
        self._ui.g_image_2.clear()

        self.stop_gif1_animation()

    def start_gif(self):
        """
        start gif animation in result page
        """
        self._ui.gif_2.setMovie(self.movie2)

    def show_thresh_images(self):
        """
        Displaying images and values according to the selected threshold value
        """
        self._ui.run_video.setEnabled(True)
        self._ui.clear.setEnabled(True)
        
        self._ui.g_image_3.setPixmap(QPixmap.fromImage(self._controller.get_binary_img()))
        self._ui.g_image_4.setPixmap(QPixmap.fromImage(self._controller.get_binary_img()))

        #image1 Threshold Results
        self._ui.T1_label_3.setText(str(self._controller.get_y_mm()) + 'mm')
        self._ui.T1_label_4.setText(str(self._controller.get_x_mm()) + 'mm')
        #image2 Trhreshold Results
        self._ui.T2_label_3.setText(str(self._controller.get_y_mm())+ 'mm')
        self._ui.T2_label_4.setText(str(self._controller.get_x_mm())+ 'mm')
        #error
        self._ui.ei_label_1.setText(str(self._controller.get_x_mm()))
        self._ui.ei_label_2.setText(str(self._controller.get_y_mm()))
        self._ui.ei_label_3.setText(str(self._controller.get_x_mm()))
        self._ui.ei_label_4.setText(str(self._controller.get_y_mm()))
        #average anterior error
        self._ui.ei_label_5.setText(str(self._controller.get_avr_ant_err()))
        #total target error (pisagor)
        self._ui.ei_label_6.setText(str(self._controller.get_targetting_err()))

    def show_first_thresh_image(self):
        """
        the first frame in the selected video is displayed on the screen
        """
        self._ui.player.setPixmap(self._controller.get_first_frame())

    def show_second_image(self):
        """
        Displaying the picture where the points are combined with a line after the points determined in the first frame are determined
        """
        self._ui.player.setPixmap(self._controller.get_second_frame())
        
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

    def warning_video_taken(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Error")
        msg.setText("Points not detected, new video should be taken!")

        x = msg.exec_()
        self.close_app()

    def warning_division_zero(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Error")
        msg.setText("No white space found in the video!")

        x = msg.exec_()
        self.close_app()

    def warning_video(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Error")
        msg.setText("You have to select a VIDEO!")

        x = msg.exec_()

    def warning_path(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Error")
        msg.setText("Wrong path!")

        x = msg.exec_()

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