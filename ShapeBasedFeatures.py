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


def extract_bit_quads(masks):
    bit_quads = np.array([0, 0, 0, 0, 0]) #Q1,Q2,Q3,Q4,QD
    offset = np.array([[1, 0], [1, 1], [0, 1]])
    masks = np.pad(masks, 2)
    for i in range(masks.shape[0]):
        for j in range(masks.shape[1]):
            if i + 1 < masks.shape[0] and j + 1 < masks.shape[1]:
                if (masks[i ,j] == 255 and masks[i + offset[1, 0], j + offset[1, 1]] == 255 and masks[i + offset[0, 0], j+ offset[0, 1]] == 0 and masks[i + offset[2, 0], j+ offset[2, 1]] == 0) or (masks[i ,j] == 0 and masks[i + offset[1, 0], j + offset[1, 1]] == 0 and masks[i + offset[0, 0], j+ offset[0, 1]] == 255 and masks[i + offset[2, 0], j+ offset[2, 1]] == 255):
                    bit_quads[4] +=1
                else:
                    sum_of_one = 0
                    if(masks[i ,j] == 255):
                        sum_of_one += 1
                    for k in range(3):
                        if(masks[i + offset[k, 0], j + offset[k, 1]] == 255):
                            sum_of_one +=1
                    if sum_of_one == 0:
                        pass
                    else:
                        bit_quads[sum_of_one - 1] += 1
    return bit_quads

def area_of_image_by_bit_quads_gray(masks):
    # This method to calculate area of a pixel area invented by Gray and Pratt, called Bit Quads
    bit_quads = extract_bit_quads(masks)
    # area = 1 / 4 * bit_quads[0] + 1 / 2 * bit_quads[1] + 7 / 8 * bit_quads[2] + bit_quads[3] + 3 / 4 * bit_quads[4] # Pratt's method
    area = 1 / 4 * (bit_quads[0] + 2 * bit_quads[1] + 3 * bit_quads[2] + 4 * bit_quads[3] + 2 * bit_quads[4]) # Gray's method 
    return area

def perimeter_of_image_by_bit_quads_gray(masks):
    # This method to calculate perimeter of a pixel area invented by Gray and Pratt, called Bit Quads
    bit_quads = extract_bit_quads(masks)
    # perimeter = bit_quads[1] + 1 / math.sqrt(2) * (bit_quads[0] + bit_quads[2] + 2 * bit_quads[4]) # Pratt's method
    perimeter = bit_quads[0] + bit_quads[1] + bit_quads[2] + 2 * bit_quads[4] # Gray's method 
    return perimeter

def area_of_image_by_bit_quads_pratt(masks):
    # This method to calculate area of a pixel area invented by Gray and Pratt, called Bit Quads
    bit_quads = extract_bit_quads(masks)
    area = 1 / 4 * bit_quads[0] + 1 / 2 * bit_quads[1] + 7 / 8 * bit_quads[2] + bit_quads[3] + 3 / 4 * bit_quads[4] # Pratt's method
    # area = 1 / 4 * (bit_quads[0] + 2 * bit_quads[1] + 3 * bit_quads[2] + 4 * bit_quads[3] + 2 * bit_quads[4]) # Gray's method 
    return area

def perimeter_of_image_by_bit_quads_pratt(masks):
    # This method to calculate perimeter of a pixel area invented by Gray and Pratt, called Bit Quads
    bit_quads = extract_bit_quads(masks)
    perimeter = bit_quads[1] + 1 / math.sqrt(2) * (bit_quads[0] + bit_quads[2] + 2 * bit_quads[4]) # Pratt's method
    # perimeter = bit_quads[0] + bit_quads[1] + bit_quads[2] + 2 * bit_quads[4] # Gray's method 
    return perimeter



            
           

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

    area = area_of_image_by_bit_quads_gray(image)
    perimeter = perimeter_of_image_by_bit_quads_gray(image)
    print(area)
    print(perimeter)

    experiment = np.array([[0, 255], [255, 255]], dtype=np.uint8)
    io.imshow(experiment)
    plt.show()
    bit = extract_bit_quads(experiment)
    print(bit)
    print(area_of_image_by_bit_quads_gray(experiment))
    print(perimeter_of_image_by_bit_quads_gray(experiment))

    print(area_of_image_by_bit_quads_pratt(experiment))
    print(perimeter_of_image_by_bit_quads_pratt(experiment))