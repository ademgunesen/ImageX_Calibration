# Program To Read video
# and Extract Frames
import model.model as model
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
from skimage.filters import median
from skimage.morphology import disk, closing
import time
from time import sleep
import model.utils as utils


	
def calculate_background(background,count):
	background_norm = (1/count)*background
	return background_norm

# def moving_avarage(num_list, filter_size):
	# mov_average = 0
	# for i in range(-filter_size,-1):
		# try:
			# mov_average += num_list[i]
		# except:
			# mov_average += 0
	# return mov_average/filter_size
	   
# Function to extract frames

def sum_video(Path , exp_t, tresh):

	#print(Path)
	vidObj = cv2.VideoCapture(Path) # Path to video file
	count = 0	# Used as counter variable
	time = 0	# in seconds
	state = 'bgnd_calc'
	
	success, image = vidObj.read()
	background = np.zeros([image.shape[0],image.shape[1]])
	beam_sum = np.zeros([image.shape[0],image.shape[1]])
	av_hist = []
	av_hist2 = []
	m_av_hist = []

	while success:

		# vidObj object calls read
		# function extract frames
		if(success):
			
			count += 1
			#print(time)

			time = count*exp_t/1000
			if(state == 'bgnd_calc'):
				background += image[:,:,0]
				if(time>36):
					state = 'beam_detect'
					b_norm = calculate_background(background,count) #normalize edilmiş bgnd
			elif(state == 'beam_detect'):
				beam_frame = image[:,:,0]-b_norm
				average = beam_frame.mean(axis=0).mean(axis=0) #turuncu grafik
				av_hist.append(average)
				average2 = image[:,:,0].mean(axis=0).mean(axis=0) #mavi grafik
				av_hist2.append(average2)
				m_av = utils.moving_avarage(av_hist, 100) #moving avarage
				m_av_hist.append(m_av)
				if(average > m_av+tresh): #bu framede beam onsa
					#show_images([beam_frame],[average])
					beam_sum += beam_frame #frameleri topla

		success, image = vidObj.read()

	#plt.plot(av_hist2)
	#plt.savefig(path + '_mean.png')
	#plt.show(block=False)
	#print(count)#
	#plt.plot(av_hist)
	#plt.plot(m_av_hist)
	#plt.savefig(path + '_means.png') #graifkleri kaydet
	#plt.show(block=False)
	#utils.show_images([beam_sum],figname= path + '_beam_sum' + str(tresh)) #beam_sum görüntüle
	return beam_sum

def segmentation_using_peak(image): #olması gereken segmentation değimiş
	smallest = image.min(axis=0).min(axis=0)
	biggest = image.max(axis=0).max(axis=0)
	cut_off = (biggest-smallest)*0.75+smallest #cut_off hesapla
	#print(smallest)
	#print(biggest)
	#print(cut_off)
	ax = plt.hist(image.ravel(), bins = 256)
	plt.show()
	ind = np.unravel_index(np.argmax(image, axis=None), image.shape)  # returns a tuple of peak pixel
	#print(ind)
	closed = closing(image, disk(30))
	thresh = closed>cut_off
	ind2 = center_of_mass(thresh)
	draft = utils.draw_circle(beam_sum,ind2,120)
	#utils.show_images([image,image>cut_off,closed,closed>cut_off])
	
def segmentation_using_com(image): #bunu geometrik merkez yap
	im = model.FrameSumSumVideo()
	smallest = image.min(axis=0).min(axis=0)
	biggest = image.max(axis=0).max(axis=0)
	cut_off = (biggest-smallest)*0.60+smallest
	#print(smallest)
	#print(biggest)
	#print(cut_off)
	closed = closing(image, disk(40)) #küçük noiselardan kurtulma
	thresh = closed>cut_off #cut_offtan büyük olan
	ind2 = center_of_mass(thresh) #ışınlanan kürenin merkezinin x ve y indisleri
	draft2 = utils.draw_circle(image,ind2,120)
	draft3 = utils.draw_circle(image,(256,256),120)
	#utils.show_images([image,closed,thresh,draft2])
	#utils.show_images([thresh],figname= path + 'thresh')
	return ind2
	
def center_of_mass(thresh):
	M = cv2.moments(thresh.astype(np.uint8))
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])
	return (cX,cY)
	
def pixels_to_mm(pix_dist):
	image_mm = 100.0
	image_pixel = 512.0
	ratio = image_mm / image_pixel
	return pix_dist*ratio


if __name__ == '__main__':

	path='ucuncu denemeler/'
	file_name='512x512pixel100ms_48gainE2E_f2.8'
	#path='C:/Users/User/Downloads/aynalı e2e/'
	#file_name='aynalı e2e'
	exp_t=51
	
	start = time.time() #kronometre baslat
	beam_sum = sum_video(Path,exp_t,8) #sadece beam on olan framelerin toplamını bul
	#print(time.time() - start) #kronometre bitir
	#utils.save_var(beam_sum,"beam_sum")
	#beam_sum = utils.read_var("beam_sum")
	ind = segmentation_using_com(beam_sum) #center of massı bularak segmente et
	x_mm = pixels_to_mm(512/2-ind[0])
	y_mm = pixels_to_mm(512/2-ind[1])
	print(x_mm,y_mm)

