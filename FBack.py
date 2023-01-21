from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt, QDate, QTime)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint, randrange
import cx_Oracle
from PyQt5 import QtCore, QtGui, QtWidgets


class FB(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1086, 671)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setStyleSheet("QWidget#bgwidget{\n"
"    \n"
"    background-image: url(:/newPrefix/Desktop/images.qrc/home-hero-left.webp);\n"
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
        self.SubmitFdbckBtn = QtWidgets.QPushButton(self.groupBox)
        self.SubmitFdbckBtn.setGeometry(QtCore.QRect(130, 440, 211, 41))
        self.SubmitFdbckBtn.setStyleSheet("QPushButton{\n"
"background-color:rgb(30,144,255);\n"
"color:white;\n"
"border-radius:20px;\n"
"font-size:20px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"\n"
"background-color: white;\n"
"color:rgb(30,144,255);\n"
"border:1px solid rgb(30,144,255);\n"
"transform:scale(1.2);\n"
"}")
        self.SubmitFdbckBtn.setObjectName("SubmitFdbckBtn")
        self.Fdbck_Name = QtWidgets.QLineEdit(self.groupBox)
        self.Fdbck_Name.setGeometry(QtCore.QRect(160, 240, 291, 31))
        self.Fdbck_Name.setObjectName("Fdbck_Name")
        self.Fdbck_Desc = QtWidgets.QTextEdit(self.groupBox)
        self.Fdbck_Desc.setGeometry(QtCore.QRect(160, 320, 291, 71))
        self.Fdbck_Desc.setObjectName("Fdbck_Desc")
        self.F_Department = QtWidgets.QLineEdit(self.groupBox)
        self.F_Department.setGeometry(QtCore.QRect(160, 200, 291, 31))
        self.F_Department.setObjectName("F_Department")
        self.Fdbck_Category = QtWidgets.QLineEdit(self.groupBox)
        self.Fdbck_Category.setGeometry(QtCore.QRect(160, 280, 291, 31))
        self.Fdbck_Category.setText("")
        self.Fdbck_Category.setObjectName("Fdbck_Category")
        self.label_33 = QtWidgets.QLabel(self.groupBox)
        self.label_33.setGeometry(QtCore.QRect(50, 330, 121, 16))
        self.label_33.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_33.setObjectName("label_33")
        self.Fdbck_Category_2 = QtWidgets.QLineEdit(self.groupBox)
        self.Fdbck_Category_2.setGeometry(QtCore.QRect(160, 280, 291, 31))
        self.Fdbck_Category_2.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;\n"
"")
        self.Fdbck_Category_2.setText("")
        self.Fdbck_Category_2.setObjectName("Fdbck_Category_2")
        self.F_Department_2 = QtWidgets.QLineEdit(self.groupBox)
        self.F_Department_2.setGeometry(QtCore.QRect(160, 200, 291, 31))
        self.F_Department_2.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;\n"
"")
        self.F_Department_2.setObjectName("F_Department_2")
        self.label_34 = QtWidgets.QLabel(self.groupBox)
        self.label_34.setGeometry(QtCore.QRect(50, 290, 121, 16))
        self.label_34.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.label_34.setObjectName("label_34")
        self.Fdbck_Desc_2 = QtWidgets.QTextEdit(self.groupBox)
        self.Fdbck_Desc_2.setGeometry(QtCore.QRect(160, 320, 291, 71))
        self.Fdbck_Desc_2.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;\n"
"")
        self.Fdbck_Desc_2.setObjectName("Fdbck_Desc_2")
        self.SubmitFdbckBtn_2 = QtWidgets.QPushButton(self.groupBox)
        self.SubmitFdbckBtn_2.setGeometry(QtCore.QRect(130, 440, 271, 41))
        self.SubmitFdbckBtn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SubmitFdbckBtn_2.setStyleSheet("QPushButton{\n"
"background-color:rgb(30,144,255);\n"
"color:white;\n"
"border-radius:20px;\n"
"font-size:20px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"\n"
"background-color: white;\n"
"color:rgb(30,144,255);\n"
"border:1px solid rgb(30,144,255);\n"
"transform:scale(1.2);\n"
"}")
        self.SubmitFdbckBtn_2.clicked.connect(lambda : self.valueEntry())
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
        self.label_2.setStyleSheet("background-image: url(:/newPrefix/Desktop/images.qrc/FeedbackImage.jpg);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../images.qrc/FeedbackImage.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(50, 50, 381, 51))
        self.label_3.setStyleSheet("font: 80 15pt \"MS Shell Dlg 2\";color:rgb(30,144,255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(820, 30, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_4.setStyleSheet("color:rgb(30,144,255);")
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
        self.SubmitFdbckBtn.setText(_translate("Dialog", "Submit"))
        self.Fdbck_Name.setPlaceholderText(_translate("Dialog", "Name"))
        self.Fdbck_Desc.setPlaceholderText(_translate("Dialog", "Description"))
        self.F_Department.setPlaceholderText(_translate("Dialog", "Department"))
        self.Fdbck_Category.setPlaceholderText(_translate("Dialog", "Category"))
        self.label_33.setText(_translate("Dialog", "Description"))
        self.Fdbck_Category_2.setPlaceholderText(_translate("Dialog", "e.g. A or B"))
        self.F_Department_2.setPlaceholderText(_translate("Dialog", "e.g. Software or Communication"))
        self.label_34.setText(_translate("Dialog", "Category"))
        self.Fdbck_Desc_2.setPlaceholderText(_translate("Dialog", "Give your feedback.."))
        self.SubmitFdbckBtn_2.setText(_translate("Dialog", "Send Feedback"))
        self.label_35.setText(_translate("Dialog", "Name"))
        self.label_36.setText(_translate("Dialog", "Department"))
        self.Fdbck_Name_2.setPlaceholderText(_translate("Dialog", "e.g. Rubab"))
        self.label_3.setText(_translate("Dialog", "Your Feedback Matters The Most!"))
        self.label_4.setText(_translate("Dialog", "ⓔ IESCO"))
        self.F_Department_3.setPlaceholderText(_translate("Dialog", "e.g. 10045"))
        self.label_37.setText(_translate("Dialog", "Reference Number"))

    def valueEntry(self):
        try:
            ref_no=int(self.F_Department_3.text())
            with cx_Oracle.connect('system/Oracle123') as co:
                cur = co.cursor()
                sql = """Select ReferenceNO FROM PERSON"""
                cur.execute(sql)
                x = cur.fetchall()
                y=[]
                for row in x:
                    for x in row:
                        y.append(x)
                if (ref_no) in y:
                    dep = self.F_Department_2.text()
                    name = self.Fdbck_Name_2.text()
                    cate = self.Fdbck_Category_2.text()
                    feedback = self.Fdbck_Desc_2.toPlainText()
                    feed_id= randint(1, 2000)
                    sql4 = """INSERT INTO Feed_bac VALUES (:1,:2,:3,:4,:5,:6)"""
                    cur.execute(sql4, [feed_id,feedback,dep,name,cate,ref_no])
                    co.commit()
                    msg = QMessageBox()
                    msg.setText("Thanks For Feedback")
                    msg.setWindowTitle("Success")
                    w = msg.exec_()
                    exit()
                else:
                    msg = QMessageBox()
                    msg.setText("You can not give feedback. You are not a member")
                    msg.setWindowTitle("Error")
                    w = msg.exec_()
        except Exception as e:
            print("Error: ", str(e))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = FB()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
