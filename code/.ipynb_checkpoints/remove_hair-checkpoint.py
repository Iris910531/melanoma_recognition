import cv2

### Preprocessing to remove hair


def remove_hair_closing(img_ori):
    if img_ori[0][0][0] == 255 : # if this line does not exist, kernal will dead due to high computational cost.
        for i in range(0,img_ori.shape[0],1) :
            for j in range(0,img_ori.shape[1],1) :
                if img_ori[i][j][0] == 255 and  img_ori[i][j][1] == 255 and img_ori[i][j][2] == 255: # white edge -> black edge
                    img_ori[i][j][0] = 0
                    img_ori[i][j][1] = 0
                    img_ori[i][j][2] = 0
    # Use cv2.getStructuringElement() to generate structural elements of different shapes 
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (10, 5)) # Cross Structure
    # The second and third parameters are the kernel size and the anchor point position, respectively. 

    # Perform closing operation use cross structure
    img_closing = cv2.morphologyEx(img_ori, cv2.MORPH_CLOSE, kernel)
    return (img_ori, img_closing)

def image_binarization(img_closing):
    im2 = np.mean(img_closing,axis=2)
    blur = cv2.GaussianBlur(im2,(3,3),0)
    blur = blur.astype("uint8")
    ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # Binarization
    img_binary = np.where(im2 >= ret3,0, 1)
    return img_binary

# Open operation: Erosion followed by dilation to fill in white spots
def remove_hair_opening(img_binary):
    img_binary = img_binary.astype('uint8')
# Use cv2.getStructuringElement() to generate structural elements of different shapes
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (20, 20)) # Cross Structure
# Perform open operation use cross structure
    opening = cv2.morphologyEx(img_binary , cv2.MORPH_OPEN, kernel)
    return opening