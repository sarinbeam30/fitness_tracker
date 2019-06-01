
from PySide2.QtWidgets import*
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import *
from PySide2.QtGui import *
import fitbit
import gather_keys_oauth2 as Oauth2
import datetime
import numpy as np
import ProgressWidget as pt
import matplotlib.font_manager as font_manager
import MplWidget as Mpl
import math
import random
from login import Login
from nutrition import Nutrition

# class PassUser()

# ------------------ MainWidget ------------------
class MainWidget(QWidget):
    def __init__(self, user, parent = None):
        self.user = user
        self.token = self.user.user_login()
        
        QWidget.__init__(self, parent=None)
        
        self.USER_ID = '22DG4C'
        self.CLIENT_SECRET = '940862ba343ec9ed386b999e689560d4'
        self.yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
        self.today = str(datetime.datetime.now().strftime("%Y%m%d"))
        self.autenticate()
        self.pullData()    
        
        self.stage = "" #graph state
        # font_path = ''
        
        # self.font_prop = font_manager.FontProperties()
        
        #main page
        designer_file = QFile("main_page2.ui")
        designer_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        loader.registerCustomWidget(Mpl.MplWidget)
        loader.registerCustomWidget(pt.ProgressWidget)
        self.ui = loader.load(designer_file, self)
        designer_file.close()

        self.ui.label_2.setPixmap(QPixmap("image/food2.png"))
        self.ui.label_5.setPixmap(QPixmap("image/water4crop.png"))

        self.ui.profile_picture_3.setPixmap(QPixmap("image/profile_picture.png"))
        self.ui.email_picture_3.setPixmap(QPixmap("image/email_picture.png"))
        self.ui.password_picture_3.setPixmap(QPixmap("image/password_picture.png"))
        self.ui.birth_date_picture_3.setPixmap(QPixmap("image/date_picture.png"))
        self.ui.weight_picture_5.setPixmap(QPixmap("image/weight_picture.png"))
        self.ui.height_picture_3.setPixmap(QPixmap("image/height_picture.svg"))
        self.ui.weight_picture_6.setPixmap(QPixmap("image/gender_picture.png"))
        self.ui.setWindowTitle("Fitness Tracker")


        self.update_graph1day()
        self.ui.pushButton_1day.clicked.connect(self.update_graph1day)
        self.ui.pushButton_7days.clicked.connect(self.update_graph1week)
        self.ui.pushButton_1month.clicked.connect(self.update_graph1month)
        self.ui.pushButton_3month.clicked.connect(self.update_graph3month)
        self.ui.pushButton_extend.clicked.connect(self.extend_graph)
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.ui)
        self.setLayout(grid_layout)

        #food data
        self.food_log = {}
        self.food_gain = 0
        self.food_max  = 2000
        self.ui.label_cal_input.setText(str(self.food_gain) + " : cals in")
        self.ui.label_cal_left.setText(str(self.food_max) + " : cals left")
        self.ui.pushButton_add_food.clicked.connect(self.add_food)
        self.ui.pushButton_food_log.clicked.connect(self.show_food_log)

        #water data
        self.water_gain = 0
        self.water_max  = 2000
        self.ui.label_water_in.setText(str(self.water_gain) + " : ml")
        self.ui.label_water_left.setText(str(self.water_max) + " : ml left")
        self.ui.pushButton_add_water.clicked.connect(self.add_water)

        #goal data
        self.goal_step = self.user.get_user_goal()
        self.step_gain = self.step_count
        self.update_goal_graph()
        self.ui.pushButton_add_goal.clicked.connect(self.set_goal)

        #adjust
        self.ui.tabWidget.setCurrentIndex(0)
        # self.ui.user_name.setText(self.user.get_user_name())
        self.ui.tabWidget.currentChanged.connect(self.change_page)
        self.ui.name_lineEdit_3.setText("default_name")
        self.ui.email_lineEdit_3.setText("default_email")
        self.ui.password_lineEdit_3.setText("default_password")
        self.ui.weight_lineEdit_3.setText("999")
        self.ui.height_lineEdit_3.setText("999")
        self.ui.save_Button_3.clicked.connect(self.save)
        self.ui.save_Button_3.setStyleSheet("QPushButton:hover:!pressed {color : white;background : black; }  QPushButton { color : white; background-color :  #1347EC;}")
        self.ui.birth_dateEdit_3.setDate(QDate(1999, 12, 28))
        self.ui.sex_comboBox_3.setCurrentIndex(self.sex_number())
        self.ui.sex_comboBox_3.addItem("male")
        self.ui.sex_comboBox_3.addItem("female")
        self.ui.sex_comboBox_3.addItem("-")

        self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.user_name), QApplication.translate("main_page", "                                                                                                                                                                                  " + self.user.get_user_name(), None, -1))

    # def make_token(self):
        
    def sex_number(self):
        if self.user.get_user_sex() == 0:
            return int(0)
        elif self.user.get_user_sex() == 1:
            return int(1)
        elif self.user.get_user_sex() == 2:
            return int(2)
        else:
            return int(0)

    def save(self):
        self.get_update_data(self.ui.name_lineEdit_3.text(),
                             self.ui.email_lineEdit_3.text(),
                             self.ui.password_lineEdit_3.text(),
                             self.ui.birth_dateEdit_3.date().toString('dd-MM-yyyy'),
                             self.ui.weight_lineEdit_3.text(),
                             self.ui.height_lineEdit_3.text(),
                             str(self.ui.sex_comboBox_3.currentText()))

    def get_update_data(self, name, email, password, birthdate, weight, height, gender):
        # print("Name : " + str(name) + " , Email : " + str(email) + " , Password : " + str(password) + " , Birthdate : " + str(birthdate) + " , Weight : " + str(weight) + " , Height : " + str(height) + " , Gender : " + str(gender))
        self.user.user_change_profile(email, password, name, weight, height, gender)
        self.user.set_user_birthdate(name, birthdate)
        self.user.set_user_gender(name, gender)

        

    def change_page(self,page):
        i = random.randint(1, 5)
        self.ui.quote_image_3.setStyleSheet("border-radius : 0px; background-image: url(./image/quote_" + str(i) + ".jpg); border : None; background-size: cover;")
        if(page == 0):
               
                self.update_goal_graph()
        else:
                getDate = self.user.get_user_birthdate()
                self.ui.birth_dateEdit_3.setDate(QDate(int(getDate[0]), int(getDate[1]), int(getDate[2])))
                #SET_DEFAULT_EMAIL
                self.ui.email_lineEdit_3.setText(self.user.get_user_email())
                #SET_DEFAULT_NAME
                self.ui.name_lineEdit_3.setText(self.user.get_user_name())
                #SET_DEFAULT_PASSWORD
                self.ui.password_lineEdit_3.setText("")
                #SET_DEFAULT_WEIGHT
                self.ui.weight_lineEdit_3.setText(str(self.user.get_user_weight()))
                #SET_DEFAULT_HEIGHT
                self.ui.height_lineEdit_3.setText(str(self.user.get_user_height()))

    def autenticate(self):
        self.server = Oauth2.OAuth2Server(self.USER_ID, self.CLIENT_SECRET)      
        self.server.browser_authorize()
        ACCESS_TOKEN = str(self.server.fitbit.client.session.token['access_token'])
        REFRESH_TOKEN = str(self.server.fitbit.client.session.token['refresh_token'])
        self.auth2_client = fitbit.Fitbit(self.USER_ID, self.CLIENT_SECRET, oauth2=True, access_token= ACCESS_TOKEN, refresh_token= REFRESH_TOKEN)

    def pullData(self):
        self.data_1day = self.auth2_client.make_request("https://api.fitbit.com/1/user/-/activities/steps/date/today/1d.json")
        self.data_1week = self.auth2_client.time_series("activities/steps",period = "7d")
        self.data_1month = self.auth2_client.time_series("activities/steps",period = "1m")
        self.data_3month = self.auth2_client.time_series("activities/steps",period = "3m")

    def set_goal(self):
        if self.ui.lineEdit_add_goal.text() == "":
            dialog = QDialog(self)
            layout = QVBoxLayout()
            label = QLabel(self)
            result = "ERROR: empty input"
            label.setText(result)
            layout.addWidget(label)
            dialog.setWindowTitle("ERROR")
            dialog.setLayout(layout)
            dialog.resize(150,100)
            dialog.setMinimumSize(150,100)
            dialog.show()
        else:
            self.goal_step = float(self.ui.lineEdit_add_goal.text())
            self.user.set_user_goal(self.user.get_user_name(),self.goal_step)
            self.update_goal_graph()
            bar_x = ('Current : km', 'Goal : km')
            data= [(self.step_gain * 0.762)/ 1000,self.goal_step]
            self.ui.progress_widget.canvas.axes.clear()
            self.ui.progress_widget.canvas.axes.bar(bar_x, data,color='green')
            self.ui.progress_widget.canvas.axes.set_title('tempo')

            
    def update_goal_graph(self):
        bar_x = ('Current : km', 'Goal : km')
        data= [(self.step_gain * 0.762)/ 1000,self.goal_step]
        self.ui.progress_widget.canvas.axes.clear()
        self.ui.progress_widget.canvas.axes.bar(bar_x, data,color='green')
        self.ui.progress_widget.canvas.axes.set_title('Goal : Day')
        self.ui.label_goal.setText("Goal :  " + str(self.goal_step) + " km.")
        if (self.step_gain * 0.762) / 1000 < 1:
            self.ui.label_current.setText("Current distance :  " + str(self.step_gain) + " m.")
        elif (self.step_gain * 0.762) / 1000 > 1:
            self.ui.label_current.setText("Current distance :  " + str(self.step_gain / 1000) + " km.")
        self.ui.label_cal_burn.setText("Calrorie burned : " + "%.2f" % (((self.step_gain * 0.762) / 1000) * 54) + " cal.")
        self.ui.progress_widget.canvas.draw()
    def update_graph1day(self):
        step_hr = []
        time_all = []
        temp_step = 0
        index = 0
        total = 0
        self.stage = "1day"
        fit_statsHR = self.data_1day
        for i in fit_statsHR["activities-steps-intraday"]["dataset"]:
            time = i.get("time")
            if time[3:5] != "00":
                temp = int(i.get("value"))
                temp_step += temp
                total += temp
            if time[3:5] == "59":
                temp = int(i.get("value"))
                step_hr.append(temp_step + temp)
                time_all.append(str(index)+ ":00")
                index += 1
                total += temp
                temp_step = 0
        self.step_count = total
        self.ui.graph_widget.canvas.axes.clear() 
        self.ui.graph_widget.canvas.axes.plot(time_all, step_hr)
        for label in (self.ui.graph_widget.canvas.axes.get_xticklabels() + self.ui.graph_widget.canvas.axes.get_yticklabels()):
            # label.set_fontproperties(self.font_prop)
            label.set_fontsize(8)
        self.ui.graph_widget.canvas.axes.set_title('Your steps in one day')
        self.ui.graph_widget.canvas.draw()

    def update_graph1week(self):
        date = []
        steps = []
        self.stage = "1week"
        fit_statsHR = self.data_1week
        for i in fit_statsHR["activities-steps"]:
            temp = i.get("dateTime")
            temp2 = temp[8:10] + "/" + temp[5:7] + "/" + temp[2:4]
            date.append(temp2)
            steps.append(int(i.get("value")))
        self.ui.graph_widget.canvas.axes.clear() 
        self.ui.graph_widget.canvas.axes.plot(date, steps)
        for label in (self.ui.graph_widget.canvas.axes.get_xticklabels() + self.ui.graph_widget.canvas.axes.get_yticklabels()):
            # label.set_fontproperties(self.font_prop)
            label.set_fontsize(8)
        self.ui.graph_widget.canvas.axes.set_title('Your steps in one week')
        self.ui.graph_widget.canvas.draw()

    def update_graph1month(self):
        date = []
        steps = []
        self.stage = "1month"
        fit_statsHR = self.data_1month
        for i in fit_statsHR["activities-steps"]:
            temp = i.get("dateTime")
            temp2 = temp[8:10] + "/" + temp[5:7] + "/" + temp[2:4]
            date.append(temp2)
            steps.append(int(i.get("value")))
        self.ui.graph_widget.canvas.axes.clear() 
        self.ui.graph_widget.canvas.axes.plot(date, steps)
        for label in (self.ui.graph_widget.canvas.axes.get_xticklabels() + self.ui.graph_widget.canvas.axes.get_yticklabels()):
            # label.set_fontproperties(self.font_prop)
            label.set_fontsize(8)
        self.ui.graph_widget.canvas.axes.set_title('Your steps in one month')
        self.ui.graph_widget.canvas.draw()
        
    def update_graph3month(self):
        date = []
        steps = []
        count = 0
        temp_step = 0
        self.stage = "3month"
        fit_statsHR = self.data_3month
        for i in fit_statsHR["activities-steps"]:
            count += 1
            temp = i.get("dateTime")
            temp2 = temp[8:10] + "/" + temp[5:7] + "/" + temp[2:4]
            temp_step += int(i.get("value"))
            if count % 7 == 1:    
                date.append(temp2)
                steps.append(temp_step)
                temp_step = 0
        self.ui.graph_widget.canvas.axes.clear() 
        self.ui.graph_widget.canvas.axes.plot(date, steps)
        for label in (self.ui.graph_widget.canvas.axes.get_xticklabels() + self.ui.graph_widget.canvas.axes.get_yticklabels()):
            # label.set_fontproperties(self.font_prop)
            label.set_fontsize(8)
        self.ui.graph_widget.canvas.axes.set_title('Your steps in three month')
        self.ui.graph_widget.canvas.draw()

    def extend_graph(self):
        #popup page
        designer_file = QFile("popup2.ui")
        designer_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.popup = loader.load(designer_file, self)
        designer_file.close()
        self.popup.setWindowTitle("Extend-graph")
        if self.stage == "1day":
            step_hr = []
            time_all = []
            temp_step = 0
            index = 0
            total = 0
            fit_statsHR = self.data_1day
            for i in fit_statsHR["activities-steps-intraday"]["dataset"]:
                time = i.get("time")
                if time[3:5] != "00":
                    temp = int(i.get("value"))
                    temp_step += temp
                    total += temp
                if time[3:5] == "59":
                    temp = int(i.get("value"))
                    step_hr.append(temp_step + temp)
                    time_all.append(str(index)+ ":00")
                    index += 1
                    total += temp
                    temp_step = 0   
            self.popup.graph_widget.canvas.axes.clear()
            for label in (self.ui.graph_widget.canvas.axes.get_xticklabels() + self.ui.graph_widget.canvas.axes.get_yticklabels()):
                # label.set_fontproperties(self.font_prop)
                label.set_fontsize(10)
            self.popup.graph_widget.canvas.axes.plot(time_all, step_hr)
            self.popup.graph_widget.canvas.axes.set_title('daily')
            self.popup.graph_widget.canvas.draw()   
        elif self.stage == "1week":
            date = []
            steps = []
            fit_statsHR = self.data_1week
            for i in fit_statsHR["activities-steps"]:
                temp = i.get("dateTime")
                temp2 = temp[8:10] + "/" + temp[5:7] + "/" + temp[2:4]
                date.append(temp2)
                steps.append(int(i.get("value")))
            self.popup.graph_widget.canvas.axes.clear() 
            self.popup.graph_widget.canvas.axes.plot(date, steps)
            for label in (self.popup.graph_widget.canvas.axes.get_xticklabels() + self.popup.graph_widget.canvas.axes.get_yticklabels()):
                # label.set_fontproperties(self.font_prop)
                label.set_fontsize(11)
            self.popup.graph_widget.canvas.axes.set_title('daily')
            self.popup.graph_widget.canvas.draw()
        elif self.stage == "1month":
            date = []
            steps = []
            fit_statsHR = self.data_1month
            for i in fit_statsHR["activities-steps"]:
                temp = i.get("dateTime")
                temp2 = temp[8:10] + "/" + temp[5:7] + "/" + temp[2:4]
                date.append(temp2)
                steps.append(int(i.get("value")))
            self.popup.graph_widget.canvas.axes.clear() 
            self.popup.graph_widget.canvas.axes.plot(date, steps)
            for label in (self.popup.graph_widget.canvas.axes.get_xticklabels() + self.popup.graph_widget.canvas.axes.get_yticklabels()):
                # label.set_fontproperties(self.font_prop)
                label.set_fontsize(11)
            self.popup.graph_widget.canvas.axes.set_title('daily')
            self.popup.graph_widget.canvas.draw()
        elif self.stage == "3month":
            date = []
            steps = []
            count = 0
            temp_step = 0
            fit_statsHR = self.data_3month
            for i in fit_statsHR["activities-steps"]:
                count += 1
                temp = i.get("dateTime")
                temp2 = temp[8:10] + "/" + temp[5:7] + "/" + temp[2:4]
                temp_step += int(i.get("value"))
                if count % 7 == 1:    
                    date.append(temp2)
                    steps.append(temp_step)
                    temp_step = 0
            self.popup.graph_widget.canvas.axes.clear() 
            self.popup.graph_widget.canvas.axes.plot(date, steps)
            for label in (self.popup.graph_widget.canvas.axes.get_xticklabels() + self.popup.graph_widget.canvas.axes.get_yticklabels()):
                # label.set_fontproperties(self.font_prop)
                label.set_fontsize(11)
            self.popup.graph_widget.canvas.axes.set_title('daily')
            self.popup.graph_widget.canvas.draw()
        self.popup.show()

    def add_food(self):
        designer_file = QFile("cal_add.ui")
        designer_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.calUi = loader.load(designer_file, self)
        designer_file.close()
        self.calUi.setWindowTitle("Add Food")
        self.calUi.pushButton_add.clicked.connect(self.add_food_log)
        self.calUi.pushButton_cancel.clicked.connect(self.calUi.close)
        self.calUi.setFixedSize(self.calUi.size())
        self.calUi.show()
        
    def add_food_log(self):
        food_name = self.calUi.lineEdit_food.text()
        cals = self.calUi.lineEdit_cals.text()
        foodCreate = Nutrition(self.token)
        foodCreate.nutrition_create(food_name, cals)
        if food_name == "" or cals == "":
            dialog = QDialog(self)
            layout = QVBoxLayout()
            label = QLabel(self)
            result = "ERROR: empty input"
            label.setText(result)
            layout.addWidget(label)
            dialog.setWindowTitle("ERROR")
            dialog.setLayout(layout)
            dialog.resize(150,100)
            dialog.setMinimumSize(150,100)
            dialog.show()
        else:
            self.food_log[food_name] = float(cals)
            self.food_gain += float(cals)
            self.food_max -= float(cals)
            if self.food_max <= 0:
                self.food_max = 0
            self.ui.label_cal_input.setText(str(self.food_gain) + " : cals in")
            self.ui.label_cal_left.setText(str(self.food_max) + " : cals left")
    
    def show_food_log(self):
        designer_file = QFile("food_log.ui")
        designer_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.food_log_ui = loader.load(designer_file, self)
        designer_file.close()
        for item in self.food_log:
                result = item + " : " + str(self.food_log[item]) + " cal"
                self.food_log_ui.listWidget_Food.addItem(result)
        self.food_log_ui.setWindowTitle("Food Log")
        self.food_log_ui.show()

    def add_water(self):
        dialog = QDialog(self)
        layout = QHBoxLayout()
        label = QLabel(self)
        self.water_input = QLineEdit(self)
        add_button = QPushButton("ADD")
        add_button.clicked.connect(self.update_water)
        label.setText("ml : ")
        layout.addWidget(label)
        layout.addWidget(self.water_input)
        layout.addWidget(add_button)
        dialog.setWindowTitle("Add Water")
        dialog.setLayout(layout)
        dialog.resize(220,100)
        dialog.setMinimumSize(220,100)
        # dialog.setFont(font)
        dialog.show()
        
    def update_water(self):
        if self.water_input.text() == "":
            dialog = QDialog(self)
            layout = QVBoxLayout()
            label = QLabel(self)
            result = "ERROR: empty input"
            label.setText(result)
            layout.addWidget(label)
            dialog.setWindowTitle("ERROR")
            dialog.setLayout(layout)
            dialog.resize(150,100)
            dialog.setMinimumSize(150,100)
            dialog.show()
        else:
            self.water_gain += float(self.water_input.text())
            self.water_max -= float(self.water_input.text())
            if self.water_max <= 0:
                self.water_max = 0
            self.ui.label_water_in.setText(str(self.water_gain) + " : ml")
            self.ui.label_water_left.setText(str(self.water_max) + " : ml left")

# if __name__ == "__main__":
#     app = QApplication([])
#     window = MainWidget()
#     window.show()
#     window.setFixedSize(window.size())
#     app.exec_()
