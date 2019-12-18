import pandas as pd
import numpy as np


def make_sequence(data_vector, n_input, n_output):
    dataset_x = np.zeros(((data_vector.shape[0]-n_input) - (n_output - 1), n_input))
    dataset_y = np.zeros(((data_vector.shape[0]-n_input) - (n_output - 1), n_output))

    for i in range((data_vector.shape[0]-n_input) - (n_output - 1)):
        x_array = data_vector[i:i+n_input]
        y_array = data_vector[i+n_input:i+n_input+n_output]
        dataset_x[i] = x_array
        dataset_y[i] = y_array

    return dataset_x, dataset_y
