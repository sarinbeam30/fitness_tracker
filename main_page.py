# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_page.ui',
# licensing of 'main_page.ui' applies.
#
# Created: Thu May 30 16:41:09 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_main_page(object):
    def setupUi(self, main_page):
        main_page.setObjectName("main_page")
        main_page.resize(1600, 900)
        main_page.setMinimumSize(QtCore.QSize(1600, 900))
        main_page.setMaximumSize(QtCore.QSize(1600, 900))
        self.tabWidget = QtWidgets.QTabWidget(main_page)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1600, 900))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(20)
        font.setUnderline(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtCore.Qt.ArrowCursor)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setStyleSheet("QTabWidget::tab-bar {\n"
"   border: 1px solid #3F3838;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"  background: #3F3838;\n"
"  color: white;\n"
"  padding: 10px;\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"  background: #3F3838;\n"
"  color : #FFA800;\n"
" }\n"
"\n"
"")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(60, 60))
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setObjectName("tabWidget")
        self.dash_board = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(35)
        self.dash_board.setFont(font)
        self.dash_board.setStyleSheet("background : qlineargradient(x2:1, y2:1, x0:1, y0:1,\n"
"                stop:0 rgb(255,255,224), stop: 0.4 rgba(255,251,219, 40), stop:1 rgb(235,119,20));")
        self.dash_board.setObjectName("dash_board")
        self.heart_rate_widgets = QtWidgets.QWidget(self.dash_board)
        self.heart_rate_widgets.setGeometry(QtCore.QRect(60, 30, 711, 371))
        self.heart_rate_widgets.setStyleSheet("border : 2px solid black;\n"
"border-radius : 15px;\n"
"background : white;")
        self.heart_rate_widgets.setObjectName("heart_rate_widgets")
        # self.graph_widget = MplWidget(self.heart_rate_widgets)
        # self.graph_widget.setGeometry(QtCore.QRect(20, 20, 671, 291))
        # self.graph_widget.setObjectName("graph_widget")
        self.pushButton_1day = QtWidgets.QPushButton(self.heart_rate_widgets)
        self.pushButton_1day.setGeometry(QtCore.QRect(30, 320, 93, 28))
        self.pushButton_1day.setObjectName("pushButton_1day")
        self.pushButton_7days = QtWidgets.QPushButton(self.heart_rate_widgets)
        self.pushButton_7days.setGeometry(QtCore.QRect(140, 320, 93, 28))
        self.pushButton_7days.setObjectName("pushButton_7days")
        self.pushButton_1month = QtWidgets.QPushButton(self.heart_rate_widgets)
        self.pushButton_1month.setGeometry(QtCore.QRect(250, 320, 93, 28))
        self.pushButton_1month.setObjectName("pushButton_1month")
        self.pushButton_3month = QtWidgets.QPushButton(self.heart_rate_widgets)
        self.pushButton_3month.setGeometry(QtCore.QRect(360, 320, 93, 28))
        self.pushButton_3month.setObjectName("pushButton_3month")
        self.pushButton_extend = QtWidgets.QPushButton(self.heart_rate_widgets)
        self.pushButton_extend.setGeometry(QtCore.QRect(470, 320, 93, 28))
        self.pushButton_extend.setObjectName("pushButton_extend")
        self.steps_widgets = QtWidgets.QWidget(self.dash_board)
        self.steps_widgets.setGeometry(QtCore.QRect(830, 30, 711, 371))
        self.steps_widgets.setStyleSheet("border : 2px solid black;\n"
"border-radius : 15px;\n"
"background : white;")
        self.steps_widgets.setObjectName("steps_widgets")
        self.food_widgets = QtWidgets.QWidget(self.dash_board)
        self.food_widgets.setGeometry(QtCore.QRect(60, 430, 711, 371))
        self.food_widgets.setStyleSheet("border : 2px solid black;\n"
"border-radius : 15px;\n"
"background : white;")
        self.food_widgets.setObjectName("food_widgets")
        self.quote_widgets = QtWidgets.QWidget(self.dash_board)
        self.quote_widgets.setGeometry(QtCore.QRect(830, 430, 711, 371))
        self.quote_widgets.setStyleSheet("border : 2px solid black;\n"
"border-radius : 15px;\n"
"background : white;")
        self.quote_widgets.setObjectName("quote_widgets")
        self.tabWidget.addTab(self.dash_board, "")
        self.profile = QtWidgets.QWidget()
        self.profile.setStyleSheet("background : qlineargradient(x2:1, y2:1, x0:1, y0:1,\n"
"                stop:0 rgb(255,255,224), stop: 0.4 rgba(255,251,219, 40), stop:1 rgb(235,119,20));")
        self.profile.setObjectName("profile")
        self.profile_widget_1 = QtWidgets.QWidget(self.profile)
        self.profile_widget_1.setGeometry(QtCore.QRect(135, 80, 620, 600))
        self.profile_widget_1.setStyleSheet("border : 2px solid black;\n"
"border-radius : 15px;\n"
"background : white;")
        self.profile_widget_1.setObjectName("profile_widget_1")
        self.profile_information_label = QtWidgets.QLabel(self.profile_widget_1)
        self.profile_information_label.setGeometry(QtCore.QRect(40, 25, 321, 67))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(23)
        self.profile_information_label.setFont(font)
        self.profile_information_label.setStyleSheet("border : none;")
        self.profile_information_label.setObjectName("profile_information_label")
        self.profile_picture = QtWidgets.QLabel(self.profile_widget_1)
        self.profile_picture.setGeometry(QtCore.QRect(50, 150, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Font Awesome 5 Free Regular")
        font.setPointSize(30)
        self.profile_picture.setFont(font)
        self.profile_picture.setStyleSheet("border : none;")
        self.profile_picture.setObjectName("profile_picture")
        self.name_label = QtWidgets.QLabel(self.profile_widget_1)
        self.name_label.setGeometry(QtCore.QRect(140, 120, 81, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(20)
        self.name_label.setFont(font)
        self.name_label.setStyleSheet("border : none;\n"
"")
        self.name_label.setObjectName("name_label")
        self.name_lineEdit = QtWidgets.QLineEdit(self.profile_widget_1)
        self.name_lineEdit.setGeometry(QtCore.QRect(140, 170, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.name_lineEdit.setFont(font)
        self.name_lineEdit.setStyleSheet("border-radius : 0px;\n"
"border-style : groove;\n"
"border-width : 1.5px;\n"
"border-color : rgb(128,128,128);")
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.email_label = QtWidgets.QLabel(self.profile_widget_1)
        self.email_label.setGeometry(QtCore.QRect(140, 260, 81, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(20)
        self.email_label.setFont(font)
        self.email_label.setStyleSheet("border : none;\n"
"")
        self.email_label.setObjectName("email_label")
        self.email_lineEdit = QtWidgets.QLineEdit(self.profile_widget_1)
        self.email_lineEdit.setGeometry(QtCore.QRect(140, 310, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.email_lineEdit.setFont(font)
        self.email_lineEdit.setStyleSheet("border-radius : 0px;\n"
"border-style : groove;\n"
"border-width : 1.5px;\n"
"border-color : rgb(128,128,128);")
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.email_picture = QtWidgets.QLabel(self.profile_widget_1)
        self.email_picture.setGeometry(QtCore.QRect(50, 297, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Font Awesome 5 Free Regular")
        font.setPointSize(30)
        self.email_picture.setFont(font)
        self.email_picture.setStyleSheet("border : none;")
        self.email_picture.setObjectName("email_picture")
        self.password_label = QtWidgets.QLabel(self.profile_widget_1)
        self.password_label.setGeometry(QtCore.QRect(140, 400, 141, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(20)
        self.password_label.setFont(font)
        self.password_label.setStyleSheet("border : none;\n"
"")
        self.password_label.setObjectName("password_label")
        self.password_lineEdit = QtWidgets.QLineEdit(self.profile_widget_1)
        self.password_lineEdit.setGeometry(QtCore.QRect(140, 450, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setStyleSheet("border-radius : 0px;\n"
"border-style : groove;\n"
"border-width : 1.5px;\n"
"border-color : rgb(128,128,128);")
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.password_picture = QtWidgets.QLabel(self.profile_widget_1)
        self.password_picture.setGeometry(QtCore.QRect(50, 430, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Font Awesome 5 Free Regular")
        font.setPointSize(30)
        self.password_picture.setFont(font)
        self.password_picture.setStyleSheet("border : none;")
        self.password_picture.setObjectName("password_picture")
        self.profile_widget_2 = QtWidgets.QWidget(self.profile)
        self.profile_widget_2.setGeometry(QtCore.QRect(852, 80, 620, 600))
        self.profile_widget_2.setStyleSheet("border : 2px solid black;\n"
"border-radius : 15px;\n"
"background : white;")
        self.profile_widget_2.setObjectName("profile_widget_2")
        self.birth_date_label = QtWidgets.QLabel(self.profile_widget_2)
        self.birth_date_label.setGeometry(QtCore.QRect(140, 100, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(20)
        self.birth_date_label.setFont(font)
        self.birth_date_label.setStyleSheet("border : none;\n"
"")
        self.birth_date_label.setObjectName("birth_date_label")
        self.birth_date_lineEdit = QtWidgets.QLineEdit(self.profile_widget_2)
        self.birth_date_lineEdit.setGeometry(QtCore.QRect(140, 160, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.birth_date_lineEdit.setFont(font)
        self.birth_date_lineEdit.setStyleSheet("border-radius : 0px;\n"
"border-style : groove;\n"
"border-width : 1.5px;\n"
"border-color : rgb(128,128,128);")
        self.birth_date_lineEdit.setObjectName("birth_date_lineEdit")
        self.weight_label = QtWidgets.QLabel(self.profile_widget_2)
        self.weight_label.setGeometry(QtCore.QRect(140, 260, 101, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(20)
        self.weight_label.setFont(font)
        self.weight_label.setStyleSheet("border : none;\n"
"")
        self.weight_label.setObjectName("weight_label")
        self.weight_lineEdit = QtWidgets.QLineEdit(self.profile_widget_2)
        self.weight_lineEdit.setGeometry(QtCore.QRect(140, 310, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.weight_lineEdit.setFont(font)
        self.weight_lineEdit.setStyleSheet("border-radius : 0px;\n"
"border-style : groove;\n"
"border-width : 1.5px;\n"
"border-color : rgb(128,128,128);")
        self.weight_lineEdit.setObjectName("weight_lineEdit")
        self.birth_date_picture = QtWidgets.QLabel(self.profile_widget_2)
        self.birth_date_picture.setGeometry(QtCore.QRect(50, 137, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Font Awesome 5 Free Regular")
        font.setPointSize(30)
        self.birth_date_picture.setFont(font)
        self.birth_date_picture.setStyleSheet("border : none;")
        self.birth_date_picture.setObjectName("birth_date_picture")
        self.weight_picture = QtWidgets.QLabel(self.profile_widget_2)
        self.weight_picture.setGeometry(QtCore.QRect(50, 290, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Font Awesome 5 Free Regular")
        font.setPointSize(30)
        self.weight_picture.setFont(font)
        self.weight_picture.setStyleSheet("border : none;")
        self.weight_picture.setObjectName("weight_picture")
        self.height_label = QtWidgets.QLabel(self.profile_widget_2)
        self.height_label.setGeometry(QtCore.QRect(370, 260, 101, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(20)
        self.height_label.setFont(font)
        self.height_label.setStyleSheet("border : none;\n"
"")
        self.height_label.setObjectName("height_label")
        self.height_lineEdit = QtWidgets.QLineEdit(self.profile_widget_2)
        self.height_lineEdit.setGeometry(QtCore.QRect(370, 310, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.height_lineEdit.setFont(font)
        self.height_lineEdit.setStyleSheet("border-radius : 0px;\n"
"border-style : groove;\n"
"border-width : 1.5px;\n"
"border-color : rgb(128,128,128);")
        self.height_lineEdit.setObjectName("height_lineEdit")
        self.height_picture = QtWidgets.QLabel(self.profile_widget_2)
        self.height_picture.setGeometry(QtCore.QRect(310, 290, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Font Awesome 5 Free Regular")
        font.setPointSize(30)
        self.height_picture.setFont(font)
        self.height_picture.setStyleSheet("border : none;\n"
"background-image : url(\"./image/height_picture.png\");\n"
"")
        self.height_picture.setObjectName("height_picture")
        self.gender_label = QtWidgets.QLabel(self.profile_widget_2)
        self.gender_label.setGeometry(QtCore.QRect(140, 400, 101, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(20)
        self.gender_label.setFont(font)
        self.gender_label.setStyleSheet("border : none;\n"
"")
        self.gender_label.setObjectName("gender_label")
        self.gender_lineEdit = QtWidgets.QLineEdit(self.profile_widget_2)
        self.gender_lineEdit.setGeometry(QtCore.QRect(140, 450, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(18)
        self.gender_lineEdit.setFont(font)
        self.gender_lineEdit.setStyleSheet("border-radius : 0px;\n"
"border-style : groove;\n"
"border-width : 1.5px;\n"
"border-color : rgb(128,128,128);")
        self.gender_lineEdit.setObjectName("gender_lineEdit")
        self.weight_picture_2 = QtWidgets.QLabel(self.profile_widget_2)
        self.weight_picture_2.setGeometry(QtCore.QRect(50, 430, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Font Awesome 5 Free Regular")
        font.setPointSize(30)
        self.weight_picture_2.setFont(font)
        self.weight_picture_2.setStyleSheet("border : none;")
        self.weight_picture_2.setObjectName("weight_picture_2")
        self.save_Button = QtWidgets.QPushButton(self.profile_widget_2)
        self.save_Button.setGeometry(QtCore.QRect(450, 519, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(18)
        self.save_Button.setFont(font)
        self.save_Button.setCursor(QtCore.Qt.PointingHandCursor)
        self.save_Button.setStyleSheet("color : white;\n"
"background : #1347EC;\n"
"border-radius : 20px;\n"
"")
        self.save_Button.setObjectName("save_Button")
        self.tabWidget.addTab(self.profile, "")
        self.user_name = QtWidgets.QWidget()
        self.user_name.setObjectName("user_name")
        self.tabWidget.addTab(self.user_name, "")

        self.retranslateUi(main_page)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_page)

    def retranslateUi(self, main_page):
        main_page.setWindowTitle(QtWidgets.QApplication.translate("main_page", "Form", None, -1))
        self.pushButton_1day.setText(QtWidgets.QApplication.translate("main_page", "1 day", None, -1))
        self.pushButton_7days.setText(QtWidgets.QApplication.translate("main_page", "7 days", None, -1))
        self.pushButton_1month.setText(QtWidgets.QApplication.translate("main_page", "1 month", None, -1))
        self.pushButton_3month.setText(QtWidgets.QApplication.translate("main_page", "3 month", None, -1))
        self.pushButton_extend.setText(QtWidgets.QApplication.translate("main_page", "EXTEND", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dash_board), QtWidgets.QApplication.translate("main_page", "DASHBOARD     ", None, -1))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.dash_board), QtWidgets.QApplication.translate("main_page", "Your dashboard", None, -1))
        self.profile_information_label.setText(QtWidgets.QApplication.translate("main_page", "Profile Information", None, -1))
        self.profile_picture.setText(QtWidgets.QApplication.translate("main_page", "", None, -1))
        self.name_label.setText(QtWidgets.QApplication.translate("main_page", "Name", None, -1))
        self.email_label.setText(QtWidgets.QApplication.translate("main_page", "Email", None, -1))
        self.email_picture.setText(QtWidgets.QApplication.translate("main_page", "", None, -1))
        self.password_label.setText(QtWidgets.QApplication.translate("main_page", "Password", None, -1))
        self.password_picture.setText(QtWidgets.QApplication.translate("main_page", "", None, -1))
        self.birth_date_label.setText(QtWidgets.QApplication.translate("main_page", "Birth-date", None, -1))
        self.weight_label.setText(QtWidgets.QApplication.translate("main_page", "Weight", None, -1))
        self.birth_date_picture.setText(QtWidgets.QApplication.translate("main_page", "", None, -1))
        self.weight_picture.setText(QtWidgets.QApplication.translate("main_page", "", None, -1))
        self.height_label.setText(QtWidgets.QApplication.translate("main_page", "Height", None, -1))
        self.height_picture.setText(QtWidgets.QApplication.translate("main_page", "", None, -1))
        self.gender_label.setText(QtWidgets.QApplication.translate("main_page", "Gender", None, -1))
        self.weight_picture_2.setText(QtWidgets.QApplication.translate("main_page", "", None, -1))
        self.save_Button.setText(QtWidgets.QApplication.translate("main_page", "Save", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.profile), QtWidgets.QApplication.translate("main_page", "PROFILE", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.user_name), QtWidgets.QApplication.translate("main_page", "                                                                                                        Sarin Wanichwasin", None, -1))

# from mplwidget import MplWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_page = QtWidgets.QWidget()
    ui = Ui_main_page()
    ui.setupUi(main_page)
    main_page.show()
    sys.exit(app.exec_())

