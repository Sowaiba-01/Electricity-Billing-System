from PyQt5 import QtWidgets

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt, QDate, QTime)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
import cx_Oracle
from random import randint, randrange
from PyQt5 import QtCore, QtGui, QtWidgets
class Del(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1086, 671)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
"    background-image: url(../images.qrc/vecteezy_hexagon-abstract-modern-background-with-overlapping-triangle_5909540.jpg);\n"
"background-repeat:no-repeat;\n"
"};\n"
"")
        self.bgwidget.setObjectName("bgwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bgwidget)
        self.verticalLayout_2.setContentsMargins(40, 40, 40, 40)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.bgwidget)
        self.groupBox.setStyleSheet("QGroupBox#groupBox\n"
"{\n"
"background-color:white;\n"
"border-radius:10px;\n"
"};")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(510, 120, 441, 391))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../garbage/FeedbackImage.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.Fdbck_Name = QtWidgets.QLineEdit(self.groupBox)
        self.Fdbck_Name.setGeometry(QtCore.QRect(160, 240, 291, 31))
        self.Fdbck_Name.setObjectName("Fdbck_Name")
        self.F_Department = QtWidgets.QLineEdit(self.groupBox)
        self.F_Department.setGeometry(QtCore.QRect(160, 200, 291, 31))
        self.F_Department.setObjectName("F_Department")
        self.F_Department_2 = QtWidgets.QLineEdit(self.groupBox)
        self.F_Department_2.setGeometry(QtCore.QRect(160, 200, 291, 31))
        self.F_Department_2.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;\n"
"")
        self.F_Department_2.setObjectName("F_Department_2")
        self.SubmitFdbckBtn_2 = QtWidgets.QPushButton(self.groupBox)
        self.SubmitFdbckBtn_2.setGeometry(QtCore.QRect(170, 330, 171, 41))
        self.SubmitFdbckBtn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SubmitFdbckBtn_2.setStyleSheet("QPushButton{\n"
"background-color:rgb(52, 45, 113);\n"
"color:white;\n"
"border-radius:20px;\n"
"font-size:20px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"\n"
"background-color: white;\n"
"color:rgb(52, 45, 113);\n"
"border:1px solid rgb(52, 45, 113);\n"
"transform:scale(1.2);\n"
"}")
        self.SubmitFdbckBtn_2.clicked.connect(lambda : self.deleting())
        self.SubmitFdbckBtn_2.setObjectName("SubmitFdbckBtn_2")
        self.label_35 = QtWidgets.QLabel(self.groupBox)
        self.label_35.setGeometry(QtCore.QRect(50, 250, 121, 16))
        self.label_35.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.groupBox)
        self.label_36.setGeometry(QtCore.QRect(50, 210, 101, 20))
        self.label_36.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_36.setObjectName("label_36")
        self.Fdbck_Name_2 = QtWidgets.QLineEdit(self.groupBox)
        self.Fdbck_Name_2.setGeometry(QtCore.QRect(160, 240, 291, 31))
        self.Fdbck_Name_2.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;\n"
"")
        self.Fdbck_Name_2.setObjectName("Fdbck_Name_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(470, 30, 521, 481))
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label_2.setStyleSheet("background-image: url(:/newPrefix/Desktop/images.qrc/istockphoto-1296846625-170667a.jpg);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../images.qrc/istockphoto-1296846625-170667a.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(50, 50, 381, 51))
        self.label_3.setStyleSheet("font: 80 15pt \"MS Shell Dlg 2\";color:rgb(52, 45, 113);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(840, 20, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_4.setStyleSheet("color:rgb(52, 45, 113);")
        self.label_4.setObjectName("label_4")
        self.F_Department_3 = QtWidgets.QLineEdit(self.groupBox)
        self.F_Department_3.setGeometry(QtCore.QRect(160, 160, 291, 31))
        self.F_Department_3.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;\n"
"")
        self.F_Department_3.setObjectName("F_Department_3")
        self.label_37 = QtWidgets.QLabel(self.groupBox)
        self.label_37.setGeometry(QtCore.QRect(50, 170, 101, 20))
        self.label_37.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_37.setObjectName("label_37")
        self.verticalLayout_2.addWidget(self.groupBox)
        self.verticalLayout.addWidget(self.bgwidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Fdbck_Name.setPlaceholderText(_translate("Dialog", "Name"))
        self.F_Department.setPlaceholderText(_translate("Dialog", "Department"))
        self.F_Department_2.setPlaceholderText(_translate("Dialog", "Enter Bill Id"))
        self.SubmitFdbckBtn_2.setText(_translate("Dialog", "Delete Data"))
        self.label_35.setText(_translate("Dialog", "Meter No"))
        self.label_36.setText(_translate("Dialog", "Bill ID"))
        self.Fdbck_Name_2.setPlaceholderText(_translate("Dialog", "Enter user Meter no"))
        self.label_3.setText(_translate("Dialog", "Deleting User Data "))
        self.label_4.setText(_translate("Dialog", "ⓔ IESCO"))
        self.F_Department_3.setPlaceholderText(_translate("Dialog", "Enter User Reference Number"))
        self.label_37.setText(_translate("Dialog", "Reference Number"))
    def deleting(self):
        try:
            msg = QMessageBox()
            if self.F_Department_3.text() == "" or self.F_Department_2.text() == ""or self.Fdbck_Name_2.text() == "":
                msg.setText("Fill All Required Fields")
                msg.setWindowTitle("Error")
                w = msg.exec_()
            else:
                ref_no = int(self.F_Department_3.text())
                bill_id = int(self.F_Department_2.text())
                meter = int(self.Fdbck_Name_2.text())
                with cx_Oracle.connect('system/Oracle123') as co:
                    cur = co.cursor()
                    cur.execute("begin delete_Customer_bill(:1); end;", [bill_id])
                    cur.execute("begin delete_Customer(:1); end;", [ref_no])
                    co.commit()
                    self.messageBox = QMessageBox()
                    self.messageBox.setText("Record Deleted SuccessFully")
                    self.messageBox.exec_()
        except Exception as e:
            print("Error: ", str(e))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Del()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
