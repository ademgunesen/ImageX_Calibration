#stop_flag = 0 
#center_of_mass_flag = 1
import model.utils as utils
import math 
import cv2
import numpy as np
from skimage.morphology import disk, closing
from skimage.filters import median, threshold_otsu

from PIL import Image, ImageQt

from PyQt5.QtCore import QObject, QThreadPool, QRunnable, pyqtSignal, pyqtSlot
my_formatter = "{0:.2f}"

import traceback, sys

class WorkerSignals(QObject):
    
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)
    state = pyqtSignal(object)
    stop = pyqtSignal(int)

class Worker(QRunnable):

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        self.kwargs['stop_callback'] = self.signals.stop

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done

class Worker2(QRunnable):

    def __init__(self, fn, *args, **kwargs):
        super(Worker2, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress
        self.kwargs['state_callback'] = self.signals.state
        self.kwargs['stop_callback'] = self.signals.stop

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done

class Model():

    def __init__(self, controller):

        self._controller = controller

        #SET VARIABLES
        self.Path = ' '
        self.beam_thresh = 0

        self.beam_sum = 0
        self.beam_sum_l = 0
        self.beam_sum_r = 0
        self.binary_img_qt = 0
        self.planned_center_l = 0
        self.planned_center_r = 0

        self.x_mm = 0
        self.y_mm = 0
        self.avr_ant_err = 0
        self.target_err = 0

        self.count = 0

        self.seg_tresh = ' '
        self.success = ' '

        self.running = True

        self.threadpool = QThreadPool()
        #print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
    
    def first_video_image(self, stop_callback):
        """
        finds the first frame of the selected video
        """
        vidObj = cv2.VideoCapture(self.Path)
        success, image = vidObj.read()
        self.image_qt = utils.show_images_in_designer(image)
        stop_callback.emit(0)

        return self.image_qt

    def threshold_thread(self, stop_callback):
        """
        Since segmentation takes a long time and there is a crashing problem in the application, it is called from the thread and ind, binay_img are obtained. 
        Obtaining ind, x_mm, y_mm and threshold image
        """
        #progress_callback.emit(count)

        ind_l, binary_img_l, enhanced_img_l = self.segmentation_using_com(self.beam_sum_l, self.seg_tresh, stop_callback) 
        binary_img_array_l = Image.fromarray(binary_img_l)
        binary_img_qt_l = ImageQt.ImageQt(binary_img_array_l)

        self.x_mm_l = self.pixels_to_mm(self.planned_center_l[0]-ind_l[0])
        self.y_mm_l = self.pixels_to_mm(self.planned_center_l[1]-ind_l[1])

        ind_r, binary_img_r, enhanced_img_r = self.segmentation_using_com(self.beam_sum_r, self.seg_tresh, stop_callback) 
        binary_img_array_r = Image.fromarray(binary_img_r)
        binary_img_qt_r = ImageQt.ImageQt(binary_img_array_r)

        self.x_mm_r = self.pixels_to_mm(self.planned_center_r[0]-ind_r[0])
        self.y_mm_r = self.pixels_to_mm(self.planned_center_r[1]-ind_r[1])
    
        self.y_mm_avg = self.average_anterior_err(self.y_mm_l, self.y_mm_r)
        self.target_err = self.targetting_err(self.x_mm_l, self.x_mm_r, self.y_mm_avg) 

        x_mm_l = my_formatter.format(self.x_mm_l)
        y_mm_l = my_formatter.format(self.y_mm_l)
        x_mm_r = my_formatter.format(self.x_mm_r)
        y_mm_r = my_formatter.format(self.y_mm_r)
        avr_ant_err = my_formatter.format(self.y_mm_avg)
        target_err = my_formatter.format(self.target_err)

        return binary_img_qt_l, binary_img_qt_r, x_mm_l, y_mm_l, x_mm_r, y_mm_r, avr_ant_err, target_err
        
    def average_anterior_err(self, y1, y2):
        """
        calculate average anterior error
        """
        avr_ant_err =  abs(y1 + y2)/2
        return avr_ant_err
       
    def targetting_err(self, x, y, z):
        """
        total targetting error (x2+y2+z2)kök
        """ 
        target_err = (math.sqrt((x*x)+(y*y)+(z*z)))
        return target_err
    
    def stop_flag(self):
        """
        Changing the flag to stop when the stop button is pressed
        """
        self.running = False

    #Frame Sum Script
    def calculate_background(self, background, count):
        background_norm = (1/count)*background
        return background_norm

    def find_plan_point(self, ref_img,count, stop_callback):
        ref_img_norm = (1/count)*ref_img
        ref_img_enhanced = self.enhance_refs(ref_img_norm)
        ref_img_binary = ref_img_enhanced > 150
        px,py = self.center_of_mass(ref_img_binary, stop_callback)
        return px,py

    def cut_ref_images(self, img):
        """
        [00]#####[01]#####[02]#####[03]#####[04]
        ##                ##                ## 
        ##                ##                ##
        [10]              [12]              [14]
        ##                ##                ##
        ##                ##                ##
        [20]#####[21]#####[22]#####[23]#####[24]
        """
        coordinates = []
        w = img.shape[1]//8
        v = w//2
        height= img.shape[0]
        midpy = img.shape[0]//2
        width = img.shape[1]
        xqtr1 = img.shape[1]//4
        midpx = img.shape[1]//2
        xqtr3 = 3*img.shape[1]//4

        im00 = img[0:w,0:w]#
        im01 = img[0:w,xqtr1-v:xqtr1+v]#
        im02 = img[0:w,midpx-v:midpx+v]#
        im03 = img[0:w,xqtr3-v:xqtr3+v]#
        im04 = img[0:w,-w:]#
        coordinates.append([0,0])
        coordinates.append([xqtr1-v,0])
        coordinates.append([midpx-v,0])
        coordinates.append([xqtr3-v,0])
        coordinates.append([width-w,0])

        im10 = img[midpy-v:midpy+v,0:w]#
        im12 = img[midpy-v:midpy+v,midpx-v:midpx+v]#
        im14 = img[midpy-v:midpy+v,-w:]#
        coordinates.append([0,midpy-v])
        coordinates.append([midpx-v,midpy-v])
        coordinates.append([width-w,midpy-v])

        im20 = img[-w:,0:w]#
        im21 = img[-w:,xqtr1-v:xqtr1+v]#
        im22 = img[-w:,midpx-v:midpx+v]#
        im23 = img[-w:,xqtr3-v:xqtr3+v]#
        im24 = img[-w:,-w:]#
        coordinates.append([0,height-w])
        coordinates.append([xqtr1-v,height-w])
        coordinates.append([midpx-v,height-w])
        coordinates.append([xqtr3-v,height-w])
        coordinates.append([width-w,height-w])

        ref_images=[im00,im01,im02,im03,im04,im10,im12,im14,im20,im21,im22,im23,im24]
        return ref_images,coordinates

    def find_ref_points(self, img, stop_callback):
        refp_img_list, cut_coords=self.cut_ref_images(img)
        ref_points = []
        for i,refp_img in enumerate(refp_img_list):
            enh_img = self.enhance_ref_img(refp_img)
            bin_img = self.segment_ref_img(enh_img)
            ref_px, ref_py = self.center_of_mass(bin_img, stop_callback)
            ref_p= (cut_coords[i][0]+ref_px,cut_coords[i][1]+ref_py)
            ref_points.append(ref_p)
        return ref_points

    def draw_ref_points(self, img, ref_points):
        drawing_img = utils.gray2rgb(utils.np2gray(img))
        for p in ref_points:
            drawing_img = utils.draw_ref_point(drawing_img,p)	
        return drawing_img
    """
    def draw_ref_lines(self, drawing_img, ref_points):
        utils.draw_ref_line_g(drawing_img,[ref_points[1],ref_points[6]])
        utils.draw_ref_line_g(drawing_img,[ref_points[3],ref_points[4]])
        intersect1 = utils.get_intersect(ref_points[1],ref_points[6],ref_points[3],ref_points[4])
        utils.draw_ref_point(drawing_img,intersect1)	
        utils.draw_ref_line_y(drawing_img,[ref_points[0],ref_points[7]])
        utils.draw_ref_line_y(drawing_img,[ref_points[2],ref_points[5]])
        intersect2 = utils.get_intersect(ref_points[0],ref_points[7],ref_points[2],ref_points[5])
        utils.draw_ref_point(drawing_img,intersect2)	
        return drawing_img, intersect1, intersect2
    """
    def draw_ref_lines_2(self, drawing_img,ref_points):
        """
        [0]#####[1]#####[2]#####[3]#####[4]
        ##       I      ##       I       ## 
        ##       I      ##       I       ##
        [5]------+------[6]------+------[7]
        ##       I      ##       I       ##
        ##       I      ##       I       ##
        [8]#####[9]####[10]#####[11]####[12]
        """
        utils.draw_ref_line_g(drawing_img,[ref_points[1],ref_points[9]])
        utils.draw_ref_line_g(drawing_img,[ref_points[5],ref_points[6]])
        intersect1 = utils.get_intersect(ref_points[1],ref_points[9],ref_points[5],ref_points[6])
        utils.draw_ref_point(drawing_img,intersect1)

        utils.draw_ref_line_y(drawing_img,[ref_points[0],ref_points[10]])
        utils.draw_ref_line_y(drawing_img,[ref_points[2],ref_points[8]])
        intersect2 = utils.get_intersect(ref_points[0],ref_points[10],ref_points[2],ref_points[8])
        utils.draw_ref_point(drawing_img,intersect2)	

        utils.draw_ref_line_g(drawing_img,[ref_points[3],ref_points[11]])
        utils.draw_ref_line_g(drawing_img,[ref_points[6],ref_points[7]])
        intersect3 = utils.get_intersect(ref_points[3],ref_points[11],ref_points[6],ref_points[7])
        utils.draw_ref_point(drawing_img,intersect3)
        utils.draw_ref_line_y(drawing_img,[ref_points[2],ref_points[12]])
        utils.draw_ref_line_y(drawing_img,[ref_points[4],ref_points[10]])
        intersect4 = utils.get_intersect(ref_points[2],ref_points[12],ref_points[4],ref_points[10])
        utils.draw_ref_point(drawing_img,intersect4)	
        return drawing_img, intersect1, intersect2, intersect3, intersect4

    def draw_img_borders(self, drawing_img,ref_points):
        """
        [0]#####[1]#####[2]#####[3]#####[4]
        ##   ________   ##   ________   ## 
        ##  |        |  ##  |        |  ##
        [5] |        |  [6] |        |  [7]
        ##  |________|  ##  |________|  ##
        ##              ##              ##
        [8]#####[9]####[10]#####[11]####[12]
        """
        t=60
        top_left_corner_1= (ref_points[0][0]+t,ref_points[0][1]+t)
        bottom_right_corner_1= (ref_points[10][0]-t,ref_points[10][1]-t)
        points1=[top_left_corner_1,bottom_right_corner_1]
        drawing_img = utils.draw_rectangle(drawing_img, points1)	
        top_left_corner_2= (ref_points[2][0]+t,ref_points[2][1]+t)
        bottom_right_corner_2= (ref_points[12][0]-t,ref_points[12][1]-t)
        points2=[top_left_corner_2,bottom_right_corner_2]
        drawing_img = utils.draw_rectangle(drawing_img, points2)	
        return drawing_img, points1, points2

    def gcoords2bcoords(self, borders, intersect1, intersect2, intersect3, intersect4):
        planned_center_1 = tuple(0.5*np.array(intersect1) + 0.5*np.array(intersect2) - borders[0][0])
        planned_center_2 = tuple(0.5*np.array(intersect3) + 0.5*np.array(intersect4) - borders[1][0])
        return planned_center_1, planned_center_2

    def find_and_draw_ref_points(self, ref_img, count, stop_callback):
        ref_img_norm = (1/count)*ref_img
        ref_points = self.find_ref_points(ref_img_norm, stop_callback)
        drawing_img = self.draw_ref_points(ref_img_norm, ref_points)
        drawing_img, intersect1, intersect2, intersect3, intersect4 = self.draw_ref_lines_2(drawing_img,ref_points)
        drawing_img, borders1, borders2 = self.draw_img_borders(drawing_img,ref_points)
        borders = [borders1, borders2]
        planned_center_1, planned_center_2 = self.gcoords2bcoords(borders, intersect1, intersect2, intersect3, intersect4)
        drawing_img = utils.show_images_in_designer(drawing_img)
        #cv2.imwrite(os.path.join(self.path, "ref_point_images.jpg"), drawing_img.astype(np.uint8))

        return drawing_img, planned_center_1, planned_center_2, borders
    
    def cut_images(self,img,border):
        (x1,y1) = border[0]
        (x2,y2) = border[1]
        cut_img = img[y1:y2,x1:x2]
        return cut_img   

    def sum_video(self, progress_callback, state_callback, stop_callback):
        vidObj = cv2.VideoCapture(self.Path) # Path to video file
        count = 0	# Used as counter variable
        time = 0	# in seconds
        state = 'find_ref_point'
        
        success, image = vidObj.read()
        ref_img = np.zeros([image.shape[0],image.shape[1]],dtype=np.float32)
        background = np.zeros([image.shape[0],image.shape[1]],dtype=np.float32)
        beam_sum = np.zeros([image.shape[0],image.shape[1]],dtype=np.float32)
        intersect1 = 0,0
        intersect2 = 0,0 
        drawing_img = None
        av_hist = []
        av_hist2 = []
        av_hist3 = []
        m_av_hist = []
        total_frame = vidObj.get(cv2.CAP_PROP_FRAME_COUNT)

        fps = vidObj.get(cv2.CAP_PROP_FPS)
        exp_time = 1000/fps
        while (success):
            if(success):
                count += 1
                progressbar_count = ((count/total_frame)*100)#for progress bar
                progress_callback.emit(progressbar_count)

                time = count*int(exp_time)/1000
                if(state == 'find_ref_point'):
                    ref_img += image[:,:,0]
                    if(time>5):
                        state = 'bgnd_calc'
                        #px,py = find_plan_point(ref_img,count) #normalize edilmiş bgnd
                        self.drawing_img, self.planned_center_l, self.planned_center_r, borders = self.find_and_draw_ref_points(ref_img, count, stop_callback)
                        state_callback.emit(self.drawing_img)
                        #print("Ref points are calculated as: x=%d, y=%d",px,py)
                elif(state == 'bgnd_calc'):
                    background += image[:,:,0]
                    if(time>36):
                        state = 'beam_detect'
                        b_norm = self.calculate_background(background,count) #normalize edilmiş bgnd
                elif(state == 'beam_detect'):
                    beam_frame = image[:,:,0]-b_norm
                    average = beam_frame.mean(axis=0).mean(axis=0) #turuncu grafik
                    av_hist.append(average)
                    average2 = image[:,:,0].mean(axis=0).mean(axis=0) #mavi grafik
                    av_hist2.append(average2)
                    m_av = utils.moving_avarage(av_hist, 100) #moving avarage
                    m_av_hist.append(m_av)
                    if(average > m_av+int(self.beam_thresh)): #bu framede beam onsa
                        beam_sum += beam_frame #frameleri topla
                        av_hist3.append(average)
                    else:
                        av_hist3.append(0)	
            success, image = vidObj.read()
            if self.running == False:
                stop_callback.emit(0)#stop_flag = 0 
                break

        self.beam_sum = beam_sum
        self.beam_sum_l = self.cut_images(beam_sum,borders[0])
        self.beam_sum_r = self.cut_images(beam_sum,borders[1])

        beam_sum_l_img =utils.gray2rgb(utils.np2gray(self.beam_sum_l))
        beam_sum_l_img = utils.show_images_in_designer(beam_sum_l_img)

        beam_sum_r_img =utils.gray2rgb(utils.np2gray(self.beam_sum_r))
        beam_sum_r_img = utils.show_images_in_designer(beam_sum_r_img)

        return beam_sum_l_img, beam_sum_r_img
    
    def segmentation_using_com(self, image, seg_thresh, stop_callback): 
        enhanced_img = self.enhance_sphere(image)
        smallest = enhanced_img.min(axis=0).min(axis=0)
        biggest = enhanced_img.max(axis=0).max(axis=0)
        cut_off = (biggest-smallest)*(seg_thresh/100)+smallest
        
        thresh = enhanced_img>cut_off 
        ind2 = self.center_of_mass(thresh, stop_callback) 
        #draft2 = utils.draw_circle(image,ind2,120)
        return ind2, thresh, enhanced_img
    
    def enhance_sphere(self, image):
        median_img = cv2.medianBlur(image, 3)
        closed_img = closing(median_img, disk(40))
        gauss_img = cv2.GaussianBlur(closed_img,(11,11),cv2.BORDER_DEFAULT)
        return gauss_img
        
    def enhance_refs(self, image):
        median_img = cv2.medianBlur(image, 5)
        closed_img = closing(median_img, disk(9))
        gauss_img = cv2.GaussianBlur(closed_img,(3,3),cv2.BORDER_DEFAULT)
        return gauss_img

    def enhance_ref_img(self, image):
        median_img = cv2.medianBlur(image, 5)
        closed_img = closing(median_img, disk(9))
        gauss_img = cv2.GaussianBlur(closed_img,(3,3),cv2.BORDER_DEFAULT)
        return gauss_img

    def segment_ref_img(self, image):
        thresh = threshold_otsu(image)
        return image>thresh

    def center_of_mass(self, binary_img, stop_callback):
        try:
            M = cv2.moments(binary_img.astype(np.uint8))
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        except:
            stop_callback.emit(1)#center_of_mass_flag = 1 

        return (cX,cY)

    def pixels_to_mm(self, pix_dist):
        image_mm = 110.0
        image_pixel = 880.0
        ratio = image_mm / image_pixel
        return pix_dist*ratio

    #SET FUNCTIONS
    def set_path(self, path_name):    
        self.Path = path_name

    def set_beam_thresh(self, beam_thresh):    
        self.beam_thresh = beam_thresh

    def set_seg_tresh(self, seg_tresh):    
        self.seg_tresh = seg_tresh