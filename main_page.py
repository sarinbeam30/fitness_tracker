# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_page.ui',
# licensing of 'main_page.ui' applies.
#
# Created: Wed May 29 21:17:44 2019
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
        self.heart_rate_widgets.setGeometry(QtCore.QRect(156, 60, 585, 340))
        self.heart_rate_widgets.setStyleSheet("border : 2px solid black;\n"
"border-radius : 15px;\n"
"background : white;")
        self.heart_rate_widgets.setObjectName("heart_rate_widgets")
        self.steps_widgets = QtWidgets.QWidget(self.dash_board)
        self.steps_widgets.setGeometry(QtCore.QRect(842, 60, 585, 340))
        self.steps_widgets.setStyleSheet("border : 2px solid black;\n"
"border-radius : 15px;\n"
"background : white;")
        self.steps_widgets.setObjectName("steps_widgets")
        self.food_widgets = QtWidgets.QWidget(self.dash_board)
        self.food_widgets.setGeometry(QtCore.QRect(156, 450, 585, 340))
        self.food_widgets.setStyleSheet("border : 2px solid black;\n"
"border-radius : 15px;\n"
"background : white;")
        self.food_widgets.setObjectName("food_widgets")
        self.quote_widgets = QtWidgets.QWidget(self.dash_board)
        self.quote_widgets.setGeometry(QtCore.QRect(842, 450, 585, 340))
        self.quote_widgets.setStyleSheet("border : 2px solid black;\n"
"border-radius : 15px;\n"
"background : white;")
        self.quote_widgets.setObjectName("quote_widgets")
        self.tabWidget.addTab(self.dash_board, "")
        self.profile = QtWidgets.QWidget()
        self.profile.setObjectName("profile")
        self.tabWidget.addTab(self.profile, "")
        self.user_name = QtWidgets.QWidget()
        self.user_name.setObjectName("user_name")
        self.tabWidget.addTab(self.user_name, "")

        self.retranslateUi(main_page)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_page)

    def retranslateUi(self, main_page):
        main_page.setWindowTitle(QtWidgets.QApplication.translate("main_page", "Form", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dash_board), QtWidgets.QApplication.translate("main_page", "DASHBOARD     ", None, -1))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.dash_board), QtWidgets.QApplication.translate("main_page", "Your dashboard", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.profile), QtWidgets.QApplication.translate("main_page", "PROFILE", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.user_name), QtWidgets.QApplication.translate("main_page", "                                                                                                        Sarin Wanichwasin", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_page = QtWidgets.QWidget()
    ui = Ui_main_page()
    ui.setupUi(main_page)
    main_page.show()
    sys.exit(app.exec_())

