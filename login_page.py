# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_page.ui',
# licensing of 'login_page.ui' applies.
#
# Created: Thu May 30 16:07:22 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from part_1_register_page import *
from main_page import Ui_main_page
from login import Login

class Ui_login_page(object):

    def __init__(self):
        self.msg = None
        self.login = None
    
    def show_error_dialog(self):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Critical)
        self.msg.setText  (" !!! -- Error -- !!! ")
        self.msg.setInformativeText("You forgot to input email or password or both email and password")
        self.msg.setWindowTitle("Error")
        self.msg.show()

    def log_in_to_your_account(self):
        
        email = self.email_input.text()
        password = self.password_input.text()

        self.login = Login(email, password) 
        self.token = self.login.user_login()
        if(self.login.get_status_code() == 200): 
                self.token = self.login.user_login()
                self.main_page = QtWidgets.QWidget()
                self.ui = Ui_main_page(self.login, self.token)
                self.ui.setupUi(self.main_page)
                self.login_page.hide()
                self.main_page.show()
        else:
                self.show_error_dialog()

    def register_page(self):
        self.register_page = QtWidgets.QWidget()
        self.ui = Ui_part_1_register_page()
        self.ui.setupUi(self.register_page)
        self.login_page.hide()
        self.register_page.show()

        
    
    def setupUi(self, login_page):
        self.login_page = login_page
        login_page.setObjectName("login_page")
        login_page.resize(1600, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(login_page.sizePolicy().hasHeightForWidth())
        login_page.setSizePolicy(sizePolicy)
        login_page.setMinimumSize(QtCore.QSize(1600, 900))
        login_page.setMaximumSize(QtCore.QSize(1600, 900))
        login_page.setWindowOpacity(1.0)
        login_page.setLayoutDirection(QtCore.Qt.LeftToRight)
        login_page.setAutoFillBackground(False)
        login_page.setStyleSheet("\n"
"\n"
"background-image: url(./image/login_wallpaper_2.png);\n"
"\n"
"background-size: cover;\n"
"\n"
"opacity : 0.7;\n"
"\n"
"")
        self.orange_background = QtWidgets.QLabel(login_page)
        self.orange_background.setGeometry(QtCore.QRect(0, 0, 1600, 900))
        self.orange_background.setCursor(QtCore.Qt.PointingHandCursor)
        self.orange_background.setStyleSheet("background: rgba(255, 140, 0 , 0.30);\n"
"\n"
"opacity: 0.69;\n"
"\n"
"")
        self.orange_background.setFrameShadow(QtWidgets.QFrame.Plain)
        self.orange_background.setText("")
        self.orange_background.setObjectName("orange_background")
        self.create_an_account_Button = QtWidgets.QPushButton(login_page)
        self.create_an_account_Button.clicked.connect(self.register_page)
        self.create_an_account_Button.setGeometry(QtCore.QRect(1220, 30, 347, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(22)
        self.create_an_account_Button.setFont(font)
        self.create_an_account_Button.setCursor(QtCore.Qt.PointingHandCursor)
        self.create_an_account_Button.setStyleSheet("color : white;\n"
"background : #1347EC;\n"
"border-radius : 30px;\n"
"")
        self.create_an_account_Button.setObjectName("create_an_account_Button")
        self.welcome_back_label = QtWidgets.QLabel(login_page)
        self.welcome_back_label.setGeometry(QtCore.QRect(630, 140, 361, 60))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(36)
        font.setWeight(75)
        font.setBold(True)
        self.welcome_back_label.setFont(font)
        self.welcome_back_label.setStyleSheet("background: transparent;")
        self.welcome_back_label.setObjectName("welcome_back_label")
        self.description_label = QtWidgets.QLabel(login_page)
        self.description_label.setGeometry(QtCore.QRect(250, 210, 1154, 67))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(30)
        self.description_label.setFont(font)
        self.description_label.setStyleSheet("background: transparent\n"
"")
        self.description_label.setObjectName("description_label")
        self.email_label = QtWidgets.QLabel(login_page)
        self.email_label.setGeometry(QtCore.QRect(540, 330, 191, 39))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        self.email_label.setFont(font)
        self.email_label.setStyleSheet("background: transparent;")
        self.email_label.setObjectName("email_label")
        self.email_input = QtWidgets.QLineEdit(login_page)
        self.email_input.setGeometry(QtCore.QRect(540, 390, 535, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(20)
        self.email_input.setFont(font)
        self.email_input.setText("")
        self.email_input.setObjectName("email_input")
        self.password_label = QtWidgets.QLabel(login_page)
        self.password_label.setGeometry(QtCore.QRect(540, 490, 231, 39))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet("background: transparent;")
        self.password_label.setObjectName("password_label")
        self.password_input = QtWidgets.QLineEdit(login_page)
        self.password_input.setGeometry(QtCore.QRect(540, 560, 535, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Medium")
        font.setPointSize(18)
        self.password_input.setFont(font)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setText("")
        self.password_input.setObjectName("password_input")
        self.log_in_Button = QtWidgets.QPushButton(login_page)
        self.log_in_Button.clicked.connect(self.log_in_to_your_account)
        self.log_in_Button.setGeometry(QtCore.QRect(540, 660, 535, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(22)
        self.log_in_Button.setFont(font)
        self.log_in_Button.setCursor(QtCore.Qt.PointingHandCursor)
        self.log_in_Button.setStyleSheet("color : white;\n"
"background : #1347EC;\n"
"border-radius : 30px;")
        self.log_in_Button.setObjectName("log_in_Button")
        self.need_an_account_label = QtWidgets.QLabel(login_page)
        self.need_an_account_label.setGeometry(QtCore.QRect(540, 760, 275, 39))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        self.need_an_account_label.setFont(font)
        self.need_an_account_label.setStyleSheet("background: transparent;")
        self.need_an_account_label.setObjectName("need_an_account_label")
        self.create_your_account_label = QtWidgets.QPushButton(login_page)
        self.create_your_account_label.clicked.connect(self.register_page)
        self.create_your_account_label.setGeometry(QtCore.QRect(840, 760, 291, 30))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(18)
        font.setWeight(50)
        font.setUnderline(False)
        font.setBold(False)
        self.create_your_account_label.setFont(font)
        self.create_your_account_label.setCursor(QtCore.Qt.PointingHandCursor)
        self.create_your_account_label.setStyleSheet("color : blue;\n"
"background: transparent;\n"
"\n"
"")
        self.create_your_account_label.setObjectName("create_your_account_label")

        self.retranslateUi(login_page)
        QtCore.QMetaObject.connectSlotsByName(login_page)

    def retranslateUi(self, login_page):
        login_page.setWindowTitle(QtWidgets.QApplication.translate("login_page", "First_page", None, -1))
        self.create_an_account_Button.setText(QtWidgets.QApplication.translate("login_page", "Create an account", None, -1))
        self.welcome_back_label.setText(QtWidgets.QApplication.translate("login_page", "Welcome Back", None, -1))
        self.description_label.setText(QtWidgets.QApplication.translate("login_page", "Log in to access your profile, dashboard and setting ", None, -1))
        self.email_label.setText(QtWidgets.QApplication.translate("login_page", "EMAIL", None, -1))
        self.password_label.setText(QtWidgets.QApplication.translate("login_page", "PASSWORD", None, -1))
        self.log_in_Button.setText(QtWidgets.QApplication.translate("login_page", "Log in to your account", None, -1))
        self.need_an_account_label.setText(QtWidgets.QApplication.translate("login_page", "Need an account?", None, -1))
        self.create_your_account_label.setText(QtWidgets.QApplication.translate("login_page", "Create your account ", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_page = QtWidgets.QWidget()
    ui = Ui_login_page()
    ui.setupUi(login_page)
    login_page.show()
    sys.exit(app.exec_())

