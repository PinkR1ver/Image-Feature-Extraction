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

def point_in_which_side(masks, i, j):
    if i == 0 and j == 0:
        return 1
    elif (i != 0 or i != masks.shape[0] - 1) and j == 0:
        return 2
    elif i == masks.shape[0] - 1 and j == 0:
        return 3
    elif i == masks.shape[0] - 1 and (j != 0 or j != masks.shape[1] - 1):
        return 4
    elif i == masks.shape[0] -1 and j == masks.shape[1] - 1:
        return 5
    elif i == 

def perimeter_of_boundary(masks):
    offset = np.array([[0, 1], [1, 1], [1, 0], [-1, 1], [-1, 0], [-1, -1], [0, -1], [-1, 1]])
    boundary = np.array(masks.shape)
    for i in masks.shape[0]:
        for j in masks.shape[1]:
            if (masks[i, j] == 1 or masks[i, j] == 255):
                if not if_point_in_corner(masks, i, j):
                    flag = 0
                    for k in range(offset.shape[0]):
                        if masks[i + offset[k, 0], j+ offset[k, 1]] != 1 or masks[i + offset[k, 0], j+ offset[k, 1]] != 255:
                            flag = 1
                            break
                else:

            
           

if __name__ == '__main__':
    pass