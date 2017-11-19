import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from package.dataprocess import CSVData

del mpl.font_manager.weight_dict['roman']
mpl.font_manager._rebuild()
mpl.use("TkAgg")

class Drawer:
    def __init__(self):
        # Configuration for font and line style
        plt.rcParams["font.size"] = 16
        plt.rcParams["font.family"] = "Times New Roman"
        plt.rcParams["lines.linewidth"] = 1

        self.figure   = Figure()
        self.axes     = self.figure.add_subplot(111)
        self.csv_data = CSVData()

    def draw_fig(self, fig_data, fig_config):
        # fig_config: dictionary
        #   'line_color': string
        #   'line_style': string
        self.csv_data.load_data(fig_data)
        self.axes.plot(self.csv_data.data_x_axis, self.csv_data.data_y_axis,
                       color=fig_config['line_color'], linestyle=fig_config['line_style'])
        # plt.xlim(0,4)
        # plt.ylim(-70,5)
    
    def set_axes(self, axes_config):
        self.axes.set_xlabel(axes_config['x_label'])
        self.axes.set_ylabel(axes_config['y_label'])
        self.axes.tick_params(direction='in', length=8, top=True, right=True)

    def clear_fig(self):
        self.axes.clear()