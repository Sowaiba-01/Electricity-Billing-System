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
from PyQt5 import QtCore, QtGui, QtWidgets
import cx_Oracle

class Forgot(object):
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
        self.label_3.setStyleSheet("background-image: url(../Desktop/images.qrc/man-character-thinking-free-vector.jpg);\n"
"")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../images.qrc/man-character-thinking-free-vector.jpg"))
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
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(30, 30, 261, 41))
        self.label_6.setStyleSheet("font-family:\'Montserrat\';\n"
"font-size:25px;\n"
"")
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 200, 311, 31))
        self.lineEdit_2.setStyleSheet("border-bottom: 1px solid black; ")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 250, 311, 31))
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_3.setStyleSheet("border-bottom: 1px solid black; ")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(70, 320, 261, 41))
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
        self.pushButton.clicked.connect(lambda :self.change())
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(40, 150, 311, 31))
        self.lineEdit_4.setStyleSheet("border-bottom: 1px solid black; ")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 10, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(30,144,255);\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.bgwidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "That\'s Okay! It happens. Provide Your new Password below. After authentication we will reset your password."))
        self.label_6.setText(_translate("Dialog", "Forgot Password?"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Enter Your New Password"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "Confirm Password"))
        self.pushButton.setText(_translate("Dialog", "Reset Password"))
        self.lineEdit_4.setPlaceholderText(_translate("Dialog", "Enter Your Reference No"))
        self.label.setText(_translate("Dialog", "ⓔ IESCO"))
    def change(self):
        ref_no=int(self.lineEdit_4.text())
        password=  self.lineEdit_2.text()
        con_pass = self.lineEdit_3.text()
        msg = QMessageBox()
        if con_pass == password:
            try:
                with cx_Oracle.connect('system/Oracle123') as co:
                    cur = co.cursor()
                    sql_2 = """UPDATE L_P SET loginPassword= (:1) WHERE ReferenceNO=(:2)"""
                    cur.execute(sql_2, [password,ref_no])
                    co.commit()
                    msg.setText("Password Reset Successfully")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setWindowTitle("Success")
                    msg.exec_()
            except Exception as e:
                print("Error: ", str(e))
        else:
            msg.setText("Both Passwords don't match each other")
            msg.setStandardButtons(QMessageBox.Retry)
            msg.setWindowTitle("Error")
            msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Forgot()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
