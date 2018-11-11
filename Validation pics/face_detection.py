#!/usr/bin/env python
# coding: utf-8

# In[81]:


import dlib
from PIL import Image
from skimage import io
import sys
img=sys.argv[1]
#import matplotlib
#matplotlib.use('GTK')
#matplotlib.use('Agg')
#import pygtk
#pygtk.require('3.0')
#import gtk
#from gtk import gdk

#import matplotlib
#matplotlib.use('GTKAgg')  # or 'GTK'
#from matplotlib.backends.backend_gtk import FigureCanvasGTK as FigureCanvas

#from numpy.random import random
#from matplotlib.figure import Figure
#import matplotlib.pyplot as plt
#matplotlib.use('Agg')
#from matplotlib.backends._backend_gdk import pixbuf_get_pixels_array
#from matplotlib.backends.backend_gtk import FigureCanvasGTK as FigureCanvas
#from matplotlib.backends.backend_gdk import RendererGDK, FigureCanvasGDK
#import matplotlib.pyplot as plt


def detect_faces(image):

    # Create a face detector
    face_detector = dlib.get_frontal_face_detector()

    # Run detector and get bounding boxes of the faces on image.
    detected_faces = face_detector(image, 1)
    face_frames = [(x.left(), x.top(),
                    x.right(), x.bottom()) for x in detected_faces]

    return face_frames

# Load image
img_path = img
#image = io.imread(img_path)
image=Image.open(img_path)
# Detect faces
detected_faces = detect_faces(image)

# Crop faces and plot
for n, face_rect in enumerate(detected_faces):
    #print(face)
    print(n)
    face = Image.fromarray(image).crop(face_rect)
#    plt.subplot(1, len(detected_faces), n+1)
#    plt.axis('off')
    #plt.imshow(face)
#    fim -a face
    face.save("%s.png" % (n+5))

