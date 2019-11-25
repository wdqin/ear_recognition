
# coding: utf-8

# In[25]:


#reading images from one folder path
import os, os.path
import cv2

def get_list_of_file_names(folder_path):
    result = os.listdir(folder_path)
    result.sort()
    return result

def get_image_from_file_name(folder_path,file_name):
    loading_path = folder_path+file_name
    image = cv2.imread(loading_path)
    return image

def get_list_of_images(folder_path):
    file_name_list = get_list_of_file_names(folder_path)
    results = []
    for file_name in file_name_list:
        results.append(get_image_from_file_name(folder_path,file_name))
    return results

