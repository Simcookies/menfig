import tkinter as tk
from tkinter import filedialog
import pygubu

class Application:
    def __init__(self, master):
        self.master = master
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('gui.ui')
        self.mainwindow = builder.get_object('mainWindow', master)
        builder.connect_callbacks(self)

    def explore_file_s11(self):
        self.explore_file(self, 'strDataFilePath_S11')

    def explore_file_s21(self):
        self.explore_file(self, 'strDataFilePath_S21')

    @staticmethod
    def explore_file(master, objId):
        # Open file from File Explorer and keep file path
        filename = askopenfilename(filetypes=[("CSV Data files","*.csv")])

        # Replace value of Entey
        objDataFile = master.builder.get_object(objId)
        objDataFile.delete(0, 'end')
        objDataFile.insert(0, filename)

def run():
    root = tk.Tk()
    app = Application(root)

    root.mainloop()
