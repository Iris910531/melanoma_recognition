import cv2
from skimage import feature
import numpy as np

def calculate_glcm(crop_img):
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

# List of pixel pair distance offsets - here 1 in each direction
# List of pixel pair angles in radians
    graycom = feature.graycomatrix(gray, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], levels=256)
# Find the GLCM properties
    contrast = feature.graycoprops(graycom, 'contrast')
    dissimilarity = feature.graycoprops(graycom, 'dissimilarity')
    homogeneity = feature.graycoprops(graycom, 'homogeneity')
    energy = feature.graycoprops(graycom, 'energy')
    correlation = feature.graycoprops(graycom, 'correlation')
    return(contrast,dissimilarity,homogeneity,energy,correlation)