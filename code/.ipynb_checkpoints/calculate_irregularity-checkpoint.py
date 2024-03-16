import numpy as np
import cv2
import imutils
import math
### Calculate feature value for Irregularity


def draw_rectangle(img_maxcon,list_con):
    img_copy = np.copy(img_maxcon)
    # Draw Rectangle and Draw the minimum bounding rectangle for angle function
    rect = cv2.minAreaRect(list_con[0])
    box = cv2.cv.Boxpoints() if imutils.is_cv2()else cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(img_copy, [box], 0, (0, 0, 255), 2)
    
    # Calculate Rectangle Area
    side1=math.sqrt((box[0][0]-box[1][0])**2+(box[0][1]-box[1][1])**2)
    side2=math.sqrt((box[1][0]-box[2][0])**2+(box[1][1]-box[2][1])**2)
    area_rect=side1*side2
    return (area_rect,box,img_copy)


def draw_ellipse(list_con,img_copy):
    ellipse = cv2.fitEllipse(list_con[0])
    cv2.ellipse(img_copy, ellipse, (255, 0, 255), 2)
    ellipse_center = (int(ellipse[0][0]), int(ellipse[0][1]))  # Ellipse Center Coordinates
    cv2.circle(img_copy, ellipse_center, 1, (255, 0, 255), 2)
    
    # Calculate Ellipse Area
    area_ell=(ellipse[1][0]/2)*(ellipse[1][1]/2)*3.1415926
    return (area_ell,img_copy)

# Calculate Irregularity
def calculate_irregularity_value(list_con,area_ell,area_rect):
    area_m=0
    for i in list_con:
        area_m += cv2.contourArea(i) # The variable area_m represents the approximate area of the tumor.
    ae_diff = abs(area_m - area_ell)/area_m
    ar_diff = abs(area_m - area_rect)/area_m
    return (area_m,ae_diff,ar_diff)
