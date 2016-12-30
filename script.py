#!/usr/bin/python3

import package.dataprocess as dp
import matplotlib.pyplot as plt
import package.gui as gui

gui.run()
dp.get_csv_data("/Users/songan/workspace/python/analysis/data/S11_1.csv")
plt.plot(dp.data_x_axis(), dp.data_y_axis())

dp.get_csv_data("/Users/songan/workspace/python/analysis/data/S21_1.csv")
plt.plot(dp.data_x_axis(), dp.data_y_axis(), color="red", linestyle="--")

dp.get_csv_data("/Users/songan/workspace/python/analysis/data/S22_1.csv")
plt.plot(dp.data_x_axis(), dp.data_y_axis(), color="red", linestyle="--")

# plt.show()

