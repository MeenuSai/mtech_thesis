#!/usr/bin/env python
# coding: utf-8

# In[81]:


import dlib
from PIL import Image
from skimage import io
import sys
img=sys.argv[1]


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
image = io.imread(img_path)
#image=Image.open(img_path)
# Detect faces
detected_faces = detect_faces(image)
 

# Crop faces and plot
for n, face_rect in enumerate(detected_faces):
    print(n)
    face = Image.fromarray(image).crop(face_rect)
    face.save("%s.png" % (n+5))
    
 
# #!/usr/bin/env python
# # coding: utf-8



# import dlib
# from PIL import Image
# from skimage import io
# import sys
# img=sys.argv[1]

# def detect_faces(image):

#     # Create a face detector
#     face_detector = dlib.get_frontal_face_detector()

#     # Run detector and get bounding boxes of the faces on image.
#     detected_faces = face_detector(image, 1)
#     face_frames = [(x.left(), x.top(),
#                     x.right(), x.bottom()) for x in detected_faces]

#     return face_frames

# img_path = img
# image = io.imread(img_path)
# detected_faces = detect_faces(image)

# for n, face_rect in enumerate(detected_faces):
#     face = Image.fromarray(image).crop(face_rect)
#     cropFileName=str(img[:-4])+'_cropped.png'
#     face.save('processed/'+cropFileName)
#     print('Image Cropped, New File name is: '+ str(cropFileName))
