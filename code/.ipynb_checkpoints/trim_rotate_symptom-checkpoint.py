import numpy as np
import cv2
import math
import imutils
#trim out the melanoma symptom images and rotate it

def mask_symptom_images(closing3,box):
    rows=closing3.shape[0]
    cols=closing3.shape[1]
    channels=closing3.shape[2]
    mask=np.zeros(closing3.shape,dtype=np.uint8)
# Input the Coordinates of the Point
    roi_corners=np.array([[box[0],box[1],box[2],box[3]]],dtype=np.int32)
    channel_count=channels
    ignore_mask_color = (255,)*channel_count
# Create a Mask Layer
    cv2.fillPoly(mask,roi_corners,ignore_mask_color)
# Perform an AND operation for each pixel, with everything outside the mask area set to 0
    masked_image=cv2.bitwise_and(closing3,mask)
    #cv2.waitKey(0)
    return masked_image

# calculate rectangle's angle which the image need to be rotated
def calculate_angle( x1,  y1,  x2,  y2):
    angle = 0.0;
    dx = x2 - x1
    dy = y2 - y1
    if  x2 == x1:
        angle = math.pi / 2.0
        if  y2 == y1 :
            angle = 0.0
        elif y2 < y1 :
            angle = 3.0 * math.pi / 2.0
    elif x2 > x1 and y2 > y1:
        angle = math.atan(dx / dy)
    elif  x2 > x1 and  y2 < y1 :
        angle = math.pi / 2 + math.atan(-dy / dx)
    elif  x2 < x1 and y2 < y1 :
        angle = math.pi + math.atan(dx / dy)
    elif  x2 < x1 and y2 > y1 :
        angle = 3.0 * math.pi / 2.0 + math.atan(dy / -dx)
    return (angle * 180 / math.pi)


# Rotate the image according to the rectangle's angle 
def rotate_image(masked_image,angle):
    rotated = imutils.rotate_bound(masked_image, angle-90)
    return rotated

def crop_rotated_image(rotated,img_binary):
    bb = np.mean(rotated,axis=2)
    arr = bb.sum(axis=0)!=0
    lis=[]
    for i in range(len(arr)):
        if arr[i] == True: lis.append(i)
    rotated = rotated[:,lis,:3]
    arr1 = bb.sum(axis=1)!= 0 
    lis1 =[]
    for i in range(len(arr1)):
        if arr1[i] == True: lis1.append(i)
    rotated = rotated[lis1,:,:3]
    
    img_binary = img_binary[lis1,:] 
    img_binary = img_binary[:,lis]
    return rotated,img_binary