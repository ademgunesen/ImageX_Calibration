from model.model import Model, Worker, Worker2
from views.main_view import MainView
import model.utils as utils

class MainController():

    def __init__(self):

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
        if path_name != '':
            worker = Worker(self._model.first_video_image)
            worker.signals.result.connect(self._view.show_first_thresh_image)

            # Execute
            self._model.threadpool.start(worker)
        else:
            self._view.warning_video()

    def play_video_controller(self, beam_thresh):
        """
        After pressing the run button, it creates a thread to run the sum_video in the model, then goes to the view and shows the results.
        """
        self._model.running = True
        self._model.set_beam_thresh(beam_thresh)
        worker = Worker2(self._model.sum_video)
        worker.signals.result.connect(self._view.show_video_images)
        worker.signals.finished.connect(self._view.thread_complete)
        worker.signals.progress.connect(self._view.set_progressbar)
        worker.signals.state.connect(self._view.after_5_sn_img)
        worker.signals.stop.connect(self._view.stop_video)
        
        # Execute
        self._model.threadpool.start(worker)
        self._view.play_video()

    def stop_video_controller(self):
        """
        It makes the video stop when the stop button is pressed.
        """
        self._model.stop_flag()

    def thresh_image_controller(self, seg_tresh):
        """
        Getting the value selected from the Execute->threshold section
        """
        self._model.set_seg_tresh(seg_tresh)

        worker = Worker(self._model.threshold_thread)
        worker.signals.result.connect(self._view.show_thresh_images)
        worker.signals.finished.connect(self._view.stop_gif)
        worker.signals.stop.connect(self._view.warning_msg)
        
        # Execute
        self._model.threadpool.start(worker)
        self._view.after_select_thresh()

    def save_to_file(self):
        date = utils.make_date()
        file = utils.make_file(date)
        
        utils.save_to_file(file, "\nImage 1 Threshold Area Information\nAnterior: " + str(self._model.y_mm))
        utils.save_to_file(file, "\nLeft: " + str(self._model.x_mm))

        utils.save_to_file(file, "\n\nImage 2 Threshold Area Information\nAnterior: " + str(self._model.y_mm))
        utils.save_to_file(file, "\nSuperior: " + str(self._model.x_mm))

        utils.save_to_file(file, "\n\nError Informationn\nLeft Error mm: " + str(self._model.x_mm))
        utils.save_to_file(file, "\nAnterior Error mm (A/L) Image: " + str(self._model.y_mm))
        utils.save_to_file(file, "\nSuperior Error mm: " + str(self._model.x_mm))
        utils.save_to_file(file, "\nAnterior Error mm (A/S) Image: " + str(self._model.y_mm))
        utils.save_to_file(file, "\nAverage Anterior Error mm: " + str(self._model.avr_ant_err))
        utils.save_to_file(file, "\nTOTAL TARGETING ERROR mm: " + str(self._model.target_err))

        self._view.warning_save_variables()

    #GET FUNCTIONS
    def get_x_mm(self):
        return self._model.x_mm

    def get_y_mm(self):
        return self._model.y_mm

    def get_avr_ant_err(self):
        return self._model.avr_ant_err

    def get_targetting_err(self):
        return self._model.target_err

    def get_running(self):
        return self._model.running

    def get_first_frame(self):
        return self._model.image_qt

    def get_second_frame(self):
        return self._model.drawing_img