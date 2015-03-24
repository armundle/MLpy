# Create polynomial features given a feature vector

import numpy as np


def creat_poly_features(x, p):

    (n, m) = x.shape
    xp = np.ones((n, 1))

    for i in range(1, p):
        xp = np.append(xp, np.power(x, i), axis=0)

    xp.resize(p, n)
    return xp.T
