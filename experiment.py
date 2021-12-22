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