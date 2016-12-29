import numpy as np

def get_csv_data(path):
    global data
    data = np.genfromtxt(path, delimiter=',',
                         skip_header=2,
                         skip_footer=10,
                         names=['x', 'y'])


def data_x_axis():
    return data["x"]

def data_y_axis():
    return data["y"]

