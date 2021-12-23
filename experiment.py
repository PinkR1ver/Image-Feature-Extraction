from matplotlib.pyplot import xcorr
import numpy as np

if __name__ == '__main__':
    bins = np.linspace(0, 256, 8)
    for i in range(bins.shape[0]):
        print(bins[i])
    
    offset = np.array([[0, 1], [1, 1], [1, 0], [-1, 1], [-1, 0], [-1, -1], [0, -1], [-1, 1]])
    print(offset.shape)

    direction = [1, 2, 4]
    for k in direction:
        print(k)

    a = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
    a = np.pad(a, 2)
    print(a)

    x = np.array([], dtype=np.uint8)
    x = np.append(x, 2 * 2)
    print(x)

    x = np.array([1, 2, 3, 4, 4, 4, 5, 6, 7, 3, 3], dtype=np.uint8)
    y = np.array([1, 2, 3, 3], dtype=np.uint8)
    z = np.array([3, 3, 4, 5])
    exp_list = []
    exp_list.append(x)
    exp_list.append(y)
    exp_list.append(z)
    print(exp_list[0])