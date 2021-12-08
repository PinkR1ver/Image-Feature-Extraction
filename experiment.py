import numpy as np

if __name__ == '__main__':
    x = np.ones((2, 3, 3))
    y = np.ones((2, 3, 3))
    #z = np.random.randn((2, 3, 3))
    x = x + y
    x = x/3
    print(x)

    print(x.all() == None)

    print(not np.array([]).all())
