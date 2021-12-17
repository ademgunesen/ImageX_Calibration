# Program To Read video
# and Extract Frames
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
from skimage.filters import median
from skimage.morphology import disk


def show_images(images: list, titles: list="Untitled	", colorScale='gray', rows = 0, columns = 0) -> None:
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
	plt.show(block=True)


# Function to extract frames
def FrameCapture(path):
	
	# Path to video file
	vidObj = cv2.VideoCapture(path)

	# Used as counter variable
	count = 0

	# checks whether frames were extracted
	success = 1

	background = np.zeros([500,512])
	
	while success:

		# vidObj object calls read
		# function extract frames
		success, image = vidObj.read()

		# Saves the frames with frame-count
		#cv2.imwrite("frame%d.jpg" % count, image)
		if(count>0 and count<600):
			background += image[:,:,0]
			#print(count)
		if(count==600):
			background_norm = (1/600)*background
			#show_images([background_norm, background])
			print("background has been estimated")
		if(count>735):
			front_img = image[:,:,0] - background_norm
			#front_img_filt = img_filt = median(front_img, disk(5))
			print("1 frame islendi")
			#show_images([image[:,:,0], front_img,front_img>10,front_img>20])
		count += 1

# Driver Code
if __name__ == '__main__':

	# Calling the function
	#C:\Users\User\Downloads\Işınlama ilk denemeler
	FrameCapture("aynali denemeler\\cropped_center_51ms_48db.avi")
