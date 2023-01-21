from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint, QRect, QSize, QUrl, Qt, QDate, QTime)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import cx_Oracle
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
import cx_Oracle

class FIn(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1086, 594)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
"    background-image:  url(../images.qrc/vecteezy_hexagon-abstract-modern-background-with-overlapping-triangle_5909540.jpg);\n"
"    \n"
"background-repeat:no-repeat;\n"
"};\n"
"")
        self.bgwidget.setObjectName("bgwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bgwidget)
        self.verticalLayout_2.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.bgwidget)
        self.frame.setStyleSheet("QFrame#frame\n"
"{\n"
"    background-color:white;\n"
"border-radius: 10px;\n"
"};")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(400, 10, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(-1)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font-family:\'Montserrat\';\n"
"font-size:25px;\n"
"color:rgb(52, 45, 113);")
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.M_Name = QtWidgets.QLineEdit(self.frame)
        self.M_Name.setGeometry(QtCore.QRect(170, 170, 311, 31))
        self.M_Name.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.M_Name.setObjectName("M_Name")
        self.SysCust = QtWidgets.QRadioButton(self.frame)
        self.SysCust.setGeometry(QtCore.QRect(670, 330, 171, 31))
        self.SysCust.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.SysCust.setObjectName("SysCust")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(540, 140, 121, 16))
        self.label_9.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(540, 180, 121, 16))
        self.label_10.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_10.setObjectName("label_10")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(40, 220, 121, 16))
        self.label_8.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_8.setObjectName("label_8")
        self.RefNo = QtWidgets.QLineEdit(self.frame)
        self.RefNo.setGeometry(QtCore.QRect(170, 290, 311, 31))
        self.RefNo.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.RefNo.setText("")
        self.RefNo.setPlaceholderText("")
        self.RefNo.setObjectName("RefNo")
        self.H_No = QtWidgets.QLineEdit(self.frame)
        self.H_No.setGeometry(QtCore.QRect(670, 130, 311, 31))
        self.H_No.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.H_No.setObjectName("H_No")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(40, 340, 121, 16))
        self.label_15.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_15.setObjectName("label_15")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(40, 260, 121, 16))
        self.label_13.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_13.setObjectName("label_13")
        self.F_Name = QtWidgets.QLineEdit(self.frame)
        self.F_Name.setGeometry(QtCore.QRect(170, 130, 311, 31))
        self.F_Name.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.F_Name.setObjectName("F_Name")
        self.U_City = QtWidgets.QLineEdit(self.frame)
        self.U_City.setGeometry(QtCore.QRect(670, 250, 311, 31))
        self.U_City.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.U_City.setObjectName("U_City")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(40, 300, 121, 16))
        self.label_14.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_14.setObjectName("label_14")
        self.Street_No = QtWidgets.QLineEdit(self.frame)
        self.Street_No.setGeometry(QtCore.QRect(670, 170, 311, 31))
        self.Street_No.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.Street_No.setText("")
        self.Street_No.setObjectName("Street_No")
        self.L_Name = QtWidgets.QLineEdit(self.frame)
        self.L_Name.setGeometry(QtCore.QRect(170, 210, 311, 31))
        self.L_Name.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.L_Name.setText("")
        self.L_Name.setObjectName("L_Name")
        self.SysEmp = QtWidgets.QRadioButton(self.frame)
        self.SysEmp.setGeometry(QtCore.QRect(670, 300, 171, 31))
        self.SysEmp.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.SysEmp.setObjectName("SysEmp")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(540, 220, 121, 16))
        self.label_11.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_11.setObjectName("label_11")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(540, 300, 121, 16))
        self.label_16.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_16.setObjectName("label_16")
        self.Passwrd = QtWidgets.QLineEdit(self.frame)
        self.Passwrd.setGeometry(QtCore.QRect(170, 330, 311, 31))
        self.Passwrd.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.Passwrd.setObjectName("Passwrd")
        self.U_Division = QtWidgets.QLineEdit(self.frame)
        self.U_Division.setGeometry(QtCore.QRect(670, 210, 311, 31))
        self.U_Division.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.U_Division.setObjectName("U_Division")
        self.MeterNo = QtWidgets.QLineEdit(self.frame)
        self.MeterNo.setGeometry(QtCore.QRect(170, 250, 311, 31))
        self.MeterNo.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.MeterNo.setObjectName("MeterNo")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(40, 140, 121, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_7.setObjectName("label_7")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(40, 180, 121, 16))
        self.label_12.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_12.setObjectName("label_12")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(540, 260, 121, 16))
        self.label_17.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_17.setObjectName("label_17")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(420, 450, 261, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"background-color:rgb(52, 45, 113);\n"
"color:white;\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"\n"
"background-color: white;\n"
"color:rgb(52, 45, 113);\n"
"border:1px solid rgb(52, 45, 113);\n"
"transform:scale(1.2);\n"
"\n"
"}")
        self.pushButton_6.clicked.connect(lambda :self.insert_up())
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(410, 70, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout.addWidget(self.bgwidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", " ⓔ IESCO"))
        self.M_Name.setPlaceholderText(_translate("Dialog", "e.g. Musa"))
        self.SysCust.setText(_translate("Dialog", "Customer"))
        self.label_9.setText(_translate("Dialog", "House No"))
        self.label_10.setText(_translate("Dialog", "Street"))
        self.label_8.setText(_translate("Dialog", "Last Name"))
        self.H_No.setPlaceholderText(_translate("Dialog", "Enter House No"))
        self.label_15.setText(_translate("Dialog", "Password"))
        self.label_13.setText(_translate("Dialog", "Meter No"))
        self.F_Name.setPlaceholderText(_translate("Dialog", "e.g. Sara"))
        self.U_City.setPlaceholderText(_translate("Dialog", "e.g. Islamabad"))
        self.label_14.setText(_translate("Dialog", "Reference No"))
        self.Street_No.setPlaceholderText(_translate("Dialog", "Enter Street No"))
        self.L_Name.setPlaceholderText(_translate("Dialog", "e.g. Arshad"))
        self.SysEmp.setText(_translate("Dialog", "Employee of the System"))
        self.label_11.setText(_translate("Dialog", "Division"))
        self.label_16.setText(_translate("Dialog", "Are you"))
        self.Passwrd.setPlaceholderText(_translate("Dialog", "Enter Password"))
        self.U_Division.setPlaceholderText(_translate("Dialog", "Enter Division "))
        self.MeterNo.setPlaceholderText(_translate("Dialog", "981455"))
        self.label_7.setText(_translate("Dialog", "First Name"))
        self.label_12.setText(_translate("Dialog", "Middle Name"))
        self.label_17.setText(_translate("Dialog", "City"))
        self.pushButton_6.setText(_translate("Dialog", "Insert or Update"))
        self.label.setText(_translate("Dialog", "Insert or Update User Data"))

    def insert_up(self):
        try:
            msg = QMessageBox()
            if self.RefNo.text() == "" or self.MeterNo.text() == "":
                msg.setText("Fill All Required Fields")
                msg.setWindowTitle("Error")
                w = msg.exec_()
            else:
                with cx_Oracle.connect('system/Oracle123') as co:
                    cur = co.cursor()
                    RefNo = int(self.RefNo.text())
                    y = []
                    for row in cur.execute("SELECT ReferenceNO FROM PERSON"):
                        y += row
                    for x in y:
                        if x == RefNo:
                            x1 = x
                            break
                        else:
                            x1 = 0
                            continue
                    if not x1 == 0:
                        F_Name = self.F_Name.text()
                        M_Name = self.M_Name.text()
                        L_Name = self.L_Name.text()
                        MeterNo = int(self.MeterNo.text())
                        Passwrd = self.Passwrd.text()
                        H_No = self.H_No.text()
                        Street_No = self.Street_No.text()
                        U_Division = self.U_Division.text()
                        U_City = self.U_City.text()
                        SysEmp = self.SysEmp.text()
                        SysCust = self.SysCust.text()
                        print("4")
                        sql5 = """UPDATE PERSON SET F_Name=(:1),M_Name=(:2),L_Name =(:3),Street =(:4),Block=(:5),City=(:6)  WHERE ReferenceNO=(:7)"""
                        print("1")
                        sql7 = """UPDATE L_P SET loginPassword=(:1) WHERE ReferenceNO= (:2)"""
                        print("2")
                        sql6 = """UPDATE PERSON1 SET MeterNo=(:1) WHERE ReferenceNO= (:2)"""
                        print("3")
                        cur.execute(sql5, [F_Name, M_Name, L_Name, Street_No, U_Division, U_City, RefNo])
                        print("3")
                        cur.execute(sql6, [MeterNo, RefNo])
                        print("3")
                        cur.execute(sql7, [Passwrd, RefNo])
                        print("3")
                        if self.SysCust.isChecked() == True:
                            sql_0 = """UPDATE CUST_DBS SET Customer=(:1) WHERE ReferenceNO= (:2)"""
                            cur.execute(sql_0, [SysCust, RefNo])
                        elif self.SysEmp.isChecked() == True:
                            sql_1 = """UPDATE EMPL_DBS SET Employee=(:1) WHERE ReferenceNO= (:2)"""
                            cur.execute(sql_1, [SysEmp, RefNo])
                        co.commit()
                        msg = QMessageBox()
                        msg.setText("Data UPDATED SuccessFully")
                        msg.setWindowTitle("Success")
                        w = msg.exec_()
                        exit()
                    else:
                        F_Name = self.F_Name.text()
                        M_Name = self.M_Name.text()
                        L_Name = self.L_Name.text()
                        MeterNo = int(self.MeterNo.text())
                        Passwrd = self.Passwrd.text()
                        H_No = self.H_No.text()
                        Street_No = self.Street_No.text()
                        U_Division = self.U_Division.text()
                        U_City = self.U_City.text()
                        SysEmp = self.SysEmp.text()
                        SysCust = self.SysCust.text()
                        sql5 = """INSERT INTO PERSON VALUES (:1,:2,:3,:4,:5,:6,:7)"""
                        sql7 = """INSERT INTO L_P VALUES (:1,:2)"""
                        sql6 = """INSERT INTO PERSON1 VALUES (:1,:2)"""
                        cur.execute(sql5, [RefNo, F_Name, M_Name, L_Name, Street_No, U_Division, U_City])
                        cur.execute(sql6, [RefNo, MeterNo])
                        cur.execute(sql7, [RefNo, Passwrd])
                        if self.SysCust.isChecked() == True:
                            sql_0 = """INSERT INTO CUST_DBS VALUES (:1,:2)"""
                            cur.execute(sql_0, [RefNo, SysCust])
                        elif self.SysEmp.isChecked() == True:
                            sql_1 = """INSERT INTO EMPL_DBS VALUES (:1,:2)"""
                            cur.execute(sql_1, [RefNo, SysEmp])
                        co.commit()
                        msg = QMessageBox()
                        msg.setText("Data Entered SuccessFully")
                        msg.setWindowTitle("Success")
                        w = msg.exec_()
                        exit()
        except Exception as e:
            print("Error: ", str(e))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = FIn()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
