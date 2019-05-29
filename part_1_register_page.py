# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'part_1_register_page.ui',
# licensing of 'part_1_register_page.ui' applies.
#
# Created: Sun May  5 23:50:55 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!
import sys
from PySide2 import QtCore, QtGui, QtWidgets
from part_2_register_page import Ui_part_2_register_page
from register import Register

class Ui_part_1_register_page(object):

    def __init__(self):
        self.register = None

    def show_error_dialog(self):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Critical)
        self.msg.setText  (" !!! -- Error -- !!! ")
        self.msg.setInformativeText("You forgot to input email or password or both email and password")
        self.msg.setWindowTitle("Error")
        self.msg.show()
    
    def part_2_register_page(self):
        self.part_2_register_page = QtWidgets.QWidget()
        self.ui = Ui_part_2_register_page()
        self.ui.setupUi(self.part_2_register_page)
        self.part_1_register_page.hide()
        self.part_2_register_page.show()

    def next_page(self):
        name = self.name_lineEdit.text()
        email = self.email_lineEdit.text()
        password = self.password_lineEdit.text()  

        if(name == " " or email == " " or password == " "):
                print("Invalid input")
                self.show_error_dialog()
        
        else:
                self.register = Register(name, email, password)
                print(self.register.get_name(), self.register.get_email(), self.register.get_password(), self.register.get_weight())
                self.part_2_register_page()

    def setupUi(self, part_1_register_page):
        self.part_1_register_page = part_1_register_page
        part_1_register_page.setObjectName("part_1_register_page")
        part_1_register_page.resize(1920, 1080)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(part_1_register_page.sizePolicy().hasHeightForWidth())
        part_1_register_page.setSizePolicy(sizePolicy)
        part_1_register_page.setStyleSheet("background-image: url(./image/black_register_wallpaper.jpg);\n"
"\n"
" background-size: contain;\n"
"background-repeat: no-repeat;\n"
"\n"
"")
        self.register_label = QtWidgets.QLabel(part_1_register_page)
        self.register_label.setGeometry(QtCore.QRect(887, 116, 215, 78))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(38)
        font.setWeight(75)
        font.setBold(True)
        self.register_label.setFont(font)
        self.register_label.setStyleSheet("color : #FFE4C4;\n"
"border-color : #FFE4C4;\n"
"background : transparent;\n"
"")
        self.register_label.setObjectName("register_label")
        self.first_sentence_label = QtWidgets.QLabel(part_1_register_page)
        self.first_sentence_label.setGeometry(QtCore.QRect(390, 210, 1208, 67))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(30)
        self.first_sentence_label.setFont(font)
        self.first_sentence_label.setStyleSheet("color : #FFF;\n"
"border-color : #FFF;\n"
"background : transparent;")
        self.first_sentence_label.setObjectName("first_sentence_label")
        self.second_sentence_label = QtWidgets.QLabel(part_1_register_page)
        self.second_sentence_label.setGeometry(QtCore.QRect(440, 280, 1056, 67))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(30)
        self.second_sentence_label.setFont(font)
        self.second_sentence_label.setStyleSheet("color : #FFF;\n"
"border-color : #FFF;\n"
"background : transparent;")
        self.second_sentence_label.setObjectName("second_sentence_label")
        self.name_label = QtWidgets.QLabel(part_1_register_page)
        self.name_label.setGeometry(QtCore.QRect(704, 395, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        self.name_label.setFont(font)
        self.name_label.setStyleSheet("color : white;\n"
"background : transparent;")
        self.name_label.setObjectName("name_label")
        self.email_label = QtWidgets.QLabel(part_1_register_page)
        self.email_label.setGeometry(QtCore.QRect(704, 547, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        self.email_label.setFont(font)
        self.email_label.setStyleSheet("color : white;\n"
"background : transparent;")
        self.email_label.setObjectName("email_label")
        self.password_label = QtWidgets.QLabel(part_1_register_page)
        self.password_label.setGeometry(QtCore.QRect(704, 699, 193, 40))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet("color : white;\n"
"background : transparent;")
        self.password_label.setObjectName("password_label")
        
        self.next_Button = QtWidgets.QPushButton(part_1_register_page)
        self.next_Button.setGeometry(QtCore.QRect(1389, 925, 347, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(22)
        self.next_Button.setFont(font)
        self.next_Button.setCursor(QtCore.Qt.PointingHandCursor)
        self.next_Button.setStyleSheet("color : white;\n"
"background : #1347EC;\n"
"border-radius : 30px;\n"
"border : 2.5px solid white;")
        self.next_Button.setObjectName("next_Button")
        self.next_Button.clicked.connect(self.next_page)
        self.name_lineEdit = QtWidgets.QLineEdit(part_1_register_page)
        self.name_lineEdit.setText(" ")
        # self.name = self.name_lineEdit.text().__str__()
        self.name_lineEdit.setGeometry(QtCore.QRect(704, 458, 535, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        self.name_lineEdit.setFont(font)
        self.name_lineEdit.setStyleSheet("background : white;\n"
"color : black;\n"
"border-radius : 15px;")
        self.name_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.email_lineEdit = QtWidgets.QLineEdit(part_1_register_page)
        self.email_lineEdit.setText(" ")
        # self.email = self.email_lineEdit.text().__str__()
        self.email_lineEdit.setGeometry(QtCore.QRect(704, 610, 535, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        self.email_lineEdit.setFont(font)
        self.email_lineEdit.setStyleSheet("background : white;\n"
"color : black;\n"
"border-radius : 15px;")
        self.email_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.password_lineEdit = QtWidgets.QLineEdit(part_1_register_page)
        self.password_lineEdit.setText(" ")
        # self.password = self.password_lineEdit.text().__str__()
        self.password_lineEdit.setGeometry(QtCore.QRect(704, 762, 535, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setStyleSheet("background : white;\n"
"color : black;\n"
"border-radius : 15px;")
        self.password_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.password_lineEdit.setObjectName("password_lineEdit")

        self.retranslateUi(part_1_register_page)
        QtCore.QMetaObject.connectSlotsByName(part_1_register_page)

    def retranslateUi(self, part_1_register_page):
        part_1_register_page.setWindowTitle(QtWidgets.QApplication.translate("part_1_register_page", "Form", None, -1))
        self.register_label.setText(QtWidgets.QApplication.translate("part_1_register_page", "Register", None, -1))
        self.first_sentence_label.setText(QtWidgets.QApplication.translate("part_1_register_page", "Look like you are the first one here, create an account", None, -1))
        self.second_sentence_label.setText(QtWidgets.QApplication.translate("part_1_register_page", "below to start using our health track application", None, -1))
        self.name_label.setText(QtWidgets.QApplication.translate("part_1_register_page", "NAME", None, -1))
        self.email_label.setText(QtWidgets.QApplication.translate("part_1_register_page", "EMAIL", None, -1))
        self.password_label.setText(QtWidgets.QApplication.translate("part_1_register_page", "PASSWORD", None, -1))
        self.next_Button.setText(QtWidgets.QApplication.translate("part_1_register_page", "Next", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    part_1_register_page = QtWidgets.QWidget()
    ui = Ui_part_1_register_page()
    ui.setupUi(part_1_register_page)
    part_1_register_page.show()
    sys.exit(app.exec_())

