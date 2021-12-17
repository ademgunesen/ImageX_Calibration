import threading
import time
import os

from model.model import Model
from views.main_view import MainView

from PyQt5 import QtGui
from PyQt5.QtCore import QObject

class MainController(QObject):
    def __init__(self):
        super().__init__()

        self._model = Model(self)
        self._view = MainView(self)
        self._view.show()

    def select_video_controller(self):
        """
        select video butonuna basıldıktan sonra videonun Pathini viewdan alıp path olarak dosyanın pathini buluyor
        """
        self._model.running = True

        path_name = self._view.select_video()

        head_tail = os.path.split(path_name)
        self._model.path = head_tail[0]
        self._model.file_name = head_tail[1]

        self._model.set_path(path_name)

        if path_name == '':
            self._view.close_app()
        else:
            self._model.first_video_image(path_name)

    def play_video_controller(self):
        """
        run butonuna basıldıktan sonra mdeldeki sumVideoyu çalıştırabilmek için thread oluşturuyor sonra viewa gidip sonuçları gösteriyor
        """
        if self._model.running == False:
            self._model.reset_video_variables()
        else:
            video_thread = threading.Thread(target = self._model.frame_sum_thread)#thread for frame_sum
            video_thread.start()
            self._view.play_video()

    def show_beam_sum_image(self):
        """
        run butonuna basılması sonucunda dönen imageları viewda gösteriyor
        """
        self._view.show_video_images()

    def stop_video_controller(self):
        """
        stop utonuna basılıca videonun durmasını sağlıyor
        """
        self._model.stop_flag()
        if self._model.running == False:
            self._view.stop_video()
            self._model.reset_video_variables()

    def thresh_image_controller(self, seg_tresh):
        """
        Execute->threshold kısmından seçilen değerin alınması
        """
        self._view.start_gif()
        self._view.start_animation()
        threshold_thread = threading.Thread(target = self._model.threshold_thread, args=(seg_tresh,))#thread for threshold
        threshold_thread.start()
        

    def thresh_image_results(self):

        self._view.show_thresh_images()
        self._view.stop_animation()
    
    def show_first_image(self):
        """
        videodaki ilk frame viewda gösteriliyor
        """
        self._view.show_first_thresh_image()
    
    def show_second_image(self):

        self._view.show_second_image()

    #GET FUNCTIONS
    def get_x_mm(self):
        return self._model.x_mm

    def get_y_mm(self):
        return self._model.y_mm

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

