from PIL import Image
import numpy as np
import skimage
from skimage import data, io, color
from matplotlib import pyplot as plt
from scipy.stats import skew, kurtosis
import cv2

def mean_of_image(image, masks=np.array([])):
    im = np.array(image)
    (w, h, d) = im.shape
    if masks.all():
        im.shape = (w*h, d)
        return tuple(np.average(im, axis=0))
    else:
        sum = [0, 0, 0]
        iter = 0
        for i in range(w):
            for j in range(h):
                if masks[i, j] == 1 or masks[i, j] ==255:
                    sum +=im[i,j]
                    iter +=1
        #sum = sum.astype('float32')
        mean = sum / iter
        return tuple(mean)

def variance_of_image(image, masks=np.array([])):
    im = np.array(image)
    (w, h, d) = im.shape
    if masks.all():
        im.shape = (w*h, d)
        return tuple(np.var(im, axis=0))
    else:
        sum = [0, 0, 0]
        iter = 0
        for i in range(w):
            for j in range(h):
                if masks[i, j] == 1 or masks[i, j] ==255:
                    sum += im[i, j]
                    iter +=1
        #sum = sum.astype('float32')
        mean = sum / iter
        sum = [0, 0, 0]
        for i in range(w):
            for j in range(h):
                if masks[i, j] == 1 or masks[i, j] ==255:
                    sum += (im[i,j] - mean) * (im[i,j] - mean)
        sum /= iter
        return tuple(sum)

def standardDeviation_of_image(image, masks=np.array([])):
    im = np.array(image)
    (w, h, d) = im.shape
    if masks.all():
        im.shape = (w*h, d)
        return tuple(skew(im, axis=0))
    else:
        sum = [0, 0, 0]
        iter = 0
        for i in range(w):
            for j in range(h):
                if masks[i, j] == 1 or masks[i, j] ==255:
                    sum += im[i, j]
                    iter +=1
        #sum = sum.astype('float32')
        mean = sum / iter
        sum = [0, 0, 0]
        for i in range(w):
            for j in range(h):
                if masks[i, j] == 1 or masks[i, j] ==255:
                    sum += (im[i,j] - mean) * (im[i,j] - mean)
        standardDeviation = np.sqrt(sum / iter)
        return tuple(standardDeviation)

def skewness_of_image(image, masks=np.array([])):
    im = np.array(image)
    (w, h, d) = im.shape
    if masks.all():
        im.shape = (w*h, d)
        return tuple(skew(im, axis=0))
    else:
        sum = [0, 0, 0]
        iter = 0
        for i in range(w):
            for j in range(h):
                if masks[i, j] == 1 or masks[i, j] ==255:
                    sum += im[i, j]
                    iter +=1
        #sum = sum.astype('float32')
        mean = sum / iter
        sum = [0, 0, 0]
        for i in range(w):
            for j in range(h):
                if masks[i, j] == 1 or masks[i, j] ==255:
                    sum += (im[i,j] - mean) * (im[i,j] - mean)
        standardDeviation = np.sqrt(sum / iter)
        sum = [0, 0, 0]
        for i in range(w):
            for j in range(h):
                if masks[i, j] == 1 or masks[i, j] ==255:
                    sum += (im[i,j] - mean) * (im[i,j] - mean) * (im[i,j] - mean)
        skewness = standardDeviation ** -3 * (sum / iter)
        return tuple(skewness)

