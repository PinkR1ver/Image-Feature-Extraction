from PIL import Image
import numpy as np
import skimage
from skimage import data, io, color
from matplotlib import pyplot as plt

def mean_of_image(image, masks=np.array([])):
    im = np.array(image)
    (w, h, d) = im.shape
    if masks.all():
        im.shape = (w*h, d)
        return tuple(np.average(im, axis=0))
    else:
        sum=[0 ,0 ,0]
        iter = 0
        for i in range(w):
            for j in range(h):
                if masks[i, j] == 1:
                    sum +=im[i,j]
                    iter +=1
        sum = sum.astype('float32')
        sum /= iter
        return tuple(sum)

def variance_of_image(image, masks=np.array([]), mean=None):
    im = np.array(image)
    (w, h, d) = im.shape
    if masks.all():
        im.shape = (w*h, d)
        return tuple(np.var(im, axis=0))


if __name__=='__main__':
    rocket = data.rocket()
    grayscale = color.rgb2gray(rocket)
    print(grayscale.shape)
    for i in range(grayscale.shape[0]):
        for j in range(grayscale.shape[1]):
            if grayscale[i,j] > 0.5:
                grayscale[i,j] = 1
            else:
                grayscale[i,j] = 0
    mean = mean_of_image(rocket, grayscale)
    var = variance_of_image(rocket)
    print(mean)
    print(var)
    io.imshow(rocket)
    plt.show()
    io.imshow(grayscale)
    plt.show()
    white = np.ones(grayscale.shape)
    io.imshow(white)
    plt.show()

