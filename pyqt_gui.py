from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt

# Table setup
class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])

# Window setup for table
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, data):
        super().__init__()

        self.table = QtWidgets.QTableView()

        self.model = TableModel(data)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)

        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table.resizeColumnsToContents()