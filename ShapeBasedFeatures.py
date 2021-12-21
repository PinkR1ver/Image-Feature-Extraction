import os
import numpy as np
import cv2
from skimage import io
from matplotlib import pyplot as plt
import math

def if_point_in_corner(masks, i, j):
    if i ==0 or i == masks.shape[0] - 1 or j == 0 or j == masks.shape[1] - 1:
        return True
    else:
        return False

'''
def point_in_which_side(masks, i, j):
    if i == 0 and j == 0:
        return 1
    elif i != 0 and i != masks.shape[0] - 1 and j == 0:
        return 2
    elif i == masks.shape[0] - 1 and j == 0:
        return 3
    elif i == masks.shape[0] - 1 and j != 0 and j != masks.shape[1] - 1:
        return 4
    elif i == masks.shape[0] -1 and j == masks.shape[1] - 1:
        return 5
    elif i != 0 and i!= masks.shape[0] - 1 and j == masks.shape[1] - 1:
        return 6
    elif i == 0 and j == masks.shape[1] - 1:
        return 7
    elif i == 0 and j != masks.shape[1] - 1 and j!= 0:
        return 8
'''

def extract_boundary(masks):
    offset = np.array([[0, 1], [1, 1], [1, 0], [-1, 1], [-1, 0], [-1, -1], [0, -1], [-1, 1]])
    boundary = np.zeros(masks.shape, dtype=np.uint8)
    for i in range(masks.shape[0]):
        for j in range(masks.shape[1]):
            if masks[i, j] == 255:
                if not if_point_in_corner(masks, i, j):
                    flag = 0
                    for k in range(offset.shape[0]):
                        if masks[i + offset[k, 0], j+ offset[k, 1]] != 255:
                            flag = 1
                            break
                    if flag:
                        boundary[i, j] = 255       
                else:
                    boundary[i, j] = 255
                    '''
                    if point_in_which_side(masks, i, j) == 1:
                        flag = 0
                        direction = [0, 1, 2]
                        for k in direction:
                            if masks[i + offset[k, 0], j + offset [k, 1]] != 255:
                                flag = 1
                                break
                        if flag:
                            boundary[i, j] = 255
                    elif  point_in_which_side(masks, i, j) == 2:
                        flag = 0
                        direction = [0, 1, 2, 3, 4]
                        for k in direction:
                            if masks[i + offset[k, 0], j + offset [k, 1]] != 255:
                                flag = 1
                                break
                        if flag:
                            boundary[i, j] = 255
                    elif  point_in_which_side(masks, i, j) == 3:
                        flag = 0
                        direction = [2, 3, 4]
                        for k in direction:
                            if masks[i + offset[k, 0], j + offset [k, 1]] != 255:
                                flag = 1
                                break
                        if flag:
                            boundary[i, j] = 255
                    elif  point_in_which_side(masks, i, j) == 4:
                        flag = 0
                        direction = [2, 3, 4, 5, 6]
                        for k in direction:
                            if masks[i + offset[k, 0], j + offset [k, 1]] != 255:
                                flag = 1
                                break
                        if flag:
                            boundary[i, j] = 255
                    elif  point_in_which_side(masks, i, j) == 5:
                        flag = 0
                        direction = [4, 5, 6]
                        for k in direction:
                            if masks[i + offset[k, 0], j + offset [k, 1]] != 255:
                                flag = 1
                                break
                        if flag:
                            boundary[i, j] = 255
                    elif  point_in_which_side(masks, i, j) == 6:
                        flag = 0
                        direction = [4, 5, 6, 7, 0]
                        for k in direction:
                            if masks[i + offset[k, 0], j + offset [k, 1]] != 255:
                                flag = 1
                                break
                        if flag:
                            boundary[i, j] = 255
                    elif  point_in_which_side(masks, i, j) == 7:
                        flag = 0
                        direction = [6, 7, 0]
                        for k in direction:
                            if masks[i + offset[k, 0], j + offset [k, 1]] != 255:
                                flag = 1
                                break
                        if flag:
                            boundary[i, j] = 255
                    elif  point_in_which_side(masks, i, j) == 8:
                        flag = 0
                        direction = [6, 7, 0, 1, 2]
                        for k in direction:
                            if masks[i + offset[k, 0], j + offset [k, 1]] != 255:
                                flag = 1
                                break
                        if flag:
                            boundary[i, j] = 255
                    '''        
    return boundary

def perimeter_of_boundary(masks):
    boundary = extract_boundary(masks)




def area_of_image(masks):
    area = 0
    for i in range(masks.shape[0]):
        for j in range(masks.shape[1]):
            if masks[i, j] == 255:
                area += 1
    return area

            
           

if __name__ == '__main__':
    image = cv2.imread(r'sample/TCGA_CS_4941_19960909_18_mask.tif', cv2.IMREAD_GRAYSCALE)
    image = np.array(image)
    io.imshow(image)
    plt.show()

    white = np.zeros(image.shape, dtype=np.uint8)
    for i in range(4, white.shape[0] - 4):
        for j in range(4, white.shape[1] - 4):
            white[i, j] = 255

    boundary = extract_boundary(image)
    io.imshow(boundary)
    plt.show()

    io.imshow(white)
    plt.show()

    white_boundary = extract_boundary(white)

    io.imshow(white_boundary)
    plt.show()