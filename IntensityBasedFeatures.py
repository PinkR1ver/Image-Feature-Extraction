from PIL import Image
import numpy as np
import skimage
from skimage import data, io, color
from matplotlib import pyplot as plt
from scipy.stats import skew

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



if __name__=='__main__':
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
    mean = mean_of_image(rocket, grayscale)
    var = variance_of_image(rocket, grayscale)
    skewness = skewness_of_image(rocket, grayscale)
    print(mean)
    print(var)
    print(skewness)
    io.imshow(rocket)
    plt.show()
    io.imshow(grayscale)
    plt.show()
    print(grayscale.shape)
    white = np.ones(grayscale.shape)
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