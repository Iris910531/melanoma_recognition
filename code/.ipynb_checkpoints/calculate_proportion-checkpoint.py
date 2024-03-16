### Calculate the Proportion of the Tumor in the Image

# Calculate the Area of the Image 
def image_area(img_original):
    sp = img_original.shape
    sp1 = sp[0]#height(rows) of image
    sp2 = sp[1]#width(colums) of image
    sp3 = sp[2]#the pixels value is made up of three primary colors
    area_sp = sp1 * sp2
    return area_sp

# Calculate the Proportion of the Tumor in the Image
def tumor_proportion(area_m,area_sp):
    Proportion = area_m / area_sp
    return Proportion