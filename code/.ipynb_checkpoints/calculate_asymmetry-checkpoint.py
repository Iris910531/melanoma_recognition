import numpy as np

### Calculate feature value for Asymmetry

def calculate_symmetry(crop_img_bin):
    crop_img_bin=crop_img_bin/255
    box = [[0,crop_img_bin.shape[0]], [0, 0],
      [crop_img_bin.shape[1], 0], [crop_img_bin.shape[0],crop_img_bin.shape[1]]]
    
    cut_leftup = crop_img_bin[box[2][1]:int((box[0][1]-box[2][1])/2+box[2][1]), box[0][0]:int((box[2][0]- box[0][0])/2+ box[0][0])]
    area_leftup = cut_leftup.sum()
    
    cut_rightup = crop_img_bin[box[2][1]:int((box[0][1]-box[2][1])/2+box[2][1]),int((box[2][0]- box[0][0])/2+ box[0][0]):box[2][0]]
    area_rightup = cut_rightup.sum()
    
    cut_leftbottom = crop_img_bin[int((box[0][1]-box[2][1])/2+box[2][1]):box[0][1],box[0][0]:int((box[2][0]- box[0][0])/2+ box[0][0])]
    area_leftbottom = cut_leftbottom.sum()

    cut_rightbottom = crop_img_bin[int((box[0][1]-box[2][1])/2+box[2][1]):box[0][1],int((box[2][0]- box[0][0])/2+ box[0][0]):box[2][0]]
    area_rightbottom = cut_rightbottom.sum()
    
    list_area=[area_rightup,area_rightbottom,area_leftup,area_leftbottom]
    for i in range(4):
        list_area[i] = list_area[i]/(crop_img_bin.shape[0]*crop_img_bin.shape[1]/4)
    return np.std(list_area)