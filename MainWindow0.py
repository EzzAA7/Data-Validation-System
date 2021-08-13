# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\hp\Desktop\EBooks\2018-2019 Currently\2ND\Linux Lab\proj2\proj.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import re

from PyQt5 import QtCore, QtGui, QtWidgets
##from Dialog import Ui_Dialog
##from DataValidator import DataValidator


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(624, 650)
        MainWindow.setStyleSheet("background:-webkit-gradient(linear, 80% 20%, 12% 16%, from(#2392B0), to(#6ED3ED))")
        self.cbData = QtWidgets.QComboBox(MainWindow)
        self.cbData.setGeometry(QtCore.QRect(220, 20, 251, 31))

        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        self.cbData.setFont(font)
        self.cbData.setAutoFillBackground(False)
        self.cbData.setStyleSheet("background:-webkit-gradient(linear, 80% 20%, 12% 16%, from(#2392B0), to(#6ED3ED))")
        self.cbData.setObjectName("cbData")
        self.cbData.addItem("")
        self.cbData.addItem("")
        self.cbData.addItem("")
        self.cbData.addItem("")
        self.cbData.addItem("")
        self.cbData.addItem("")
        self.cbData.addItem("")
        self.cbData.addItem("")
        self.cbData.addItem("")
        self.cbData.addItem("")

        self.cbRules = QtWidgets.QComboBox(MainWindow)
        self.cbRules.setGeometry(QtCore.QRect(220, 50, 251, 31))
        self.cbRules.setObjectName("cbRules")
        self.cbRules.addItem("")
        self.cbRules.addItem("")
        self.cbRules.addItem("")
        self.cbRules.addItem("")
        self.cbRules.addItem("")
        self.cbRules.addItem("")
        self.cbRules.addItem("")
        self.cbRules.addItem("")
        self.cbRules.addItem("")
        self.cbRules.addItem("")

        self.label1 = QtWidgets.QLabel(MainWindow)
        self.label1.setGeometry(QtCore.QRect(30, 70, 121, 21))

        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(11)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")

        self.lblValid = QtWidgets.QLabel(MainWindow)
        self.lblValid.setGeometry(QtCore.QRect(30, 340, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(11)
        self.lblValid.setFont(font)
        self.lblValid.setObjectName("lblValid")

        self.validity = QtWidgets.QLabel(MainWindow)
        self.validity.setGeometry(QtCore.QRect(30, 380, 111, 71))
        self.validity.setText("")
        self.validity.setObjectName("validity")

        self.btnChoose = QtWidgets.QPushButton(MainWindow)
        self.btnChoose.setGeometry(QtCore.QRect(480, 20, 93, 28))
        self.btnChoose.setObjectName("btnChoose")
        self.btnChoose.clicked.connect(self.choose)
        self.btnChoose.setFlat(True)

        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(30, 20, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label1_2 = QtWidgets.QLabel(MainWindow)
        self.label1_2.setGeometry(QtCore.QRect(30, 190, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(11)
        self.label1_2.setFont(font)
        self.label1_2.setObjectName("label1_2")

        self.btnV = QtWidgets.QPushButton(MainWindow)
        self.btnV.setGeometry(QtCore.QRect(110, 330, 101, 51))
        self.btnV.setStyleSheet("image: url(:/newPrefix/validicy.png)")
        self.btnV.setText("")
        self.btnV.setObjectName("btnV")
        self.btnV.setIcon(QtGui.QIcon("validicy.png"))
        self.btnV.clicked.connect(self.PrintError)

        self.lwData = QtWidgets.QListWidget(MainWindow)
        self.lwData.setGeometry(QtCore.QRect(30, 90, 541, 91))
        self.lwData.setObjectName("lwData")

        self.lwRules = QtWidgets.QListWidget(MainWindow)
        self.lwRules.setGeometry(QtCore.QRect(30, 220, 541, 101))
        self.lwRules.setObjectName("lwRules")

        self.lbGIF = QtWidgets.QLabel(MainWindow)
        self.lbGIF.setGeometry(QtCore.QRect(410, 350, 161, 111))
        self.lbGIF.setObjectName("lbGIF")

        self.errors = QtWidgets.QListWidget(MainWindow)
        self.errors.setGeometry(QtCore.QRect(30, 500, 531, 131))
        self.errors.setObjectName("errors")

        movie = QtGui.QMovie("gif.gif")
        self.lbGIF.setMovie(movie)
        movie.start()


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def choose(self):
        self.lwData.clear()
        cbDataText = self.cbData.currentText()
        data = {}
        with open(cbDataText, 'r') as f:
            for line in f:
                (key, val) = line.split(",")
                data[(key)] = val
        self.lwData.addItem(str(data))


        self.lwRules.clear()
        cbRulesText = self.cbRules.currentText()
        rules = {}
        with open(cbRulesText, 'r') as fi:
            for line in fi:
                (key, val) = line.split(",")
                rules[(key)] = val
        self.lwRules.addItem(str(rules))

        return data, rules

    def PrintError(self):
        error = []
        data , rules = self.choose()
        for keyData, valData in data.items():
            for keyRule, valRule in rules.items():
                if keyData == keyRule:
                    valRule = valRule.lstrip()
                    valRule = re.sub('\n', '', valRule)
                    valData = valData.lstrip()
                    if valRule == "string":                       ## String
                        if valData[0].isdigit():
                            error.append("The " +valRule +" field must be a String")
                    elif valRule == "number":                       ## Number
                        try:
                            valData = int(valData)
                        except ValueError:
                            error.append("The " +valRule +" field must be a Number")
                    elif valRule == "email":                      ## email
                        email_reg = r'[^@]+@[^@]+\.[^@]+'
                        if not valData:
                            print("")   ##Empty
                        if re.match(email_reg, valData):
                            print("")
                        else:
                            error.append("The " + valRule + " field must be a Email")


                    elif valRule == "phone number":
                        phone_reg = r"[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]"

                        if valData.count('+') != 1 :
                            error.append("The " +valRule +" field must be a Phone Number")

                        if valData.startswith('+'):
                            valData = valData.replace('+', '')
                        if not valData:   ##Empty
                            print("")
                        if re.match(phone_reg, valData):
                            print("")
                        else:
                            error.append("The " + valRule + " field must be a Phone Number")

                    elif valRule == "date":
                        date_reg = r"[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]"

                        if not valData:   ##Empty
                            print("")
                        if re.match(date_reg, valData):
                            print("")
                        else:
                            error.append("The " + valRule + " field must be a valid Date")




        self.errors.clear()
        if not error:
            self.errors.addItem(str("There is no Error found !!"))
        else:
            self.errors.addItem(str(error))



        """
        print ("-" *50)
        for key, val in rules.items():
            print (key, "=>", val)
        """




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Data Validator", "Data Validator"))
        self.cbData.setItemText(0, _translate("MainWindow", "Data1.txt"))
        self.cbData.setItemText(1, _translate("MainWindow", "Data2.txt"))
        self.cbData.setItemText(2, _translate("MainWindow", "Data3.txt"))
        self.cbData.setItemText(3, _translate("MainWindow", "Data4.txt"))
        self.cbData.setItemText(4, _translate("MainWindow", "Data5.txt"))
        self.cbData.setItemText(5, _translate("MainWindow", "Data6.txt"))
        self.cbData.setItemText(6, _translate("MainWindow", "Data7.txt"))
        self.cbData.setItemText(7, _translate("MainWindow", "Data8.txt"))
        self.cbData.setItemText(8, _translate("MainWindow", "Data9.txt"))
        self.cbData.setItemText(9, _translate("MainWindow", "Data10.txt"))
        self.cbRules.setItemText(0, _translate("MainWindow", "Rules1.txt"))
        self.cbRules.setItemText(1, _translate("MainWindow", "Rules2.txt"))
        self.cbRules.setItemText(2, _translate("MainWindow", "Rules3.txt"))
        self.cbRules.setItemText(3, _translate("MainWindow", "Rules4.txt"))
        self.cbRules.setItemText(4, _translate("MainWindow", "Rules5.txt"))
        self.cbRules.setItemText(5, _translate("MainWindow", "Rules6.txt"))
        self.cbRules.setItemText(6, _translate("MainWindow", "Rules7.txt"))
        self.cbRules.setItemText(7, _translate("MainWindow", "Rules8.txt"))
        self.cbRules.setItemText(8, _translate("MainWindow", "Rules9.txt"))
        self.cbRules.setItemText(9, _translate("MainWindow", "Rules10.txt"))
        self.label1.setText(_translate("MainWindow", "Data & Rules"))
        self.lblValid.setText(_translate("MainWindow", "Is It Valid?"))
        self.btnChoose.setText(_translate("MainWindow", "Choose"))
        ##      self.btnReset.setText(_translate("MainWindow", "Reset"))
        self.label.setText(_translate("MainWindow", "Choose Data and Rules Set"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
