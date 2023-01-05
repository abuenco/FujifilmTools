"""
This script is for displaying Fujifilm image's metadata describing 
general image properties, shoot settings, and Fujifilm recipe settings.

NOTE: The script requires "ExifTool" by Phil Harvey.
https://exiftool.org/
"""

import os
import sys
import subprocess # module to run processes in the command line

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt

# Display metadata of one image
img = "C:\Documents\ImageTools\samples\_DSF2004.jpg"

#TODO: Write functions for all of these
# File properties
file_data = ["File Name", 
             "File Size", 
             "File Type",
             "File Type Extension",
             "File Creation Date/Time",
             "Image Width",
             "Image Height"]

# Camera's shooting information
shooting_data = ["Make",
                 "Camera Model Name",
                 "Softrware",
                 "Exposure Program",
                 "ISO",
                 "F Number",
                 "Exposure Time",
                 "Focal Length",
                 "Exposure Compensation",
                 "Fuji Flash Mode",
                 "Flash Exposure Comp"]

# Fujifilm settings in camera
recipe_data= ["Film Mode",
              "Grain Effect Roughness",
              "Grain Effect Size",
              "Color Chrome Effect",
              "Color Chrome FX Blue",
              "Light Source",
              "White Balance Fine Tune",
              "Highlight Tone",
              "Shadow Tone",
              "Saturation",
              "Noise Reduction",
              "Clarity"]

# Run ExifTool like you would in the command prompt
output = subprocess.check_output(["exiftool", "samples\_DSF2004.jpg"])

# Parse output
results = output.decode().split("\r\n")
data = {}
for i, line in enumerate(results):
    if i < len(results)-1:
        s = line.split(":")
        s_key = s[0].rstrip()
        s_val = s[1]
        data[s_key] = s_val

#TODO: Display data in a table
print("FILE DATA")
for key, val in data.items():
    if key in file_data:
        print(f"{key}: {val}")

print('\n')

print("SHOOTING DATA")
for key, val in data.items():
    if key in shooting_data:
        print(f"{key}: {val}")

print('\n')

print("FUJIFILM RECIPE DATA")
for key, val in data.items():
    if key in recipe_data:
        print(f"{key}: {val}")


data_list = list(data.items())

# PyQt5 table setup

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableView()

        self.model = TableModel(data_list)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)

'''
cols = 2
rows = len(file_data) + len(shooting_data) + len(recipe_data)
tableWidget = QtWidgets.QTableView()
'''

app = QtWidgets.QApplication(sys.argv)
windows = MainWindow()

windows.setWindowTitle("FujiFilm Image Metadata")
windows.setWindowIcon(QtGui.QIcon("camera.png"))
windows.show()
sys.exit(app.exec_())

#TODO: Write a function to match the recipe data to a recipe in my camera.