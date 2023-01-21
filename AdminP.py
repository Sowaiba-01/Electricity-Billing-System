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
from AdDash import Admin

class AD_Portal(object):
    def openWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Admin()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1216, 589)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setStyleSheet("QWidget#bgwidget\n"
"{\n"
"background-image: url(../images.qrc/vecteezy_hexagon-abstract-modern-background-with-overlapping-triangle_5909540.jpg);\n"
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
"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(70, 60, 351, 71))
        self.label_6.setStyleSheet("font-family:\'Montserrat\';\n"
"font-size:25px;\n"
"")
        self.label_6.setObjectName("label_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(130, 350, 181, 41))
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
        self.pushButton_6.clicked.connect(lambda : self.credentials())
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 200, 231, 31))
        self.lineEdit_4.setStyleSheet("font-family:\'Montserrat\';border:none;\n"
"border-bottom:1px solid black;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 280, 231, 31))
        self.lineEdit_5.setAutoFillBackground(False)
        self.lineEdit_5.setStyleSheet("border:none;\n"
"border-bottom:1px solid black;\n"
"font-family:\'Montserrat\';")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(70, 180, 111, 16))
        self.label.setStyleSheet("font-size:12px;\n"
"font-family:\'Montserrat\';")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(70, 260, 111, 16))
        self.label_2.setStyleSheet("font-size:12px;\n"
"font-family:\'Montserrat\';")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(541, 32, 530, 451))
        self.label_3.setStyleSheet("\n"
"background-image: url(../images.qrc/istockphoto-1217246641-612x612.jpg);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../images.qrc/istockphoto-1387500458-612x612.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(980, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(52, 45, 113);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.groupBox)
        self.verticalLayout.addWidget(self.bgwidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_6.setText(_translate("Dialog", "Welcome To The Admin Portal"))
        self.pushButton_6.setText(_translate("Dialog", "Login"))
        self.lineEdit_4.setPlaceholderText(_translate("Dialog", "Enter Your Name"))
        self.lineEdit_5.setPlaceholderText(_translate("Dialog", "Enter Password"))
        self.label.setText(_translate("Dialog", "Name"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.label_4.setText(_translate("Dialog", "ⓔ IESCO"))

    def credentials(self):
        msg = QMessageBox()
        AdminName = self.lineEdit_4.text()
        AdminPass = self.lineEdit_5.text()
        y = ["Sora9801","sora@123"]
        if (AdminName and AdminPass) in y:
           self.openWindow()
        else:
            msg.setText("Invalid User credentials")
            msg.setStandardButtons(QMessageBox.Retry)
            w = msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = AD_Portal()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
