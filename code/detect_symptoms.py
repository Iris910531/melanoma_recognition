import numpy as np
import cv2

### Detecting the true melanoma symptoms - the largest contour as the symptom

def find_max_contours(img_original,img_open):
    black1 = np.zeros(img_original.shape, np.uint8)  
    white1 = np.ones(img_original.shape, np.uint8) * 255 
    (contours,hierarchy)=cv2.findContours(img_open.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    l_im = list(contours)
    l_im.sort(key=len, reverse=True)
    max_con  = cv2.drawContours(white1,[l_im[0]],-1,(0,0,255),2)
    return (max_con,l_im)