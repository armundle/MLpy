# Gradient Descent implementation

import numpy as np


def calculate_error(x, y, theta):

    (n, m) = x.shape
    h_theta = np.dot(theta.T, x)
    return (np.sum(np.square(h_theta - y)))/(2*m)


def costfunction(x, y, theta):

    h_theta = np.dot(theta.T, x)
    m = h_theta.size
    return (np.sum(np.square(h_theta - y)))/(2*m)


def costfunction_pd(x, y, theta):

    h_theta = np.dot(theta.T, x)
    pd_cf = np.multiply((h_theta - y), x)
    return np.sum(pd_cf, axis=1)


def gradientdescent(x, y, theta, alpha, iterations, lamda=0.0):

    (n, m) = x.shape

    # Create a local copy of theta
    theta_cache = theta.copy()

    for i in range(iterations):
        pd_cf = costfunction_pd(x, y, theta)

        theta_cache[0] = theta_cache[0] - (alpha/m)*pd_cf[0]

        for j in range(1, n):
            theta_cache[j] = theta_cache[j] - (alpha/m)*pd_cf[j] + (lamda/m)*theta_cache[j]

        theta = theta_cache.copy()

    return theta
