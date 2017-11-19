from matplotlib.figure import Figure
import matplotlib as mpl
import matplotlib.pyplot as plt
from package import dataprocess as dp

del mpl.font_manager.weight_dict['roman']
mpl.font_manager._rebuild()
mpl.use("TkAgg")

class Drawer:
    def __init__(self):
        # Configuration for font and line style
        plt.rcParams["font.size"] = 16
        plt.rcParams["font.family"] = "Times New Roman"
        plt.rcParams["lines.linewidth"] = 1

        self.figure = Figure()
        self.axes   = self.figure.add_subplot(111)

    def draw_fig(self, fig_data, fig_config):
        # fig_config: dictionary
        #   'line_color': string
        #   'line_style': string
        dp.get_csv_data(fig_data)
        self.axes.plot(dp.data_x_axis(), dp.data_y_axis(),
                       color=fig_config['line_color'], linestyle=fig_config['line_style'])
        #plt.xlim(0,4)
        #plt.ylim(-70,5)
    
    def set_axes(self, axes_config=None):
        self.axes.set_xlabel("Frequency(GHz)")
        self.axes.set_ylabel(r'|S$_{11}$|,|S$_{21}$|(dB)')
        self.axes.tick_params(direction='in', length=8, top=True, right=True)
    #def destroy_fig(self):