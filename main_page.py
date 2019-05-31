from PySide2 import QtCore, QtGui, QtWidgets
from login import Login

class Ui_main_page(object):
    def __init__(self, user, token):
        self.user = user
        self.token = token

    def change_page(self, page):
        # i = random.randint(1, 5)
        # self.quote_image.setStyleSheet("border-radius : 0px; background-image: url(./image/quote_" + "1" + ".jpg); border : None; background-size: cover;")
        
        if(page == 0):
                print('Dash_board')
        else:
                self.birth_dateEdit.setDate(QtCore.QDate(1999, 12, 28))
                #SET_DEFAULT_EMAIL
                self.email_lineEdit.setText(self.user.get_user_email())
                #SET_DEFAULT_NAME
                self.name_lineEdit.setText(self.user.get_user_name())
                #SET_DEFAULT_PASSWORD
                self.password_lineEdit.setText("")
                #SET_DEFAULT_WEIGHT
                self.weight_lineEdit.setText(str(self.user.get_user_weight()))
                #SET_DEFAULT_HEIGHT
                self.height_lineEdit.setText(str(self.user.get_user_height()))
                
    
    def save(self):
        self.get_update_data(self.name_lineEdit.text(), 
        self.email_lineEdit.text(), self.password_lineEdit.text(), 
        self.birth_dateEdit.date().toString("yyyy-MM-dd"), 
        self.weight_lineEdit.text(), 
        self.height_lineEdit.text(),
        str(self.sex_comboBox.currentText()))

    def get_update_data(self, name, email, password, birthdate, weight, height, gender):
        print("Name : " + str(name) + " , Email : " + str(email) + " , Password : " + str(password) + " , Birthdate : " + str(birthdate) + " , Weight : " + str(weight) + " , Height : " + str(height) + " , Gender : " + str(gender))
        self.user.user_change_profile(email, password, name, weight, height, gender)
        self.user.set_user_birthdate(name, birthdate)
        self.user.set_user_gender(name, gender)

    def setupUi(self, main_page):
        main_page.setObjectName("main_page")
        main_page.resize(1600, 900)
        main_page.setMinimumSize(QtCore.QSize(1600, 900))
        main_page.setMaximumSize(QtCore.QSize(1600, 900))
        self.tabWidget = QtWidgets.QTabWidget(main_page)
        self.tabWidget.currentChanged.connect(self.change_page)
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
        # self.tabWidget.setCurrentIndex(0)
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

        #QUOTE_WIDGETS
        self.quote_widgets = QtWidgets.QWidget(self.dash_board)
        self.quote_widgets.setGeometry(QtCore.QRect(830, 430, 711, 371))
        self.quote_widgets.setStyleSheet("border : 2px solid black;\n"
"border-radius : 15px;\n"
"background : white;")
        self.quote_widgets.setObjectName("quote_widgets")
        self.quote_image = QtWidgets.QLabel(self.quote_widgets)
        self.quote_image.setGeometry(QtCore.QRect(150, 35, 450, 300))
        self.quote_image.setStyleSheet("border-radius : 0px;\n"
"background-image: url(./image/quote_1.jpg);\n"
"border : None;\n"
"background-size: cover;")
        self.quote_image.setText("")
        self.quote_image.setObjectName("quote_image")

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
        self.profile_picture.setGeometry(QtCore.QRect(50, 160, 51, 51))
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
        
        #NAME
        self.name_lineEdit = QtWidgets.QLineEdit(self.profile_widget_1)

        
        self.name_lineEdit.setGeometry(QtCore.QRect(140, 170, 380, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
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

        #EMAIL
        self.email_lineEdit = QtWidgets.QLineEdit(self.profile_widget_1)
        self.email_lineEdit.setGeometry(QtCore.QRect(140, 310, 380, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        self.email_lineEdit.setFont(font)

        
        
        self.email_lineEdit.setStyleSheet("border-radius : 0px;\n"
"border-style : groove;\n"
"border-width : 1.5px;\n"
"border-color : rgb(128,128,128);")
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.email_picture = QtWidgets.QLabel(self.profile_widget_1)
        self.email_picture.setGeometry(QtCore.QRect(50, 310, 51, 51))
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

        #PASSWORD
        self.password_lineEdit = QtWidgets.QLineEdit(self.profile_widget_1)
        

        self.password_lineEdit.setGeometry(QtCore.QRect(140, 450, 380, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setStyleSheet("border-radius : 0px;\n"
"border-style : groove;\n"
"border-width : 1.5px;\n"
"border-color : rgb(128,128,128);")
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.password_picture = QtWidgets.QLabel(self.profile_widget_1)
        self.password_picture.setGeometry(QtCore.QRect(50, 440, 61, 51))
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

        self.weight_label = QtWidgets.QLabel(self.profile_widget_2)
        self.weight_label.setGeometry(QtCore.QRect(140, 260, 101, 31))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(20)
        self.weight_label.setFont(font)
        self.weight_label.setStyleSheet("border : none;\n"
"")
        self.weight_label.setObjectName("weight_label")

         #WEIGHT
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
        self.weight_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.weight_lineEdit.setObjectName("weight_lineEdit")
        self.birth_date_picture = QtWidgets.QLabel(self.profile_widget_2)
        self.birth_date_picture.setGeometry(QtCore.QRect(50, 150, 51, 51))
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

        #HEIGHT
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
        self.height_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
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
        self.weight_picture_2 = QtWidgets.QLabel(self.profile_widget_2)
        self.weight_picture_2.setGeometry(QtCore.QRect(50, 430, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Font Awesome 5 Free Regular")
        font.setPointSize(30)
        self.weight_picture_2.setFont(font)
        self.weight_picture_2.setStyleSheet("border : none;")
        self.weight_picture_2.setObjectName("weight_picture_2")

        #SAVE_BUTTON
        self.save_Button = QtWidgets.QPushButton(self.profile_widget_2)
        self.save_Button.clicked.connect(self.save)
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

        #BIRTH_DATE
        self.birth_dateEdit = QtWidgets.QDateEdit(self.profile_widget_2)

        #SET_DEFAULT_BIRTH_DATE (Format : yyy , mm, dd)

        self.birth_dateEdit.setGeometry(QtCore.QRect(139, 160, 301, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.birth_dateEdit.setFont(font)
        self.birth_dateEdit.setStyleSheet("border : black;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius : 0px;\n"
"border-color : rgb(128,128,128);")
        self.birth_dateEdit.setCalendarPopup(True)
        self.birth_dateEdit.setObjectName("birth_dateEdit")

        #GENDER
        self.sex_comboBox = QtWidgets.QComboBox(self.profile_widget_2)
        
        #SET_DEFAULT_GENDER (MALE == 0)
        self.sex_comboBox.setCurrentIndex(0)
        self.sex_comboBox.addItem("male")
        self.sex_comboBox.addItem("female")
        self.sex_comboBox.addItem("-")
        self.sex_comboBox.setGeometry(QtCore.QRect(140, 450, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        self.sex_comboBox.setFont(font)
        self.sex_comboBox.setStyleSheet("border : black;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius : 0px;\n"
"border-color : rgb(128,128,128);")
        self.sex_comboBox.setEditable(True)
        self.sex_comboBox.setObjectName("sex_comboBox")
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
        self.weight_lineEdit.setInputMask(QtWidgets.QApplication.translate("main_page", "999", None, -1))
        self.birth_date_picture.setText(QtWidgets.QApplication.translate("main_page", "", None, -1))
        self.weight_picture.setText(QtWidgets.QApplication.translate("main_page", "", None, -1))
        self.height_label.setText(QtWidgets.QApplication.translate("main_page", "Height", None, -1))
        self.height_lineEdit.setInputMask(QtWidgets.QApplication.translate("main_page", "999", None, -1))
        self.height_picture.setText(QtWidgets.QApplication.translate("main_page", "", None, -1))
        self.gender_label.setText(QtWidgets.QApplication.translate("main_page", "Gender", None, -1))
        self.weight_picture_2.setText(QtWidgets.QApplication.translate("main_page", "", None, -1))
        self.save_Button.setText(QtWidgets.QApplication.translate("main_page", "Save", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.profile), QtWidgets.QApplication.translate("main_page", "PROFILE", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.user_name), QtWidgets.QApplication.translate("main_page", "                                                                                                        " + self.name_lineEdit.text(), None, -1))

# from mplwidget import MplWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_page = QtWidgets.QWidget()
    ui = Ui_main_page()
    ui.setupUi(main_page)
    main_page.show()
    sys.exit(app.exec_())