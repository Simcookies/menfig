import numpy as np

class CSVData:
    def load_data(self, path):
        data = np.genfromtxt(path, delimiter=',',
                             skip_header=2,
                             skip_footer=10,
                             names=['x', 'y'])
        self.data_x_axis = data['x']
        self.data_y_axis = data['y']