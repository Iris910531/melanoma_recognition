import numpy as np

### Removing areas unrelated to the peripheral melanoma lesions
def diagonal_direction(img, path_values, path, index) :
    # Obtain the Center Point of the Image
    height, width = img.shape
    height = int(height)
    width = int(width)
    max_ = 50

    # calculate image size in order to determine the steps Forward
    h = int(height/(max_*2))
    w = int(width/(max_*2))
    
    # Direction of steps (Top Left, Top Right, Bottom Left, Bottom Right)
    directions = [[-h, -w], [-h, w], [h, -w], [h, w]]
    x = int(height/2)
    y = int(width/2)
    for i in range(int(max_)):
        path.append((x, y))
        path_values.append(img[x, y])
        x += directions[index][0]
        y += directions[index][1]
        if not (0 <= x < height and 0 <= y < width):
            break
    # print('往', direction, '方向的路徑：', path)


def border_junction(path_values):
    n = np.array(path_values).shape[0]
    path_values = np.array(path_values)
    count=0
    for i in range(n-1,0,-1):
        if path_values[i]==1:
            count=count+1
        else:
            break
    return count