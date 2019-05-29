# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'part_2_register_page.ui',
# licensing of 'part_2_register_page.ui' applies.
#
# Created: Wed May 29 14:33:36 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from main_page import Ui_main_page
from register import Register

class Ui_part_2_register_page(object):

    def __init__(self):
        self.register = None

    def show_error_dialog(self):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setIcon(QtWidgets.QMessageBox.Critical)
        self.msg.setText  (" !!! -- Error -- !!! ")
        self.msg.setInformativeText("You forgot to input email or password or both email and password")
        self.msg.setWindowTitle("Error")
        self.msg.show()

    def main_page(self):
        self.main_page = QtWidgets.QWidget()
        self.ui = Ui_main_page()
        self.ui.setupUi(self.main_page)
        part_2_register_page.hide()
        self.main_page.show()

    def next_page(self):
        weight = self.weight_lineEdit.text()
        height = self.height_lineEdit.text()
        sex = str(self.sex_comboBox.currentText())
        birthdate = self.birthdate_dateEdit.date().toString('dd-MMM-yyyy')

        if(weight == " " or height == " "):
                print("Invalid input")
                self.show_error_dialog
        else:
                self.register = Register()
                self.register.set_weight(weight)
                self.register.set_height(height)
                self.register.set_sex(sex)
                self.register.set_birthdate(birthdate)
                self.main_page()            

    def setupUi(self, part_2_register_page):
        part_2_register_page.setObjectName("part_2_register_page")
        part_2_register_page.resize(1920, 1080)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(part_2_register_page.sizePolicy().hasHeightForWidth())
        part_2_register_page.setSizePolicy(sizePolicy)
        part_2_register_page.setStyleSheet("background-image: url(./image/black_register_wallpaper.jpg);\n"
"\n"
"background-size: contain;\n"
"background-repeat: no-repeat;\n"
"\n"
"opacity : 0.5;\n"
"")
        self.register_label = QtWidgets.QLabel(part_2_register_page)
        self.register_label.setGeometry(QtCore.QRect(711, 115, 500, 78))
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
        self.first_sentence_label = QtWidgets.QLabel(part_2_register_page)
        self.first_sentence_label.setGeometry(QtCore.QRect(356, 210, 1208, 67))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(30)
        self.first_sentence_label.setFont(font)
        self.first_sentence_label.setStyleSheet("color : #FFF;\n"
"border-color : #FFF;\n"
"background : transparent;")
        self.first_sentence_label.setObjectName("first_sentence_label")
        self.second_sentence_label = QtWidgets.QLabel(part_2_register_page)
        self.second_sentence_label.setGeometry(QtCore.QRect(502, 280, 1056, 67))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(30)
        self.second_sentence_label.setFont(font)
        self.second_sentence_label.setStyleSheet("color : #FFF;\n"
"border-color : #FFF;\n"
"background : transparent;")
        self.second_sentence_label.setObjectName("second_sentence_label")
        self.weight_label = QtWidgets.QLabel(part_2_register_page)
        self.weight_label.setGeometry(QtCore.QRect(704, 445, 135, 40))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        self.weight_label.setFont(font)
        self.weight_label.setStyleSheet("color : white;\n"
"background : transparent;")
        self.weight_label.setObjectName("weight_label")
        self.height_label = QtWidgets.QLabel(part_2_register_page)
        self.height_label.setGeometry(QtCore.QRect(952, 445, 135, 40))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        self.height_label.setFont(font)
        self.height_label.setStyleSheet("color : white;\n"
"background : transparent;")
        self.height_label.setObjectName("height_label")
        self.sex_label = QtWidgets.QLabel(part_2_register_page)
        self.sex_label.setGeometry(QtCore.QRect(704, 597, 65, 40))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        self.sex_label.setFont(font)
        self.sex_label.setStyleSheet("color : white;\n"
"background : transparent;")
        self.sex_label.setObjectName("sex_label")
        self.sex_comboBox = QtWidgets.QComboBox(part_2_register_page)
        self.sex_comboBox.setGeometry(QtCore.QRect(710, 650, 118, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(18)
        self.sex_comboBox.setFont(font)
        self.sex_comboBox.setMouseTracking(True)
        self.sex_comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sex_comboBox.setStyleSheet("background : white;\n"
"color : black;\n"
"border-radius : 17px solid white;\n"
"\n"
"QComboBox { background-color: white; color : black;}")
        self.sex_comboBox.setMaxVisibleItems(3)

        self.sex_comboBox.setCurrentIndex(1)

        self.sex_comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.sex_comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.sex_comboBox.setObjectName("sex_comboBox")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("."), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sex_comboBox.addItem(icon, "")
        self.sex_comboBox.addItem("")
        self.sex_comboBox.addItem("")
        self.sex_label_2 = QtWidgets.QLabel(part_2_register_page)
        self.sex_label_2.setGeometry(QtCore.QRect(704, 740, 190, 40))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        self.sex_label_2.setFont(font)
        self.sex_label_2.setStyleSheet("color : white;\n"
"background : transparent;")
        self.sex_label_2.setObjectName("sex_label_2")
        self.birthdate_dateEdit = QtWidgets.QDateEdit(part_2_register_page)
        self.birthdate_dateEdit.setGeometry(QtCore.QRect(710, 790, 225, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(18)
        self.birthdate_dateEdit.setFont(font)
        self.birthdate_dateEdit.setCursor(QtCore.Qt.PointingHandCursor)
        self.birthdate_dateEdit.setCalendarPopup(True)
        self.birthdate_dateEdit.setObjectName("birthdate_dateEdit")
        self.weight_lineEdit = QtWidgets.QLineEdit(part_2_register_page)
        self.weight_lineEdit.setGeometry(QtCore.QRect(704, 508, 160, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        self.weight_lineEdit.setFont(font)
        self.weight_lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.weight_lineEdit.setStyleSheet("background: white;\n"
"color : black;\n"
"border-radius : 17px solid white;\n"
"")
        self.weight_lineEdit.setText(" ")
        self.weight_lineEdit.setMaxLength(3)
        self.weight_lineEdit.setFrame(True)
        self.weight_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.weight_lineEdit.setObjectName("weight_lineEdit")
        self.height_lineEdit = QtWidgets.QLineEdit(part_2_register_page)
        self.height_lineEdit.setGeometry(QtCore.QRect(952, 508, 160, 50))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        self.height_lineEdit.setFont(font)
        self.height_lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.height_lineEdit.setStyleSheet("background: white;\n"
"color : black;\n"
"border-radius : 17px solid white;\n"
"")
        self.height_lineEdit.setText(" ")
        self.height_lineEdit.setMaxLength(3)
        self.height_lineEdit.setFrame(True)
        self.height_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.height_lineEdit.setObjectName("height_lineEdit")
        self.next_Button = QtWidgets.QPushButton(part_2_register_page)
        self.next_Button.clicked.connect(self.next_page)
        self.next_Button.setGeometry(QtCore.QRect(1490, 900, 347, 61))
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

        self.retranslateUi(part_2_register_page)
        QtCore.QMetaObject.connectSlotsByName(part_2_register_page)

    def retranslateUi(self, part_2_register_page):
        part_2_register_page.setWindowTitle(QtWidgets.QApplication.translate("part_2_register_page", "Form", None, -1))
        self.register_label.setText(QtWidgets.QApplication.translate("part_2_register_page", "Register [continue]", None, -1))
        self.first_sentence_label.setText(QtWidgets.QApplication.translate("part_2_register_page", "Look like you are the first one here, create an account", None, -1))
        self.second_sentence_label.setText(QtWidgets.QApplication.translate("part_2_register_page", "below to start using our health track application", None, -1))
        self.weight_label.setText(QtWidgets.QApplication.translate("part_2_register_page", "WEIGHT", None, -1))
        self.height_label.setText(QtWidgets.QApplication.translate("part_2_register_page", "HEIGHT", None, -1))
        self.sex_label.setText(QtWidgets.QApplication.translate("part_2_register_page", "SEX", None, -1))
        self.sex_comboBox.setItemText(0, QtWidgets.QApplication.translate("part_2_register_page", "Male", None, -1))
        self.sex_comboBox.setItemText(1, QtWidgets.QApplication.translate("part_2_register_page", "Female", None, -1))
        self.sex_comboBox.setItemText(2, QtWidgets.QApplication.translate("part_2_register_page", "Other", None, -1))
        self.sex_label_2.setText(QtWidgets.QApplication.translate("part_2_register_page", "BIRTHDATE", None, -1))
        self.birthdate_dateEdit.setDisplayFormat(QtWidgets.QApplication.translate("part_2_register_page", "dd-MMM-yyyy", None, -1))
        self.weight_lineEdit.setInputMask(QtWidgets.QApplication.translate("part_2_register_page", "999", None, -1))
        self.height_lineEdit.setInputMask(QtWidgets.QApplication.translate("part_2_register_page", "999", None, -1))
        self.next_Button.setText(QtWidgets.QApplication.translate("part_2_register_page", "Next", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    part_2_register_page = QtWidgets.QWidget()
    ui = Ui_part_2_register_page()
    ui.setupUi(part_2_register_page)
    part_2_register_page.show()
    sys.exit(app.exec_())

