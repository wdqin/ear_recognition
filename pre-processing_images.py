
# coding: utf-8

# In[29]:


#processing image(s)
from reading_images_from_folder import *
import matplotlib.pyplot as plt

def processing_images(image,median = True, median_ksize = 5, hist_equal = True,resize = False, resize_ratio = 1):
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    if(median):
        image = cv2.medianBlur(image,median_ksize)
    if(resize):
        image = resize_image(image,resize_ratio)
    if(hist_equal):
        image = cv2.equalizeHist(image)
    return image
def resize_image(image,ratio):
    height = image.shape[0]
    width = image.shape[1]
    new_height = int(height*ratio)
    new_width = int(width*ratio)
    image = cv2.resize(image,(new_width,new_height))
    return image
def crop_image(image,x_left,y_top,x_right,y_bottom):
    image = image[y_top:y_bottom,x_left:x_right]
    return image

