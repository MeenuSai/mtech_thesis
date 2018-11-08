# -*- coding: utf-8 -*-

import sys
import os
import os.path
import dlib
from skimage import io
import cv2
import numpy as np
# from predict_gender import*

# os.remove("a.txt")
file = open("a.txt", 'a')
#os.system('python crfasrnn_demo.py')
# image_name='/home/bhavana/code/crfasrnn/python-scripts/30.jpg'
# seg_name='/home/bhavana/code/crfasrnn/python-scripts/output_30.png'
good_images=[]
source_input_folder = "/Macintosh HD⁩/Users⁩/meenusai⁩/Documents/water-depth/Input/"
seg_input_folder = "/Macintosh HD⁩/Users⁩/meenusai⁩/Documents/water-depth/output1/"
source_imgs = []
seg_imgs = []
valid_images = [".jpg",".gif",".png",".tga"]
for f in os.listdir(source_input_folder):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue
    source_imgs.append(os.path.join(source_input_folder,f))

for f in os.listdir(seg_input_folder):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue
    seg_imgs.append(os.path.join(seg_input_folder,f))

source_imgs = sorted(source_imgs)
seg_imgs = sorted(seg_imgs)

for k in range(0, len(source_imgs)):
	#print source_imgs
	#print seg_imgs[i]
	image=cv2.imread(source_imgs[k])
	img=image.copy()
	seg_img = cv2.imread(seg_imgs[k])

	seg_img=cv2.resize(seg_img,(img.shape[1],img.shape[0]))
	#cv2.imshow('Resize Human Segmented Image',seg_img) 
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	#cv2.imshow('Gray Color of Original Image',gray) 
	gray_seg = cv2.cvtColor(seg_img, cv2.COLOR_BGR2GRAY)
	#cv2.imshow('Gray Color of Resized Segemented Image',gray_seg) 
	(thresh, im_bw) = cv2.threshold(gray_seg, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	detector = dlib.get_frontal_face_detector()

	#win = dlib.image_window()
	faces=[]
	dets = detector(img, 1)

	if len(dets)==0:
	   print "no face found"
	   continue
	   # exit(0)

	print("Number of faces detected: {}".format(len(dets)))
	for i, d in enumerate(dets):
	    print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
	        i, d.left(), d.top(), d.right(), d.bottom()))
	    faces.append([d.left(),d.top(),d.right(),d.bottom()])
	avg_height=None
	depth_values=[]
	for f in faces:
		x=f[0]
		y=f[1]
		x1=f[2]
		y1=f[3]
		#face_part=img[y:y1,x;x1]
		face=img[y:y1,x:x1]
		image_part=img[y:seg_img.shape[1]-1, x:x1] 
		roi_color =im_bw[y:seg_img.shape[1]-1, x:x1] 	
		cv2.imwrite('face.jpg',face)
		cv2.imwrite('roi_color.jpg',roi_color)
		cv2.imwrite('image_part.jpg',image_part)
		cv2.imwrite('main.jpg',img)
		cv2.rectangle(img, (x, y), (x1, y1), (255,0,0), 2)
		cv2.imwrite('face_bounding_box.jpg',img)
		
		try:
		 gender=get_gender_final('face.jpg')
		except Exception as e:
		 print "exception "+str(e)
		 exit(0)


		if gender=='Male':
			avg_height=5.9
		else:
			avg_height=5.9
		file.write('\nGender of detected face :'+ str(gender) + "\n")  
		file.write('\nAverage Height :'+ str(avg_height)+ "\n")  
		human_avg_height=avg_height	
		for i in range(0,roi_color.shape[0]-10):
			if np.mean(roi_color[i:i+5,:]/255.0)==0:
				human_height = 7* abs(y1-y) 
			 
				human_part=image_part[0:i,0:human_height]		
				depth_in_pixel=abs(i-human_height)
				#print "depth of water in pixels:",depth_in_pixel
				percent_in_water=float(depth_in_pixel)/human_height
				#print 'percent_in_water:',percent_in_water
				depth_of_water=(avg_height*percent_in_water) + 2
	    			#print 'depth in feet:',depth_of_water
				#print "***********"
				depth_values.append(depth_of_water)
				#file.write('Water depth in feet for this detected human:' + str(depth_of_water) + "\n")
	file.write("\n"+source_imgs[k]+"\n")
	file.write('\nApproximate depth of water level :\n' + str(np.mean(depth_values)) +'-ft\n\n\n')
        #file.write(str(np.mean(depth_values)) +'-ft\n\n\n')
	#good_images.append(source_imgs[i])
        #if len(depth_values)==0:
	#file.write(str("failed to find depth"))
	#else:
	#file.write("\nAproximated water level in feet is:"+ str(np.mean(depth_values)) +'-ft\n')
os.system("clear")

