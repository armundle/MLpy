# Normalize the feature set with std and mean

import numpy as np


def normalize_features(x, std=None, mean=None):

    (m, n) = x.shape

    if mean is None:
        mean = np.mean(x, axis=0)

    if std is None:
        if (n > 1):
            std = np.std(x, axis=0)
        else:
            std = np.ones(1, n)

    for i in range(1, m):
        x[i, :] = (x[i, :] - mean[i])/(std[i])

    return (x, std, mean)