def kurtosis_of_image(image, masks=np.array([])):
    im = np.array(image)
    (w, h, d) = im.shape
    if masks.all():
        im.shape = (w*h ,d)
        return tuple(kurtosis(im, axis=0))   
    else:
        sum = [0, 0, 0]
        iter = 0
        for i in range(w):
            for j in range(h):
                if masks[i, j] == 1 or masks[i, j] ==255:
                    sum += im[i, j]
                    iter +=1
        mean = sum / iter
        sum = [0, 0, 0]
        for i in range(w):
            for j in range(h):
                if masks[i, j] == 1 or masks[i, j] ==255:
                    sum += (im[i,j] - mean) * (im[i,j] - mean)
        standardDeviation = np.sqrt(sum / iter)
        sum = [0, 0, 0]
        for i in range(w):
            for j in range(h):
                if masks[i, j] == 1 or masks[i, j] ==255:
                    sum += (im[i,j] - mean) * (im[i,j] - mean) * (im[i,j] - mean) * (im[i,j] - mean)
        kurt = standardDeviation ** -4 * (sum / iter) - [3, 3, 3]
        return tuple(kurt)

def energy_of_image(image, masks=np.array([])):
    pass



if __name__=='__main__':
    '''
    rocket = data.rocket()
    grayscale = color.rgb2gray(rocket)
    io.imshow(grayscale)
    plt.show()
    for i in range(grayscale.shape[0]):
        for j in range(grayscale.shape[1]):
            if grayscale[i,j] > 0.5:
                grayscale[i,j] = 1
            else:
                grayscale[i,j] = 0
    white = np.ones(grayscale.shape)
    mean = mean_of_image(rocket, grayscale)
    mean2 = mean_of_image(rocket)
    mean3 = mean_of_image(rocket, white)
    var = variance_of_image(rocket, grayscale)
    var2 = variance_of_image(rocket)
    var3 = variance_of_image(rocket, white)
    skewness = skewness_of_image(rocket, grayscale)
    skewness2 = skewness_of_image(rocket)
    skewness3 =skewness_of_image(rocket, white)
    kurt = kurtosis_of_image(rocket, grayscale)
    kurt2 = kurtosis_of_image(rocket)
    kurt3 = kurtosis_of_image(rocket, white)
    print(mean, mean2, mean3)
    print(var, var2, var3)
    print(skewness, skewness2, skewness3)
    print(kurt, kurt2, kurt3)
    io.imshow(rocket)
    plt.show()
    io.imshow(grayscale)
    plt.show()
    print(grayscale.shape)
    io.imshow(white)
    plt.show()

    Brain = Image.open(r'sample/TCGA_CS_4941_19960909_18.tif')
    Brain_mask = Image.open(r'sample/TCGA_CS_4941_19960909_18_mask.tif')
    #Brain_mask = Brain_mask.convert('1')
    print(Brain_mask.mode)
    Brain_mask = np.array(Brain_mask)
    Brain = np.array(Brain)
    print(Brain_mask.shape)
    io.imshow(Brain_mask)
    plt.show()
    print(Brain.shape)
    io.imshow(Brain)
    plt.show()
    #print(np.nonzero(Brain_mask))
    Brain_mean = mean_of_image(Brain, Brain_mask)
    Brain_var = variance_of_image(Brain, Brain_mask)
    Brain_skew = skewness_of_image(Brain, Brain_mask)
    print(Brain_mean)
    print(Brain_var)
    print(Brain_skew)
    Brain = cv2.cvtColor(Brain, cv2.COLOR_RGB2GRAY)
    io.imshow(Brain)
    plt.show()
    print(Brain.shape)
    '''
    Ivy = Image.open(r'sample/Ivy.jpeg')
    Ivy = np.array(Ivy)
    gray_Ivy = color.rgb2gray(Ivy)
    gray_Ivy2 = cv2.cvtColor(Ivy, cv2.COLOR_RGB2GRAY)
    io.imshow(Ivy)
    plt.show()
    io.imshow(gray_Ivy)
    plt.show()
    io.imshow(gray_Ivy2)
    plt.show()
    print(Ivy.shape)
    print(f'mean:{mean_of_image(Ivy)}')
    print(f'variance:{variance_of_image(Ivy)}')
    print(f'standard deviation:{standardDeviation_of_image(Ivy)}')
    print(f'skewness:{skewness_of_image(Ivy)}')
    print(f'kurtosis:{kurtosis_of_image(Ivy)}')