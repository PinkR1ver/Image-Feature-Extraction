import os
import numpy as np
import cv2
from skimage import io
from matplotlib import pyplot as plt
from skimage.feature import greycomatrix, greycoprops

def ImageCompress(image, levels):
    bins = np.linspace(0, 256, levels)
    image_compress = np.digitize(image, bins)
    image_compress = np.uint8(image_compress)
    return image_compress

def gray_level_co_occurence_matrix(image, levels):
    #GLCM: gray level co-occurence matrix
    glcm = greycomatrix(image, [1], [0, np.pi/4, np.pi/2, np.pi*3/4], levels)
    return glcm



if __name__ == '__main__':
    levels = 8
    image = cv2.imread('sample/Ivy.jpeg', 0)
    image_compress = ImageCompress(image, levels)
    stack_image = np.hstack((image, image_compress))
    io.imshow(stack_image)
    plt.show()
    glcm = gray_level_co_occurence_matrix(image_compress, levels)
    print(glcm.shape)
    for prop in {'contrast', 'dissimilarity','homogeneity', 'energy', 'correlation', 'ASM'}:
            
        temp = greycoprops(glcm, prop)

        print(prop, temp)
        print( "==============================\n")


    
