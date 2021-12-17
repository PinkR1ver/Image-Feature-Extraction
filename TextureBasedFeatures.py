import os
import numpy as np
import cv2
from numpy.lib.type_check import imag
from skimage import io
from matplotlib import pyplot as plt
from skimage.feature import greycomatrix, greycoprops


def ImageCompress(image, image_depth=256, levels=8):
    bins = np.linspace(0, image_depth, levels)
    image_compress = np.digitize(image, bins, True)
    image_compress = np.uint8(image_compress)
    return image_compress


def gray_level_co_occurence_matrix(image, image_depth=256, levels=8, offset=[0, 1]):
    image = ImageCompress(image, image_depth, levels)
    GLCM = np.zeros((levels, levels))  # gray levels co-occurence matrix
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if i + offset[0] < image.shape[0] and i + offset[0] >= 0 and j + offset[1] < image.shape[1] and j + offset[1] >= 0:
                x = image[i, j]
                y = image[i + offset[0], j + offset[1]]
                GLCM[x, y] += 1
    return np.uint(GLCM)


if __name__ == '__main__':
    levels = 8
    image = cv2.imread('sample/Ivy.jpeg', 0)
    print()
    image_compress = ImageCompress(image, levels=levels)
    stack_image = np.hstack((image, image_compress))
    io.imshow(stack_image)
    plt.show()
    glcm = greycomatrix(image_compress, [1], [0], levels)
    print(glcm.shape)
    print(np.squeeze(np.uint(glcm)))
    for prop in {'contrast', 'dissimilarity', 'homogeneity', 'energy', 'correlation', 'ASM'}:

        temp = greycoprops(glcm, prop)

        print(prop, temp)
        print("==============================\n")

    GLCM = gray_level_co_occurence_matrix(image, levels=levels)
    print(GLCM)
    print(image.size - np.count_nonzero(image))
    print(image_compress.size - np.count_nonzero(image_compress))
    

    test = np.array([[0, 0, 1, 1],
                       [0, 0, 1, 1],
                       [0, 2, 2, 2],
                       [2, 2, 3, 3]], dtype=np.uint8)
    test_glcm = greycomatrix(test, [1], [0], levels = 4)
    test_GLCM = gray_level_co_occurence_matrix(test, levels=4, image_depth=4)
    print(np.squeeze(test_glcm))
    print(test_GLCM)
    print(ImageCompress(test, image_depth=4, levels=4))
    
