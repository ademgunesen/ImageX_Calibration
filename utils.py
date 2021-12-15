import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
from skimage.filters import median
from skimage.morphology import disk
import time
import pickle

def save_var(var, file_name):
	'''
	Saves any type of variable with the given filename(can be a path)
	'''
	out_file = open(file_name,'wb')
	pickle.dump(var,out_file)
	out_file.close()
	
def read_var(file_name):   
	infile = open(file_name,'rb')
	var = pickle.load(infile)
	infile.close()
	return var
	
def show_images(images: list, titles: list="Untitled	", colorScale='gray', figname="unnamed", rows = 0, columns = 0) -> None:
	n: int = len(images)
	if rows == 0:
		rows=int(math.sqrt(n))
	if columns == 0:
		columns=(n/rows)
	f = plt.figure()
	for i in range(n):
		# Debug, plot figure
		f.add_subplot(rows, columns, i + 1)
		plt.imshow(images[i], cmap=colorScale)
		plt.title(titles[i])
	plt.savefig(figname + '.png')
	plt.show(block=True)
	
def bool2rgb(bool_img):
    h=bool_img.shape[0]
    w=bool_img.shape[1]
    gray_img = bool_img*255
    rgb_img = np.zeros((h,w,3), np.uint8)
    rgb_img[:,:,0] = gray_img
    rgb_img[:,:,1] = gray_img
    rgb_img[:,:,2] = gray_img
    return rgb_img

def gray2rgb(gray_img):
	h=gray_img.shape[0]
	w=gray_img.shape[1]
	rgb_img = np.zeros((h,w,3), np.uint8)
	rgb_img[:,:,0] = gray_img
	rgb_img[:,:,1] = gray_img
	rgb_img[:,:,2] = gray_img
	return rgb_img

def np2gray(np_img):
	#img = img_as_ubyte(np_img)
	img = cv2.normalize(src=np_img, dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
	return img

def moving_avarage(num_list, filter_size):
	mov_average = 0
	if(len(num_list) > filter_size):
		mov_average = sum(num_list[-filter_size:-1])/filter_size
	return mov_average

def draw_circle(image,cxy,r):	

	cxy = (int(cxy[0]), int(cxy[1])) #eskisinde yok   
	color = (0, 0, 0)
	# Line thickness of 2 px
	thickness = 2 
	# Using cv2.circle() method
	# Draw a circle with blue line borders of thickness of 2 px
	ret_image = cv2.circle(image, cxy, r, color, thickness)
	return ret_image

def draw_ref_point(image,cxy):	   
	color = (255, 0, 0)
	# Line thickness of 2 px
	thickness = 1 
	r = 5 #radius
	cxy = (int(cxy[0]), int(cxy[1])) 
	# Using cv2.circle() method
	# Draw a circle with blue line borders of thickness of 2 px
	ret_image = cv2.circle(image, cxy, r, color, thickness)
	return ret_image

def draw_ref_line_g(drawing_img,lpoints):
	ret_image = cv2.line(drawing_img,lpoints[0],lpoints[1],(0,255,0),1)
	return ret_image

def draw_ref_line_y(drawing_img,lpoints):
	ret_image = cv2.line(drawing_img,lpoints[0],lpoints[1],(255,255,0),1)
	return ret_image

def get_intersect(a1, a2, b1, b2):
    """ 
    Returns the point of intersection of the lines passing through a2,a1 and b2,b1.
    a1: [x, y] a point on the first line
    a2: [x, y] another point on the first line
    b1: [x, y] a point on the second line
    b2: [x, y] another point on the second line
    """
    s = np.vstack([a1,a2,b1,b2])        # s for stacked
    h = np.hstack((s, np.ones((4, 1)))) # h for homogeneous
    l1 = np.cross(h[0], h[1])           # get first line
    l2 = np.cross(h[2], h[3])           # get second line
    x, y, z = np.cross(l1, l2)          # point of intersection
    if z == 0:                          # lines are parallel
        return (float('inf'), float('inf'))
    return (x/z, y/z)