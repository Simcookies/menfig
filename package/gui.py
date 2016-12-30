import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

import pygubu
import package.dataprocess as dp
import matplotlib.pyplot as plt

class Application:
    def __init__(self, master):
        self.master = master
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('gui.ui')
        self.mainwindow = builder.get_object('mainWindow', master)
        builder.connect_callbacks(self)

    def draw_figure(self):
        filename = self.builder.get_object('strDataFilePath').get()
        if filename == '':
            messagebox.showinfo('From callback', 'File name can not be blank.')
            return None
        try:
            dp.get_csv_data(filename)
            self.plot_data = plt.plot(dp.data_x_axis(), dp.data_y_axis())
            plt.show()
        except:
            messagebox.showinfo('From callback', 'File can not be found.')

    def quit_app(self):
        plt.close('all')
        self.master.quit()

    def explore_file(self):
        # Open file from File Explorer and keep file path
        filename = filedialog.askopenfilename(filetypes=[("CSV Data files","*.csv")])

        # Replace value of Entey
        objDataFile = self.builder.get_object('strDataFilePath')
        objDataFile.delete(0, 'end')
        objDataFile.insert(0, filename)

def run():
    root = tk.Tk()
    app = Application(root)

    root.mainloop()
