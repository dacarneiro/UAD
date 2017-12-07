import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class MyFrame(QtWidgets.QFrame):
    def __init__(self, parent=None,initials=None):
        QtWidgets.QFrame.__init__(self, parent)
        self.table = QtWidgets.QTableWidget(5,2,self)
        self.table.move(30,30)
        self.table.resize(400,300)

        item1 = QtWidgets.QTableWidgetItem('Plugin')
        item1.setBackground(QtGui.QColor(255, 0, 0))
        self.table.setHorizontalHeaderItem(0,item1)

        item2 = QtWidgets.QTableWidgetItem('Status')
        item2.setBackground(QtGui.QColor(0, 255, 0))
        self.table.setHorizontalHeaderItem(1,item2)
        combo_box_options = ["Show", "Hide"]
        index = 0
        item1 = QtWidgets.QTableWidgetItem('UAD1')
        item2 = QtWidgets.QTableWidgetItem('UAD2')
        self.table.setItem(index, 0, item1)
        self.table.setItem(1, 0, item2)
        combo = QtWidgets.QComboBox()
        self.table.setRowCount(4)
        data1 = ['row1','row2','row3','row4']
        data2 = ['1','2.0','3.00000001','3.9999999']
        for index in range(4):
            item1 = QtWidgets.QTableWidgetItem('asdf')
            self.table.setItem(index,0,item1)
            item2 = QtWidgets.QTableWidgetItem('asssdf')
            self.table.setItem(index,1,item2)
            combo = QtWidgets.QComboBox()
            for t in combo_box_options:
                combo.addItem(t)
            self.table.setCellWidget(1,1,combo)













#        for index in range(4):
#            for t in combo_box_options:
#                combo.addItem(t)
#            self.table.setCellWidget(index, 1, combo)
#
#        for index in range(4):
#            item1 = QtWidgets.QTableWidgetItem('asdf')
#            self.table.setItem(index, 0, item1)
#            item2 = QtGui.QTableWidgetItem(data2[index])
#            self.table.setItem(index, 1, item2)
#            combo = QtGui.QComboBox()
#            for t in combo_box_options:
#                combo.addItem(t)
#            self.table.setCellWidget(index, 2, combo)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion')) # won't work on windows style.
    Frame = MyFrame(None)
    Frame.resize(500,400)
    Frame.show()
    app.exec_()