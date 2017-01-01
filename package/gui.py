import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

import pygubu
import package.dataprocess as dp
import matplotlib

# avoid from crashing after import tkinter (on Mac)
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

line_style_dic = { 'Dashed': '--', 'Dotted': ':', 'Solid': '-', 'Dash-Dotted': '-.' }

class Application:
    def __init__(self, master):
        self.master = master
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('gui.ui')
        self.mainwindow = builder.get_object('mainWindow', master)
        builder.connect_callbacks(self)

    def draw_figure(self):
        # Get file name, line color and line style
        filename = self.builder.get_object('strDataFilePath').get()
        objSelectColor = self.builder.get_object('selectColor')
        objSelectLine = self.builder.get_object('selectLineStyle')

        line_color = objSelectColor["text"].lower()
        line_style = line_style_dic[objSelectLine["text"]]
        
        if filename == '':
            messagebox.showinfo('From callback', 'File name can not be blank.')
            return None
        try:
            # Read from data file and draw figure
            dp.get_csv_data(filename)
            self.plot_data = plt.plot(dp.data_x_axis(), dp.data_y_axis(),
                                      color=line_color, linestyle=line_style)
            plt.show()
        except:
            messagebox.showinfo('From callback', 'File can not be found.')

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

def run():
    root = tk.Tk()
    app = Application(root)

    root.mainloop()
