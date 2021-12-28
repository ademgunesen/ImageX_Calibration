from sys import flags
import model.utils as utils

#frame_sum
import math 
import os
import cv2
import numpy as np
from skimage.morphology import disk, closing

from PIL import Image, ImageQt

from PyQt5.QtCore import QObject
my_formatter = "{0:.2f}"
class Model(QObject):
    def __init__(self, controller):
        super().__init__()
        """
        definition of all variables used
        """
        self._controller = controller

        #SET VARIABLES
        self.Path = ' '
        self.path = ' '
        self.exp_time = 0
        self.beam_thresh = 0

        self.beam_sum = 0
        self.beam_sum_img = 0
        self.binary_img = 0
        self.ind = 0

        self.binary_img_qt = 0
        self.image_qt = 0

        self.planned_center = 0
        self.x_mm = 0
        self.y_mm = 0
        self.avr_ant_err = 0
        self.target_err = 0

        self.count = 0

        self.seg_tresh = ' '
        self.success = ' '

        self.running = True
        self.text = False

    def frame_sum_thread(self, exp_time, beam_thresh, ref_point_thresh):
        """
        Since sum_video takes a long time, it is called from the thread and beam_sum is obtained
        """
        self.beam_sum, intersect1, intersect2, drawing_img = self.sum_video(self.Path, exp_time, beam_thresh, ref_point_thresh)
        self.planned_center = tuple(0.5*np.array(intersect1) + 0.5*np.array(intersect2))
        self.stop_flag()

    def threshold_thread(self, seg_tresh):
        """
        Since segmentation takes a long time and there is a crashing problem in the application, it is called from the thread and ind, binay_img are obtained. 
        """
        self.ind, self.binary_img, enhanced_img = self.segmentation_using_com(self.beam_sum, seg_tresh) 
        self.calculate_xy_img()
        
    def calculate_xy_img(self):
        """
        Obtaining ind, x_mm, y_mm and threshold image
        """
        binary_img_array = Image.fromarray(self.binary_img)
        self.binary_img_qt = ImageQt.ImageQt(binary_img_array)

        x_mm = self.pixels_to_mm(self.planned_center[0]-self.ind[0])
        y_mm = self.pixels_to_mm(self.planned_center[1]-self.ind[1])

        #self.average_anterior_err(y_mm, y_mm)
        self.targetting_err(x_mm, x_mm, y_mm) 

        self.x_mm = my_formatter.format(x_mm)
        self.y_mm = my_formatter.format(y_mm)

        self._controller.thresh_image_results()  

    def average_anterior_err(self, y1, y2):
        """
        calculate average anterior error
        """
        avr_ant_err =  (y1 + y2)/2
        self.avr_ant_err = my_formatter.format(avr_ant_err)
        return avr_ant_err
       
    def targetting_err(self, x, y, z):
        """
        total targetting error (x2+y2+z2)kök
        """
        avr_ant_err = self.average_anterior_err(z, z)
        z = avr_ant_err
        target_err = (math.sqrt(pow(x, 2)+pow(y, 2)+pow(z, 2)))
        self.target_err = my_formatter.format(target_err)

    def stop_flag(self):
        """
        Changing the flag to stop when the stop button is pressed
        """
        self.running = False

    def reset_video_variables(self):
        """
        stop butonun  basılınca değerlerin sıfırlanaması
        """
        self.beam_sum = 0
        self.ind = 0

        self.x_mm = 0
        self.y_mm = 0

    def first_video_image(self, Path):
        """
        finds the first frame of the selected video
        """
        vidObj = cv2.VideoCapture(Path)
        success, image = vidObj.read()
        self.image_qt = utils.show_images_in_designer(image)
        self._controller.show_first_image()

    #Frame Sum Script
    def calculate_background(self, background, count):
        background_norm = (1/count)*background
        return background_norm

    def find_plan_point(self, ref_img,count):
        ref_img_norm = (1/count)*ref_img
        ref_img_enhanced = self.enhance_refs(ref_img_norm)
        ref_img_binary = ref_img_enhanced > 150
        px,py = self.center_of_mass(ref_img_binary)
        return px,py

    def find_ref_points(self, bin_img):
        ref_points = []
        w = 100
        v = w//2
        width = bin_img.shape[1]
        height = bin_img.shape[0]
        midpx = bin_img.shape[0]//2
        midpy = bin_img.shape[1]//2
        im00 = bin_img[0:w,0:w]
        im01 = bin_img[0:w,midpx-v:midpx+v]
        im02 = bin_img[0:w,-w:]
        im10 = bin_img[midpy-v:midpy+v,0:w]
        im11 = bin_img[midpy-v:midpy+v,midpx-v:midpx+v]
        im12 = bin_img[midpy-v:midpy+v,-w:]
        im20 = bin_img[-w:,0:w]
        im21 = bin_img[-w:,midpx-v:midpx+v]
        im22 = bin_img[-w:,-w:]
        
        ref_px00, ref_py00 = self.center_of_mass(im00)
        ref_px01, ref_py01 = self.center_of_mass(im01)
        ref_px02, ref_py02 = self.center_of_mass(im02)
        ref_px10, ref_py10 = self.center_of_mass(im10)
        #ref_px11, ref_py11 = center_of_mass(im11)
        ref_px12, ref_py12 = self.center_of_mass(im12)
        ref_px20, ref_py20 = self.center_of_mass(im20)
        ref_px21, ref_py21 = self.center_of_mass(im21)
        ref_px22, ref_py22 = self.center_of_mass(im22)

        ref_p00 = (ref_px00, ref_py00)
        ref_p01 = (midpx-v + ref_px01, ref_py01)
        ref_p02 = (width-w + ref_px02, ref_py02)
        ref_p10 = (ref_px10, midpy-v + ref_py10)
        #ref_p11 = 
        ref_p12 = (width-w + ref_px12, midpy-v + ref_py12)
        ref_p20 = (ref_px20, height-w + ref_py20)
        ref_p21 = (midpx-v + ref_px21, height-w + ref_py21)
        ref_p22 = (width-w + ref_px22, height-w + ref_py22)
        ref_points = [ref_p00,ref_p01,ref_p02,ref_p10,ref_p12,ref_p20,ref_p21,ref_p22]
        return ref_points

    def draw_ref_points(self, bin_img, ref_points):
        drawing_img = utils.bool2rgb(bin_img)
        for p in ref_points:
            drawing_img = utils.draw_ref_point(drawing_img,p)	
        return drawing_img

    def draw_ref_lines(self, drawing_img,ref_points):
        utils.draw_ref_line_g(drawing_img,[ref_points[1],ref_points[6]])
        utils.draw_ref_line_g(drawing_img,[ref_points[3],ref_points[4]])
        intersect1 = utils.get_intersect(ref_points[1],ref_points[6],ref_points[3],ref_points[4])
        utils.draw_ref_point(drawing_img,intersect1)	
        utils.draw_ref_line_y(drawing_img,[ref_points[0],ref_points[7]])
        utils.draw_ref_line_y(drawing_img,[ref_points[2],ref_points[5]])
        intersect2 = utils.get_intersect(ref_points[0],ref_points[7],ref_points[2],ref_points[5])
        utils.draw_ref_point(drawing_img,intersect2)	
        return drawing_img, intersect1, intersect2

    def find_and_draw_ref_points(self, ref_img, count, ref_point_thresh):
        ref_img_norm = (1/count)*ref_img
        ref_img_enhanced = self.enhance_refs(ref_img_norm)
        ref_img_binary = ref_img_enhanced > int(ref_point_thresh)
        ref_points = self.find_ref_points(ref_img_binary)
        drawing_img = self.draw_ref_points(ref_img_binary,ref_points)
        drawing_img, intersect1, intersect2 = self.draw_ref_lines(drawing_img,ref_points)
        self.drawing_img = utils.show_images_in_designer(drawing_img)
        #cv2.imwrite(os.path.join(self.path, "ref_point_images.jpg"), drawing_img.astype(np.uint8))
        self._controller.show_second_image()
        return drawing_img, intersect1, intersect2
    
    def sum_video(self, Path , exp_time, beam_thresh, ref_point_thresh):
        vidObj = cv2.VideoCapture(Path) # Path to video file
        count = 0   # Used as counter variable
        time = 0    # in seconds
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
        while (success):
            #print(success)
            if(success):
                count += 1
                #self._controller.set_progresbar(count/55)#for progress bar
                time = count*int(exp_time)/1000
                if(state == 'find_ref_point'):
                    ref_img += image[:,:,0]
                    if(time>5):
                        state = 'bgnd_calc'
                        #px,py = find_plan_point(ref_img,count) #normalize edilmiş bgnd
                        drawing_img, intersect1, intersect2 = self.find_and_draw_ref_points(ref_img,count, ref_point_thresh)
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
                    if(average > m_av+int(beam_thresh)): #bu framede beam onsa
                        beam_sum += beam_frame #frameleri topla
                        av_hist3.append(average)
                    else:
                        av_hist3.append(0)	
            success, image = vidObj.read()
            self.success = success
            if self.running == False:
                break

        self.beam_sum_img =utils.gray2rgb(utils.np2gray(beam_sum))#convert a nparray to 0-255 normalize
        self.beam_sum_img = utils.show_images_in_designer(self.beam_sum_img)
        #self.stop_flag()

        if self.success == False:
            self._controller.show_beam_sum_image()#QObject::killTimer: Timers cannot be stopped from another thread!!!
            
        return beam_sum, intersect1, intersect2, drawing_img
    
    def segmentation_using_com(self, image, seg_thresh): 
        enhanced_img = self.enhance_sphere(image)
        smallest = enhanced_img.min(axis=0).min(axis=0)
        biggest = enhanced_img.max(axis=0).max(axis=0)
        cut_off = (biggest-smallest)*(seg_thresh/100)+smallest
        
        thresh = enhanced_img>cut_off 
        ind2 = self.center_of_mass(thresh) 
        draft2 = utils.draw_circle(image,ind2,120)
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

    def center_of_mass(self, binary_img):
        try:
            M = cv2.moments(binary_img.astype(np.uint8))
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        except:
            self._controller.warning_video_taken()

        return (cX,cY)

    def pixels_to_mm(self, pix_dist):
        image_mm = 110.0
        image_pixel = 880.0
        ratio = image_mm / image_pixel
        return pix_dist*ratio

    #SET FUNCTIONS
    def set_path(self, path_name):
        self.Path = path_name

    def set_text (self, flag):
        self.text = flag

    def set_count(self, cnt):
        self.count = cnt