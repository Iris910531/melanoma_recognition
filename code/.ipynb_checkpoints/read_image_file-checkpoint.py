import cv2

def read_image(filename):
    img_ori = cv2.imread(filename,1)
    return img_ori