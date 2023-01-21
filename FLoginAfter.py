from PyQt5 import QtWidgets
import time
from datetime import datetime
from datetime import date
from datetime import datetime, timedelta
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt, QDate, QTime)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
import cx_Oracle
from FAfterLogin import AfterLogin
from PyQt5 import QtCore, QtGui, QtWidgets
from FForgot import Forgot
from FSignU import SignUp
from random import randint, randrange
count = 0
class Login1(object):

    def openWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = AfterLogin()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow2(self):
        self.window = QtWidgets.QDialog()
        self.ui = SignUp()
        self.ui.setupUi(self.window)
        self.window.show()

    def openWindow3(self):
        self.window = QtWidgets.QDialog()
        self.ui = Forgot()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1086, 554)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setStyleSheet("QWidget#bgwidget\n"
"{\n"
"background-image: url(../images.qrc/home-hero-left.webp);\n"
"background-repeat:no-repeat;\n"
"};\n"
"")
        self.bgwidget.setObjectName("bgwidget")
        self.groupBox = QtWidgets.QGroupBox(self.bgwidget)
        self.groupBox.setGeometry(QtCore.QRect(90, 49, 901, 441))
        self.groupBox.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 0, 501, 441))
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_3.setStyleSheet("background-image: url(:/newPrefix/Desktop/images.qrc/istockphoto-1296488320-612x612.jpg);\n"
"")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../images.qrc/istockphoto-1296488320-612x612.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setGeometry(QtCore.QRect(500, 0, 401, 441))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(30, 70, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(True)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(150, 360, 101, 23))
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("border: 0px;\n"
"color: rgb(30,144,255);;")
        self.pushButton_7.clicked.connect(lambda : self.openWindow3())
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(30, 30, 261, 41))
        self.label_6.setStyleSheet("font-family:\'Montserrat\';\n"
"font-size:25px;\n"
"")
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 150, 231, 31))
        self.lineEdit_2.setStyleSheet("border-bottom: 1px solid black; ")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 200, 231, 31))
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_3.setStyleSheet("border-bottom: 1px solid black; ")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(70, 270, 261, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)

        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color:rgb(30,144,255);\n"
"color:white;\n"
"border-radius:20px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"\n"
"background-color: white;\n"
"color:rgb(30,144,255);\n"
"border:1px solid rgb(30,144,255);\n"
"transform:scale(1.2);\n"
"\n"
"}")
        self.pushButton.clicked.connect(
            lambda: self.ref_checker())
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 320, 261, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("\n"
"QPushButton{\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(245,245,245);\n"
"color:black;\n"
"border-radius:20px;\n"
"\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"\n"
"background-color: black;\n"
"color: rgb(245,245,245);\n"
"border-radius:20px;\n"
"\n"
"}\n"
"")
        self.pushButton_2.clicked.connect(
            lambda: self.openWindow2())
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.bgwidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "To keep connected with us, please login with your personal information by reference number and you password."))
        self.pushButton_7.setText(_translate("Dialog", "Forget Password?"))
        self.label_6.setText(_translate("Dialog", "Welcome Back :)"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Reference No"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "Password"))
        self.pushButton.setText(_translate("Dialog", "Login In"))
        self.pushButton_2.setText(_translate("Dialog", "Create Account"))


    def ref_checker(self):
        global count
        msg = QMessageBox()
        if self.lineEdit_2.text() == "" or self.lineEdit_3.text() == "" :
            msg.setText("Fill All Required Fields")
            msg.setWindowTitle("Error")
            w = msg.exec_()
            self.lineEdit_2.setStyleSheet("QLineEdit:Focus\n"
                                          "{\n"
                                          "border-bottom:2px solid red;\n"
                                          "}\n""QLineEdit\n"
"{\n"
"border-bottom: 1px solid black; \n"
"}")

            self.lineEdit_2.setFocus()
            self.lineEdit_3.setStyleSheet("QLineEdit:Focus\n"
                                          "{\n"
                                          "border-bottom:2px solid red;\n"
                                          "}\n""QLineEdit\n"
"{\n"
"border-bottom: 1px solid black; \n"
"}")

            self.lineEdit_3.setFocus()
        else:
             try:
                ref_no = self.lineEdit_2.text()
                Error_Ocuurance = "Reference NO " + ref_no+" logged in 3 times incorrectly"
                Error_location="Log in"
                ref_no = int(self.lineEdit_2.text())
                pas = self.lineEdit_3.text()
                alert_id=randint(1, 2000)
                global value
                with cx_Oracle.connect('system/Oracle123') as co:
                    cur = co.cursor()
                    y = []
                    sql = """Select * FROM L_P WHERE ReferenceNO=(:1) AND loginPassword=(:2)"""
                    cur.execute(sql, [ref_no, pas])
                    x = cur.fetchall()
                    now = datetime.now()
                    current_time = str(now.strftime("%H:%M:%S"))
                    today = str(date.today())
                    total = today+" "+current_time
                    for row in x:
                        for x in row:
                            y.append(x)
                    print(y)
                    print(total)
                    if (ref_no and str(pas)) in y:
                        with cx_Oracle.connect('system/Oracle123') as co:
                            cur = co.cursor()
                            sql_4 = """INSERT INTO LO_IN(ReferenceNO) VALUES (:1)"""
                            cur.execute(sql_4, [ref_no])
                            co.commit()
                        self.pushButton.clicked.connect(self.openWindow())
                    else:
                        count += 1
                        if count == 3:
                            with cx_Oracle.connect('system/Oracle123') as co:
                                cur = co.cursor()
                                sql6 = """INSERT INTO ALERT_SYS VALUES (:1,:2,:3,:4)"""
                                cur.execute(sql6, [alert_id, Error_Ocuurance, Error_location, 9801])
                                co.commit()
                            msg.setText("You Logged in 3 times incorrectly! ")
                            msg.setInformativeText("See Details")
                            msg.setDetailedText("You have logged in 3 times incorrectly. Beacuse of security reason an alert has been sent to admin. Your account will be active after 1 hour now. If you don't remenber your password. Press Forgot password button. ")
                            msg.setWindowTitle("Error")
                            w = msg.exec_()
                            self.openWindow3()
                        else:
                            msg.setText("Invalid User Credentials")
                            msg.setWindowTitle("Error")
                            w = msg.exec_()
             except Exception as e:
                print("Error: ", str(e))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Login1()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
