"""
This script is for displaying Fujifilm image's metadata describing 
general image properties, shoot settings, and Fujifilm recipe settings.

NOTE: The script requires "ExifTool" by Phil Harvey.
ExifTool is normally run in the command line.
https://exiftool.org/
"""

from os import sys
from PyQt5 import QtWidgets, QtGui
from PIL import Image

import funcs
import params
from pyqt_gui import MainWindow

# Set path to image of interest
img_path = "samples\_DSF2004.jpg"

# Collect all image metadata using ExifTool
all_data = funcs.get_all_metadata(img_path)

# Collect specific fields of data from overall set
file_data = funcs.get_subset_data(all_data, params.file_params) # Image file properties
shooting_data = funcs.get_subset_data(all_data, params.shooting_params) # Camera capture settings
recipe_data = funcs.get_subset_data(all_data, params.recipe_params) # FujiFilm recipe settings

# Merge data dictionaries and convert to list for PyQt Windows
fujifilm_data = file_data | shooting_data | recipe_data
fujifilm_data_list = list(fujifilm_data.items())

# Display image
img = Image.open(img_path)
img.show()

# Display metadata of interest in a new window
app = QtWidgets.QApplication(sys.argv)
windows = MainWindow(fujifilm_data_list)
windows.setWindowTitle("FujiFilm Image Metadata")
windows.setWindowIcon(QtGui.QIcon("camera.png"))
windows.show()
sys.exit(app.exec_())