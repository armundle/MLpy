# Load matlab mat file

import scipy.io


def load_data(filename):
    return scipy.io.loadmat(filename)
