# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Inspect.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import cx_Oracle

class Ins(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 691)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
"    background-image:  url(../images.qrc/vecteezy_hexagon-abstract-modern-background-with-overlapping-triangle_5909540.jpg);\n"
"background-repeat: no-repeat;\n"
"};")
        self.bgwidget.setObjectName("bgwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bgwidget)
        self.verticalLayout_2.setContentsMargins(50, 50, 50, 50)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.bgwidget)
        self.frame.setAcceptDrops(True)
        self.frame.setStyleSheet("background-color:white;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.AdminLoginBtn = QtWidgets.QPushButton(self.frame)
        self.AdminLoginBtn.setGeometry(QtCore.QRect(350, 490, 411, 41))
        self.AdminLoginBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AdminLoginBtn.setStyleSheet("QPushButton{\n"
"background-color: rgb(72,61,139);\n"
"color:white;\n"
"border-radius:20px;\n"
"font-size:20px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: white;\n"
"color:rgb(72,61,139);\n"
"border:1px solid rgb(72,61,139);\n"
"transform:scale(1.2);\n"
"}")
        self.AdminLoginBtn.setFlat(False)
        self.AdminLoginBtn.clicked.connect(lambda :self.inset())
        self.AdminLoginBtn.setObjectName("AdminLoginBtn")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(40, 100, 1001, 361))
        self.tableWidget.setMouseTracking(False)
        self.tableWidget.setStyleSheet("background-color: white;\n"
"color: rgb(0, 0, 127);")
        self.tableWidget.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(12)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 255, 255))
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setItalic(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        item.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget.setItem(0, 3, item)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(420, 10, 281, 51))
        self.label.setStyleSheet("font-family:\'Montserrat\';\n"
"font-size:40px;\n"
"color: rgb(72,61,139);\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout.addWidget(self.bgwidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.AdminLoginBtn.setText(_translate("Dialog", "Load Data"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Customer 1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "Customer 2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "Customer 3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "Customer 4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "Customer 5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "Customer 6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "Customer 7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Dialog", "Customer 8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Dialog", "Customer 9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Dialog", "Customer 10"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("Dialog", "Customer 11"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("Dialog", "Customer 12"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Reference No"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "First Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Middle Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Last Name"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Street"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Division"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "City"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "Meter No"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "Password"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Dialog", "Customer Data"))

    def inset(self):
        try:
            with cx_Oracle.connect('system/Oracle123') as co:
                cur = co.cursor()
                quey = """SELECT * FROM show_123"""
                result = cur.execute(quey)
                self.tableWidget.setRowCount(0)
                for rowNo, row_data in enumerate(result):
                    self.tableWidget.insertRow(rowNo)
                    for col_no, col_data in enumerate(row_data):
                        self.tableWidget.setItem(rowNo, col_no, QtWidgets.QTableWidgetItem(str(col_data)))
        except Exception as e:
            print("Error: ", str(e))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ins()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
