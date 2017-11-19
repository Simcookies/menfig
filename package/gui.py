from tkinter import filedialog
from tkinter import messagebox

import pygubu
from package.drawfig import Drawer
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

line_style_dic = { 'Dashed': '--', 'Dotted': ':', 'Solid': '-', 'Dash-Dotted': '-.' }

class Application:
    def __init__(self, master):
        # Load UI and set callbacks function
        self.master = master
        self.builder = pygubu.Builder()
        self.builder.add_from_file('gui.ui')
        self.mainwindow = self.builder.get_object('mainWindow', master=master)
        self.builder.connect_callbacks(self)

        # Bundle drawer into canvas of Tk
        self.drawer = Drawer()
        self.canvas = FigureCanvasTkAgg(self.drawer.figure, 
                                        master=self.builder.get_object('fig_area'))
        self.canvas.get_tk_widget().pack()
        # toolbar = NavigationToolbar2TkAgg(self.canvas, self.builder.get_object('fig_area'))
        # toolbar.update()
        # self.canvas._tkcanvas.pack()

    def set_axes(self):
        self.drawer.set_axes()
        self.canvas.show()
    
    def draw_figure(self):
        # Get file name, line color and line style
        objFilePath    = self.builder.get_object('strDataFilePath')
        objSelectColor = self.builder.get_object('selectColor')
        objSelectLine  = self.builder.get_object('selectLineStyle')

        filename = objFilePath.get()
        fig_config = {}
        fig_config['line_color'] = objSelectColor["text"].lower()
        fig_config['line_style'] = line_style_dic[objSelectLine["text"]]

        if filename == '':
            messagebox.showinfo('From callback', 'File name can not be blank.')
            return None
        
        self.drawer.draw_fig(filename, fig_config)
        self.canvas.show()
        #   except:
        #    messagebox.showinfo('From callback', 'File can not be found.')

    def clear_fig(self):
        self.drawer.axes.clear()
        self.canvas.show()
        print("TODO: still in developing")

    def quit_app(self):
        self.master.quit()

    def explore_file(self):
        # Open file from File Explorer and keep file path
        filename = filedialog.askopenfilename(filetypes=[("CSV Data files","*.csv")])

        # Replace value of Entey
        objDataFile = self.builder.get_object('strDataFilePath')
        objDataFile.delete(0, 'end')
        objDataFile.insert(0, filename)

    def on_colormenu_clicked(self, itemId):
        objSelectColor = self.builder.get_object('selectColor')
        objSelectColor["text"] = itemId[5:]

    def on_linemenu_clicked(self, itemId):
        objSelectLine = self.builder.get_object('selectLineStyle')
        objSelectLine["text"] = itemId[4:]