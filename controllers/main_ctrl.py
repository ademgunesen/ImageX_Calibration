#from _typeshed import Self
import threading
import time
import os

from numpy.lib.function_base import select

from model.model import Model
from views.main_view import MainView

from PyQt5.QtCore import QObject

class MainController(QObject):
    def __init__(self):
        super().__init__()
        """
        connecting from controller to view and model
        """
        self._model = Model(self)
        self._view = MainView(self)
        self._view.show()

    def select_video_controller(self):
        """
        After clicking the select video button, it takes the path of the video from the view and finds the path of the file as the path.
        """
        self._model.running = True

        path_name = self._view.select_video()
        self._model.set_path(path_name)

        if path_name == self._model.Path:
            self._model.first_video_image(path_name)
        else:
            self._view.warning_video()

    def play_video_controller(self, exp_time, beam_thresh, ref_point_thresh):
        """
        After pressing the run button, it creates a thread to run the sum_video in the model, then goes to the view and shows the results.
        """        
        video_thread = threading.Thread(target = self._model.frame_sum_thread, args=(exp_time, beam_thresh, ref_point_thresh,))#thread for frame_sum
        video_thread.start()
        self._view.play_video()
        #if self._model.running == False:
            #self._model.reset_video_variables()
        if self._model.running == False:
            self.warning_video_taken()

    def show_beam_sum_image(self):
        """
        Shows the images returned as a result of pressing the run button.
        """
        if self._model.beam_sum_img != None:
            self._view.show_video_images()

    def stop_video_controller(self):
        """
        It makes the video stop when the stop button is pressed.
        """
        self._model.stop_flag()
        if self._model.running == False:
            self._view.stop_video()
            self._model.reset_video_variables()

    def thresh_image_controller(self, seg_tresh):
        """
        Getting the value selected from the Execute->threshold section
        """
        self._view.start_gif()
        self._view.start_gif2_animation()
        threshold_thread = threading.Thread(target = self._model.threshold_thread, args=(seg_tresh,))#thread for threshold
        threshold_thread.start()

    def thresh_image_results(self):
        """
        Images obtained after threshold is set are displayed in view
        """
        self._view.show_thresh_images()
        self._view.stop_gif2_animation()
    
    def show_first_image(self):
        """
        the first frame view in the video is also shown
        """
        self._view.show_first_thresh_image()
    
    def show_second_image(self):
        """
        The image showing the intersections of the points of the lines obtained by combining the points in the first frame.
        """
        self._view.show_second_image()

    def warning_video_taken(self):
        """
        If the function cannot find the points in the first 5 seconds, it prints a warning in the view and shot down the application.
        """
        self._view.warning_video_taken()
        #self._view.close_app()

    #GET FUNCTIONS
    def get_x_mm(self):
        return self._model.x_mm

    def get_y_mm(self):
        return self._model.y_mm

    def get_avr_ant_err(self):
        return self._model.avr_ant_err

    def get_targetting_err(self):
        return self._model.target_err

    def get_success(self):
        return self._model.success

    def get_running(self):
        return self._model.running

    def get_images_path(self):
        return self._model.path

    def get_first_frame(self):
        return self._model.image_qt

    def get_second_frame(self):
        return self._model.drawing_img

    def get_binary_img(self):
        return self._model.binary_img_qt

    def get_beam_sum_img(self):
        return self._model.beam_sum_img

    #SET FUNCTIONS
    def set_progresbar(self, count):
        self._view.set_progresbar(count)


