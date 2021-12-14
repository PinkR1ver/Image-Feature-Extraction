import numpy as np

if __name__ == '__main__':
    x = np.ones((2, 3, 3))
    y = np.ones((2, 3, 3))
    z = np.random.randn((2, 3, 3))
    print(z)

    

    (w, h, d) = z.shape()
    z.shape = (w*h, d)
    print(x)
