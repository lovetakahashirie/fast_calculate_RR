# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rr_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(242,228)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3R_value = QtWidgets.QLabel(self.centralwidget)
        self.label_3R_value.setGeometry(QtCore.QRect(110, 160, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3R_value.setFont(font)
        self.label_3R_value.setAutoFillBackground(False)
        self.label_3R_value.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3R_value.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3R_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3R_value.setObjectName("label_3R_value")
        self.lineEdit_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_entry.setGeometry(QtCore.QRect(110, 10, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_entry.setFont(font)
        self.lineEdit_entry.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_entry.setObjectName("lineEdit_entry")
        # my trigger function here
        self.lineEdit_entry.textChanged.connect(self.update_2R3R_label)
        self.label_2R_value = QtWidgets.QLabel(self.centralwidget)
        self.label_2R_value.setGeometry(QtCore.QRect(110, 110, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2R_value.setFont(font)
        self.label_2R_value.setAutoFillBackground(False)
        self.label_2R_value.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2R_value.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2R_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2R_value.setObjectName("label_2R_value")
        self.lineEdit_stop = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_stop.setGeometry(QtCore.QRect(110, 60, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_stop.setFont(font)
        self.lineEdit_stop.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_stop.setObjectName("lineEdit_stop")
        # my trigger function here
        self.lineEdit_stop.textChanged.connect(self.update_2R3R_label)
        self.label_entry = QtWidgets.QLabel(self.centralwidget)
        self.label_entry.setGeometry(QtCore.QRect(10, 10, 80, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_entry.setFont(font)
        self.label_entry.setAutoFillBackground(False)
        self.label_entry.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(252, 252, 252);")
        self.label_entry.setAlignment(QtCore.Qt.AlignCenter)
        self.label_entry.setObjectName("label_entry")
        self.label_3R = QtWidgets.QLabel(self.centralwidget)
        self.label_3R.setGeometry(QtCore.QRect(10, 160, 80, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3R.setFont(font)
        self.label_3R.setAutoFillBackground(False)
        self.label_3R.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(252, 252, 252);")
        self.label_3R.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3R.setObjectName("label_3R")
        self.label_stop = QtWidgets.QLabel(self.centralwidget)
        self.label_stop.setGeometry(QtCore.QRect(10, 60, 80, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_stop.setFont(font)
        self.label_stop.setAutoFillBackground(False)
        self.label_stop.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(252, 252, 252);")
        self.label_stop.setAlignment(QtCore.Qt.AlignCenter)
        self.label_stop.setObjectName("label_stop")
        self.label_2R = QtWidgets.QLabel(self.centralwidget)
        self.label_2R.setGeometry(QtCore.QRect(10, 110, 80, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2R.setFont(font)
        self.label_2R.setAutoFillBackground(False)
        self.label_2R.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(252, 252, 252);")
        self.label_2R.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2R.setObjectName("label_2R")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def update_2R3R_label(self):
        # first get value in entry and stop lineEdit
        entry_text = self.lineEdit_entry.text()
        stop_text = self.lineEdit_stop.text()
        try:
            float(entry_text)
            entry = float(entry_text)
        except ValueError:
            entry = 0
        
        try:
            float(stop_text)
            stop = float(stop_text)
        except ValueError:
            stop = 0

        risk = entry-stop
        # calculate 2R and 3R
        two_R = entry + 2*risk
        three_R = entry + 3*risk
        # update 2R and 3R label
        self.label_2R_value.setText(str(round(two_R,2)))
        self.label_3R_value.setText(str(round(three_R,2)))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3R_value.setText(_translate("MainWindow", "0"))
        self.lineEdit_entry.setText(_translate("MainWindow", "0"))
        self.label_2R_value.setText(_translate("MainWindow", "0"))
        self.lineEdit_stop.setText(_translate("MainWindow", "0"))
        self.label_entry.setText(_translate("MainWindow", "ENTRY"))
        self.label_3R.setText(_translate("MainWindow", "3R"))
        self.label_stop.setText(_translate("MainWindow", "STOP"))
        self.label_2R.setText(_translate("MainWindow", "2R"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
