from PyQt5 import QtCore, QtGui, QtWidgets
import time
import cx_Oracle
from datetime import date
from datetime import datetime, timedelta
from PyQt5 import QtWidgets

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt, QDate, QTime)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QPushButton
from random import randint, randrange

class G_Bill(object):
    def openWindow(self):
        exit()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1390, 744)
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setMaximumSize(QtCore.QSize(1500, 1000))
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
"    background-image:  url(../images.qrc/vecteezy_hexagon-abstract-modern-background-with-overlapping-triangle_5909540.jpg);\n"
"background-repeat:no-repeat;\n"
"};\n"
"")
        self.bgwidget.setObjectName("bgwidget")
        self.frame = QtWidgets.QFrame(self.bgwidget)
        self.frame.setGeometry(QtCore.QRect(60, 50, 1221, 621))
        self.frame.setMaximumSize(QtCore.QSize(16777, 16777215))
        self.frame.setStyleSheet("QFrame#frame\n"
"{\n"
"    \n"
"    background-color:white;\n"
"border-radius: 10px;\n"
"};")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(280, 10, 591, 86))
        self.label_3.setStyleSheet("font-family:\'Montserrat\';\n"
"font-size:30px;\n"
"color:rgb(52, 45, 113);")
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(90, 100, 521, 411))
        self.groupBox.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.groupBox.setObjectName("groupBox")
        self.label_28 = QtWidgets.QLabel(self.groupBox)
        self.label_28.setGeometry(QtCore.QRect(40, 100, 121, 16))
        self.label_28.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.groupBox)
        self.label_29.setGeometry(QtCore.QRect(40, 260, 121, 16))
        self.label_29.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_29.setObjectName("label_29")
        self.BillMeterNo = QtWidgets.QLineEdit(self.groupBox)
        self.BillMeterNo.setGeometry(QtCore.QRect(170, 210, 311, 31))
        self.BillMeterNo.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.BillMeterNo.setText("")
        self.BillMeterNo.setObjectName("BillMeterNo")
        self.label_30 = QtWidgets.QLabel(self.groupBox)
        self.label_30.setGeometry(QtCore.QRect(40, 180, 121, 16))
        self.label_30.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_30.setObjectName("label_30")
        self.BillDueDate = QtWidgets.QLineEdit(self.groupBox)
        self.BillDueDate.setGeometry(QtCore.QRect(170, 130, 311, 31))
        self.BillDueDate.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.BillDueDate.setText("")
        self.BillDueDate.setObjectName("BillDueDate")
        self.BillDateIssued = QtWidgets.QLineEdit(self.groupBox)
        self.BillDateIssued.setGeometry(QtCore.QRect(170, 90, 311, 31))
        self.BillDateIssued.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.BillDateIssued.setObjectName("BillDateIssued")
        self.label_31 = QtWidgets.QLabel(self.groupBox)
        self.label_31.setGeometry(QtCore.QRect(40, 220, 121, 16))
        self.label_31.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.groupBox)
        self.label_32.setGeometry(QtCore.QRect(40, 60, 121, 16))
        self.label_32.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_32.setObjectName("label_32")
        self.BillRefNo = QtWidgets.QLineEdit(self.groupBox)
        self.BillRefNo.setGeometry(QtCore.QRect(170, 170, 311, 31))
        self.BillRefNo.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.BillRefNo.setObjectName("BillRefNo")
        self.MeterPrevRdng = QtWidgets.QLineEdit(self.groupBox)
        self.MeterPrevRdng.setGeometry(QtCore.QRect(170, 250, 311, 31))
        self.MeterPrevRdng.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.MeterPrevRdng.setObjectName("MeterPrevRdng")
        self.Bill_ID = QtWidgets.QLineEdit(self.groupBox)
        self.Bill_ID.setGeometry(QtCore.QRect(170, 50, 311, 31))
        self.Bill_ID.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.Bill_ID.setObjectName("Bill_ID")
        self.label_33 = QtWidgets.QLabel(self.groupBox)
        self.label_33.setGeometry(QtCore.QRect(40, 140, 121, 16))
        self.label_33.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_33.setObjectName("label_33")
        self.MeterPresRdng = QtWidgets.QLineEdit(self.groupBox)
        self.MeterPresRdng.setGeometry(QtCore.QRect(170, 290, 311, 31))
        self.MeterPresRdng.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.MeterPresRdng.setObjectName("MeterPresRdng")
        self.label_34 = QtWidgets.QLabel(self.groupBox)
        self.label_34.setGeometry(QtCore.QRect(40, 300, 121, 16))
        self.label_34.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_34.setObjectName("label_34")
        self.Units_consumed = QtWidgets.QLineEdit(self.groupBox)
        self.Units_consumed.setGeometry(QtCore.QRect(170, 330, 311, 31))
        self.Units_consumed.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.Units_consumed.setObjectName("Units_consumed")
        self.label_35 = QtWidgets.QLabel(self.groupBox)
        self.label_35.setGeometry(QtCore.QRect(40, 340, 121, 16))
        self.label_35.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_35.setObjectName("label_35")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setGeometry(QtCore.QRect(650, 100, 521, 281))
        self.groupBox_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_37 = QtWidgets.QLabel(self.groupBox_3)
        self.label_37.setGeometry(QtCore.QRect(40, 50, 121, 16))
        self.label_37.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_37.setObjectName("label_37")
        self.ElecDuty_tax = QtWidgets.QLineEdit(self.groupBox_3)
        self.ElecDuty_tax.setGeometry(QtCore.QRect(170, 40, 311, 31))
        self.ElecDuty_tax.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.ElecDuty_tax.setObjectName("ElecDuty_tax")
        self.label_38 = QtWidgets.QLabel(self.groupBox_3)
        self.label_38.setGeometry(QtCore.QRect(40, 90, 121, 16))
        self.label_38.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_38.setObjectName("label_38")
        self.TVFee_TAx = QtWidgets.QLineEdit(self.groupBox_3)
        self.TVFee_TAx.setGeometry(QtCore.QRect(170, 80, 311, 31))
        self.TVFee_TAx.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.TVFee_TAx.setObjectName("TVFee_TAx")
        self.label_39 = QtWidgets.QLabel(self.groupBox_3)
        self.label_39.setGeometry(QtCore.QRect(40, 130, 121, 16))
        self.label_39.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_39.setObjectName("label_39")
        self.GST_tax = QtWidgets.QLineEdit(self.groupBox_3)
        self.GST_tax.setGeometry(QtCore.QRect(170, 120, 311, 31))
        self.GST_tax.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.GST_tax.setObjectName("GST_tax")
        self.IncomeTax = QtWidgets.QLineEdit(self.groupBox_3)
        self.IncomeTax.setGeometry(QtCore.QRect(170, 160, 311, 31))
        self.IncomeTax.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.IncomeTax.setObjectName("IncomeTax")
        self.label_40 = QtWidgets.QLabel(self.groupBox_3)
        self.label_40.setGeometry(QtCore.QRect(40, 170, 121, 16))
        self.label_40.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.groupBox_3)
        self.label_41.setGeometry(QtCore.QRect(40, 210, 121, 16))
        self.label_41.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_41.setObjectName("label_41")
        self.TaxTotal = QtWidgets.QLineEdit(self.groupBox_3)
        self.TaxTotal.setGeometry(QtCore.QRect(170, 200, 311, 31))
        self.TaxTotal.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.TaxTotal.setObjectName("TaxTotal")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_4.setGeometry(QtCore.QRect(650, 390, 521, 121))
        self.groupBox_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_42 = QtWidgets.QLabel(self.groupBox_4)
        self.label_42.setGeometry(QtCore.QRect(40, 50, 121, 16))
        self.label_42.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_42.setObjectName("label_42")
        self.BillTotal = QtWidgets.QLineEdit(self.groupBox_4)
        self.BillTotal.setGeometry(QtCore.QRect(170, 40, 311, 31))
        self.BillTotal.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;")
        self.BillTotal.setObjectName("BillTotal")
        self.GenerateBill = QtWidgets.QPushButton(self.frame)
        self.GenerateBill.setGeometry(QtCore.QRect(360, 530, 251, 51))
        self.GenerateBill.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GenerateBill.setStyleSheet("QPushButton{\n"
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
"\n"
"}")
        self.GenerateBill.clicked.connect(lambda :self.generation_of_bill())
        self.GenerateBill.setObjectName("GenerateBill")
        self.ExitButton = QtWidgets.QPushButton(self.frame)
        self.ExitButton.setGeometry(QtCore.QRect(650, 530, 251, 51))
        self.ExitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ExitButton.setStyleSheet("QPushButton{\n"
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
"\n"
"}")
        self.ExitButton.clicked.connect(lambda :self.openWindow())
        self.ExitButton.setObjectName("ExitButton")
        self.verticalLayout.addWidget(self.bgwidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Generate Bill"))
        self.groupBox.setTitle(_translate("Dialog", "Bill Info"))
        self.label_28.setText(_translate("Dialog", "Date Issued"))
        self.label_29.setText(_translate("Dialog", "Previous Reading"))
        self.label_30.setText(_translate("Dialog", "Reference No"))
        self.label_31.setText(_translate("Dialog", "Meter No"))
        self.label_32.setText(_translate("Dialog", "Bill ID"))
        self.label_33.setText(_translate("Dialog", "Due Date"))
        self.label_34.setText(_translate("Dialog", "Present Reading"))
        self.label_35.setText(_translate("Dialog", "Units Consumed"))
        self.groupBox_3.setTitle(_translate("Dialog", "Taxes Applied"))
        self.label_37.setText(_translate("Dialog", "Electricity Duty"))
        self.label_38.setText(_translate("Dialog", "TV Fee"))
        self.label_39.setText(_translate("Dialog", "GST"))
        self.label_40.setText(_translate("Dialog", "Income Tax"))
        self.label_41.setText(_translate("Dialog", "GRAND TOTAL"))
        self.groupBox_4.setTitle(_translate("Dialog", "Total Bill"))
        self.label_42.setText(_translate("Dialog", "Total Bill"))
        self.GenerateBill.setText(_translate("Dialog", "Generate"))
        self.ExitButton.setText(_translate("Dialog", "Exit"))
    def generation_of_bill(self):
     try:
        print(123)
        msg = QMessageBox()
        ref_no = int(self.BillRefNo.text())
        with cx_Oracle.connect('system/Oracle123') as co:
            cur = co.cursor()
            sql3 = """SELECT ReferenceNO FROM B_X WHERE ReferenceNO=(:1)"""
            cur.execute(sql3, [ref_no])
            x = cur.fetchone()
            print(x)
        if not x:
                print(123)
                bill_id = randint(10, 50000)
                due = date.today()
                date_issued = due - timedelta(days=30)
                ref_no = int(self.BillRefNo.text())
                with cx_Oracle.connect('system/Oracle123') as co:
                    cur = co.cursor()
                    sql3 = """SELECT MeterNo FROM PERSON1 WHERE ReferenceNO=(:1)"""
                    cur.execute(sql3, [ref_no])
                    x = cur.fetchone()
                    for row in x:
                       x1 = row
                bill_sys_id=9801
                units = randint(100, 400)
                duty = randint(1, 10)
                tv_fee = randint(1, 10)
                GST = randint(10, 100)
                income = randint(100, 200)
                grand = duty + tv_fee + GST + income
                bill_gen = (units * 72 * 10) + grand
                ChareRate=15
                PerUnitCost=9
                InvoiceNO=str(randint(10, 2000))
                encoded_by = "Sowaiba Arshad"
                status = 'Active'
                with cx_Oracle.connect('system/Oracle123') as co:
                    cur = co.cursor()
                    sql3 = """INSERT INTO B_X VALUES (:1,:2,:3,:4,:5,:6,:7)"""
                    cur.execute(sql3, [bill_id, ref_no, due, date_issued, units, x1, bill_sys_id])
                    sql4 = """INSERT INTO B_TAX VALUES (:1,:2)"""
                    cur.execute(sql4, [bill_id, grand])
                    sql5 = """INSERT INTO BI_INFO VALUES (:1,:2,:3,:4)"""
                    cur.execute(sql5, [ChareRate, PerUnitCost, InvoiceNO, bill_id])
                    sql1 = """INSERT INTO B_S VALUES (:1,:2,:3,:4)"""
                    cur.execute(sql1, [bill_sys_id,due, encoded_by, status])
                    sql2 = """INSERT INTO B_S_1 VALUES (:1,:2,:3)"""
                    cur.execute(sql2, [bill_sys_id, bill_id,bill_gen])
                    sql_1 = """INSERT INTO BS_2 VALUES (:1,:2,:3,:4)"""
                    cur.execute(sql_1, [bill_id, status,date_issued,due])

                    co.commit()
                units = str(units)
                duty = str(duty)
                tv_fee = str(tv_fee)
                GST = str(GST)
                income = str(income)
                grand = str(grand)
                bill_gen = str(bill_gen)
                bill_id = str(bill_id)
                due = str(due)
                date_issued = str(date_issued)
                x1 = str(x1)
                self.BillMeterNo.setText(x1)
                self.MeterPrevRdng.setText("83107")
                self.MeterPresRdng.setText("10324")
                self.BillDateIssued.setText(date_issued)
                self.BillDueDate.setText(due)
                self.Bill_ID.setText(bill_id)
                self.Units_consumed.setText(units)
                self.ElecDuty_tax.setText(duty)
                self.TVFee_TAx.setText(tv_fee)
                self.GST_tax.setText(GST)
                self.IncomeTax.setText(income)
                self.TaxTotal.setText(grand)
                self.BillTotal.setText("Rs " + bill_gen)
        else:
                ref_no = str(ref_no)
                msg.setText("Bill already generated for Reference No "+ref_no)
                msg.setStandardButtons(QMessageBox.Ok)
                w = msg.exec_()
     except Exception as e:
         print("Error: ", str(e))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = G_Bill()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
