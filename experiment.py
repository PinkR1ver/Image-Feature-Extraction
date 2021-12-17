import numpy as np

if __name__ == '__main__':
    bins = np.linspace(0, 256, 8)
    for i in range(bins.shape[0]):
        print(bins[i])