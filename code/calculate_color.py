import cv2
import numpy as np


### Calculate feature value for color(HSV and RGB) channel

def calculate_hsv(name):
    img = name
    # Convert BGR to HSV colorspace
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Split the channels - h,s,v
    h, s, v = cv2.split(hsv)
    # Initialize the color feature
    color_feature = []
    # N = h.shape[0] * h.shape[1]
    # The first central moment - average 
    h_mean = np.mean(h)  # np.sum(h)/float(N)
    s_mean = np.mean(s)  # np.sum(s)/float(N)
    v_mean = np.mean(v)  # np.sum(v)/float(N)
    color_feature.extend([h_mean, s_mean, v_mean])
    # The second central moment - standard deviation
    h_std = np.std(h)  # np.sqrt(np.mean(abs(h - h.mean())**2))
    s_std = np.std(s)  # np.sqrt(np.mean(abs(s - s.mean())**2))
    v_std = np.std(v)  # np.sqrt(np.mean(abs(v - v.mean())**2))
    color_feature.extend([h_std, s_std, v_std])
    # The third central moment - the third root of the skewness
    h_skewness = np.mean(abs(h - h.mean())**3)
    s_skewness = np.mean(abs(s - s.mean())**3)
    v_skewness = np.mean(abs(v - v.mean())**3)
    h_thirdMoment = h_skewness**(1./3)
    s_thirdMoment = s_skewness**(1./3)
    v_thirdMoment = v_skewness**(1./3)
    color_feature.extend([h_thirdMoment, s_thirdMoment, v_thirdMoment])
    return color_feature

def calculate_rgb(name):
    img = name
    # Convert BGR to HSV colorspace
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Split the channels - h,s,v
    r, g, b = cv2.split(rgb)
    # Initialize the color feature
    color_feature = []
    # N = h.shape[0] * h.shape[1]
    # The first central moment - average 
    r_mean = np.mean(r)  # np.sum(h)/float(N)
    g_mean = np.mean(g)  # np.sum(s)/float(N)
    b_mean = np.mean(b)  # np.sum(v)/float(N)
    color_feature.extend([r_mean, g_mean, b_mean])
    # The second central moment - standard deviation
    r_std = np.std(r)  # np.sqrt(np.mean(abs(h - h.mean())**2))
    g_std = np.std(g)  # np.sqrt(np.mean(abs(s - s.mean())**2))
    b_std = np.std(b)  # np.sqrt(np.mean(abs(v - v.mean())**2))
    color_feature.extend([r_std, g_std, b_std])
    # The third central moment - the third root of the skewness
    r_skewness = np.mean(abs(r - r.mean())**3)
    g_skewness = np.mean(abs(g - g.mean())**3)
    b_skewness = np.mean(abs(b - b.mean())**3)
    r_thirdMoment = r_skewness**(1./3)
    g_thirdMoment = g_skewness**(1./3)
    b_thirdMoment = b_skewness**(1./3)
    color_feature.extend([r_thirdMoment, g_thirdMoment, b_thirdMoment])

    return color_feature