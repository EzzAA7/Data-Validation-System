# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\hp\Desktop\EBooks\2018-2019 Currently\2ND\Linux Lab\proj2\proj.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import re

from PyQt5 import QtCore, QtGui, QtWidgets
##from MainWindow import Ui_MainWindow
##from DataValidator import DataValidator


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(624, 847)
        MainWindow.setStyleSheet("background:-webkit-gradient(linear, 80% 20%, 12% 16%, from(#2392B0), to(#6ED3ED))")
        self.cbData = QtWidgets.QComboBox(MainWindow)
        self.cbData.setGeometry(QtCore.QRect(240, 10, 281, 31))

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
        self.cbRules.setGeometry(QtCore.QRect(240, 50, 281, 31))
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
        self.label1.setGeometry(QtCore.QRect(10, 70, 121, 21))

        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(11)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")

        self.lblValid = QtWidgets.QLabel(MainWindow)
        self.lblValid.setGeometry(QtCore.QRect(40, 360, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(11)
        self.lblValid.setFont(font)
        self.lblValid.setObjectName("lblValid")

        self.validity = QtWidgets.QLabel(MainWindow)
        self.validity.setGeometry(QtCore.QRect(50, 440, 161, 81))
        self.validity.setText("")
        self.validity.setObjectName("validity")

        self.btnChoose = QtWidgets.QPushButton(MainWindow)
        self.btnChoose.setGeometry(QtCore.QRect(530, 10, 93, 71))
        self.btnChoose.setObjectName("btnChoose")
        self.btnChoose.clicked.connect(self.choose)
        self.btnChoose.setFlat(True)

        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(10, 10, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label1_2 = QtWidgets.QLabel(MainWindow)
        self.label1_2.setGeometry(QtCore.QRect(10, 190, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(11)
        self.label1_2.setFont(font)
        self.label1_2.setObjectName("label1_2")

        self.btnV = QtWidgets.QPushButton(MainWindow)
        self.btnV.setGeometry(QtCore.QRect(120, 360, 61, 51))
        self.btnV.setStyleSheet("image: url(:/newPrefix/validicy.png)")
        self.btnV.setText("")
        self.btnV.setObjectName("btnV")
        self.btnV.setIcon(QtGui.QIcon("validicy.png"))
        self.btnV.clicked.connect(self.PrintError)

        self.lwData = QtWidgets.QListWidget(MainWindow)
        self.lwData.setGeometry(QtCore.QRect(10, 90, 611, 91))
        self.lwData.setObjectName("lwData")

        self.lwRules = QtWidgets.QListWidget(MainWindow)
        self.lwRules.setGeometry(QtCore.QRect(10, 220, 611, 101))
        self.lwRules.setObjectName("lwRules")

        self.lbGIF = QtWidgets.QLabel(MainWindow)
        self.lbGIF.setGeometry(QtCore.QRect(440, 400, 161, 111))
        self.lbGIF.setObjectName("lbGIF")

        movie = QtGui.QMovie("gif.gif")
        self.lbGIF.setMovie(movie)
        movie.start()

        self.errors = QtWidgets.QListWidget(MainWindow)
        self.errors.setGeometry(QtCore.QRect(20, 530, 591, 291))
        self.errors.setLineWidth(20)
        self.errors.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.errors.setObjectName("errors")

        self.cbCA = QtWidgets.QCheckBox(MainWindow)
        self.cbCA.setGeometry(QtCore.QRect(210, 360, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(10)
        font.setUnderline(True)

        self.cbCA.setFont(font)
        self.cbCA.setObjectName("cbCA")
        self.cbCE = QtWidgets.QCheckBox(MainWindow)
        self.cbCE.setGeometry(QtCore.QRect(400, 360, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(10)
        font.setUnderline(True)
        self.cbCA.stateChanged.connect(self.cbCAIsChecked)


        self.cbCE.setFont(font)
        self.cbCE.setObjectName("cbCE")
        self.cbCE.stateChanged.connect(self.cbCEIsChecked)

        self.gbCE = QtWidgets.QGroupBox(MainWindow)
        self.gbCE.setGeometry(QtCore.QRect(650, 430, 461, 301))
        self.gbCE.setTitle("")
        self.gbCE.setObjectName("gbCE")

        self.btnUpdateCE = QtWidgets.QPushButton(self.gbCE)
        self.btnUpdateCE.setGeometry(QtCore.QRect(170, 250, 93, 41))
        self.btnUpdateCE.setObjectName("btnUpdateCE")

        self.label1_4 = QtWidgets.QLabel(self.gbCE)
        self.label1_4.setGeometry(QtCore.QRect(10, 10, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(11)
        self.label1_4.setFont(font)
        self.label1_4.setObjectName("label1_4")

        self.cbCErr = QtWidgets.QComboBox(self.gbCE)
        self.cbCErr.setGeometry(QtCore.QRect(10, 40, 281, 31))
        font.setFamily("Franklin Gothic Book")
        self.cbCErr.setFont(font)
        self.cbCErr.setAutoFillBackground(False)
        self.cbCErr.setStyleSheet("background:-webkit-gradient(linear, 80% 20%, 12% 16%, from(#2392B0), to(#6ED3ED))")
        self.cbCErr.setObjectName("cbCErr")
        self.cbCErr.addItem("")
        self.cbCErr.addItem("")
        self.cbCErr.addItem("")
        self.cbCErr.addItem("")
        self.cbCErr.addItem("")
        self.cbCErr.addItem("")
        self.cbCErr.addItem("")
        self.cbCErr.addItem("")
        self.cbCErr.addItem("")
        self.cbCErr.addItem("")

        self.lwCE = QtWidgets.QListWidget(self.gbCE)
        self.lwCE.setGeometry(QtCore.QRect(10, 80, 441, 161))
        self.lwCE.setLineWidth(5)
        self.lwCE.setObjectName("lwCE")
        self.gbCA = QtWidgets.QGroupBox(MainWindow)
        self.gbCA.setGeometry(QtCore.QRect(650, 40, 461, 341))
        self.gbCA.setTitle("")
        self.gbCA.setObjectName("gbCA")

        self.btnUpdateCA = QtWidgets.QPushButton(self.gbCA)
        self.btnUpdateCA.setGeometry(QtCore.QRect(160, 290, 93, 41))
        self.btnUpdateCA.setObjectName("btnUpdateCA")
        self.btnUpdateCA.clicked.connect(self.updateCA)


        self.lwCA = QtWidgets.QListWidget(self.gbCA)
        self.lwCA.setGeometry(QtCore.QRect(10, 80, 441, 201))
        self.lwCA.setLineWidth(5)
        self.lwCA.setObjectName("lwCA")

        self.cbCAtt = QtWidgets.QComboBox(self.gbCA)
        self.cbCAtt.setGeometry(QtCore.QRect(10, 40, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        self.cbCAtt.setFont(font)
        self.cbCAtt.setAutoFillBackground(False)
        self.cbCAtt.setStyleSheet("background:-webkit-gradient(linear, 80% 20%, 12% 16%, from(#2392B0), to(#6ED3ED))")
        self.cbCAtt.setObjectName("cbCAtt")
        self.cbCAtt.addItem("")
        self.cbCAtt.addItem("")
        self.cbCAtt.addItem("")
        self.cbCAtt.addItem("")
        self.cbCAtt.addItem("")
        self.cbCAtt.addItem("")
        self.cbCAtt.addItem("")
        self.cbCAtt.addItem("")
        self.cbCAtt.addItem("")
        self.cbCAtt.addItem("")

        self.label1_3 = QtWidgets.QLabel(self.gbCA)
        self.label1_3.setGeometry(QtCore.QRect(10, 10, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(11)
        self.label1_3.setFont(font)
        self.label1_3.setObjectName("label1_3")

        self.btnChoose_2 = QtWidgets.QPushButton(self.gbCA)
        self.btnChoose_2.setGeometry(QtCore.QRect(302, 40, 91, 31))
        self.btnChoose_2.setObjectName("btnChoose_2")
        self.btnChoose_2.clicked.connect(self.chooseCA)


        self.btnChoose_3 = QtWidgets.QPushButton(self.gbCE)
        self.btnChoose_3.setGeometry(QtCore.QRect(300, 40, 91, 31))
        self.btnChoose_3.setObjectName("btnChoose_3")
        self.btnChoose_3.clicked.connect(self.chooseCE)



        self.gbCA.setEnabled(False)
        self.gbCE.setEnabled(False)
        


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
                (key, val) = line.split(",",1)
                rules[(key)] = val
        self.lwRules.addItem(str(rules))

        return data, rules
    
    def chooseCA(self):            
        self.lwCA.clear()
        cbCAtext = self.cbCAtt.currentText()
        CA = {}
        with open(cbCAtext, 'r') as f:
            for line in f:
                (key, val) = line.split(": ")
                CA[(key)] = val

        self.lwCA.addItem(str(CA))

        return CA

    def chooseCE(self):            
        self.lwCE.clear()
        cbCEtext = self.cbCErr.currentText()
        CE = {}
        with open(cbCEtext, 'r') as f:
            for line in f:
                (key, val) = line.split(": ")
                CE[(key)] = val

        self.lwCE.addItem(str(CE))

        return CE


    def cbCAIsChecked(self,state):
        
        self.lwCA.clear()

        if state == QtCore.Qt.Checked:
            MainWindow.resize(1119, 847)
            self.gbCA.setEnabled(True)
            data , rules = self.choose()


        else:
            self.gbCA.setEnabled(False)


    def cbCEIsChecked(self,state):

        self.lwCE.clear()

        if state == QtCore.Qt.Checked:
            MainWindow.resize(1119, 847)
            self.gbCE.setEnabled(True)
            data , rules = self.choose()
        else:
            self.gbCE.setEnabled(False)

    def updateCA(self):

        data , rules = self.choose()
        CA=self.chooseCA()
        #newData=dict(data)
            
        for key1, value1 in data.items() :
            for key2,value2 in CA.items():
                if key1==key2:
                    data[value2] = data[key1]
                    del data[key1]
        self.lwData.clear()
        self.lwData.addItem(str(data))
                    



    def PrintError(self):
        error = []
        data , rules = self.choose()
        for keyData, valData in data.items():
            for keyRule, valRule in rules.items():
                if keyData == keyRule:
                    valData = valData.lstrip()
                    valData = re.sub('\n', '', valData)
                    if '|' in valRule:  ##re.search(r"|",valRule):
                        valRule=valRule.split('|')
                        for x in range(len(valRule)):



                            valRule[x] = valRule[x].lstrip()
                            valRule[x] = re.sub('\n', '', valRule[x])

                            if valRule[x] == "string":                       ## String
                                if valData[0].isdigit():
                                    error.append("The " +keyRule +" field must be a String")
                            elif valRule[x] == "number":                       ## Number
                                try:
                                    valData = int(valData)
                                except ValueError:
                                    error.append("The " +keyRule +" field must be a Number")
                            elif valRule[x] == "email":                      ## email
                                email_reg = r'[^@]+@[^@]+\.[^@]+'
                                if not valData:
                                    print("")   ##Empty
                                if re.match(email_reg, valData):
                                    print("")
                                else:
                                    error.append("The " + keyRule + " field must be a Email")


                            elif valRule[x] == "phone number":     ##Phone Number
                                phone_reg = r"[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]"

                                if valData.count('+') != 1 :
                                    error.append("The " +keyRule +" field must be a Phone Number")

                                if valData.startswith('+'):
                                    valData = valData.replace('+', '')
                                if not valData:   ##Empty
                                    print("")
                                if re.match(phone_reg, valData):
                                    print("")
                                else:
                                    error.append("The " + keyRule + " field must be a Phone Number")

                            elif valRule[x] == "date":     ##Date
                                date_reg = r"[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]"

                                if not valData:   ##Empty
                                    print("")
                                if re.match(date_reg, valData):
                                    print("")
                                else:
                                    error.append("The " + keyRule + " field must be a valid Date")

                            elif re.match(r"min",valRule[x]):
                                splitWord=valRule[x].split(':')

                                if not valData:
                                    print("")
                                if str(valData) < splitWord[1]:
                                    error.append("The " + keyRule + " field must be at least "+ splitWord[1])

                            elif re.match(r"max", valRule[x]):
                                splitWord = valRule[x].split(':')

                                if not valData:
                                    print("")
                                if valData > splitWord[1]:
                                    error.append("The " + keyRule + " field must be at max " + splitWord[1])

                            elif valRule[x] == "Array":

                                if not valData:
                                    print("")

                                if valData.startswith('[') and valData.endswith(']'):
                                    print("")
                                else:
                                    error.append("The " + keyRule + " field must be a Array")

                            elif re.match(r"in", valRule[x]):
                                if not valData:
                                    print("")

                                splitWord1=valRule[x].split(':')   ## split (in) and another charachter
                                splitWord1=splitWord1[1].split(',')  ## split character to pieces

                                CheckTrue = 0
                                for x in range(len(splitWord1)):
                                    if splitWord1[x] == valData:
                                        CheckTrue= 1

                                if CheckTrue == 0:
                                    error.append("The " + keyRule + " field must be one of these "+ ', '.join(splitWord1))

                            elif valRule[x] == "Required":
                                if not valData:
                                    error.append("The " + keyRule + " field is required.")
                    else:
                        valRule = valRule.lstrip()
                        valRule = re.sub('\n', '', valRule)
                        ##  valData = valData.lstrip()
                        ## valData = re.sub('\n', '', valData)
                        if valRule == "string":  ## String
                            if valData[0].isdigit():
                                error.append("The " + keyRule + " field must be a String")
                        elif valRule == "number":  ## Number
                            try:
                                valData = int(valData)
                            except ValueError:
                                error.append("The " + keyRule + " field must be a Number")
                        elif valRule == "email":  ## email
                            email_reg = r'[^@]+@[^@]+\.[^@]+'
                            if not valData:
                                print("")  ##Empty
                            if re.match(email_reg, valData):
                                print("")
                            else:
                                error.append("The " + keyRule + " field must be a Email")


                        elif valRule == "phone number":  ##Phone Number
                            phone_reg = r"[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]"

                            if valData.count('+') != 1:
                                error.append("The " + keyRule + " field must be a Phone Number")

                            if valData.startswith('+'):
                                valData = valData.replace('+', '')
                            if not valData:  ##Empty
                                print("")
                            if re.match(phone_reg, valData):
                                print("")
                            else:
                                error.append("The " + keyRule + " field must be a Phone Number")

                        elif valRule == "date":  ##Date
                            date_reg = r"[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]"

                            if not valData:  ##Empty
                                print("")
                            if re.match(date_reg, valData):
                                print("")
                            else:
                                error.append("The " + keyRule + " field must be a valid Date")

                        elif re.match(r"min", valRule):
                            splitWord = valRule.split(':')

                            if not valData:
                                print("")
                            if valData < splitWord[1]:
                                error.append("The " + keyRule + " field must be at least " + splitWord[1])

                        elif re.match(r"max", valRule):
                            splitWord = valRule.split(':')

                            if not valData:
                                print("")
                            if valData > splitWord[1]:
                                error.append("The " + keyRule + " field must be at max " + splitWord[1])

                        elif valRule == "Array":

                            if not valData:
                                print("")

                            if valData.startswith('[') and valData.endswith(']'):
                                print("")
                            else:
                                error.append("The " + keyRule + " field must be a Array")

                        elif re.match(r"in", valRule):
                            if not valData:
                                print("")

                            splitWord1 = valRule.split(':')  ## split (in) and another charachter
                            splitWord1 = splitWord1[1].split(',')  ## split character to pieces

                            CheckTrue = 0
                            for x in range(len(splitWord1)):
                                if splitWord1[x] == valData:
                                    CheckTrue = 1

                            if CheckTrue == 0:
                                error.append("The " + keyRule + " field must be one of these " + ', '.join(splitWord1))

                        elif valRule == "Required":
                            if not valData:
                                error.append("The " + keyRule + " field is required.")


        self.errors.clear()
        if not error:
            self.errors.addItem(str("There is no Error found !!"))
        else:
            self.errors.addItem(str(error))





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
        self.label1.setText(_translate("MainWindow", "Data"))
        self.lblValid.setText(_translate("MainWindow", "Is It Valid?"))
        self.btnChoose.setText(_translate("MainWindow", "Choose"))
        ##      self.btnReset.setText(_translate("MainWindow", "Reset"))
        self.label.setText(_translate("MainWindow", "Choose Data and Rules Set"))
        self.label1_2.setText(_translate("MainWindow", "Rules"))
        self.lbGIF.setText(_translate("MainWindow", "TextLabel"))
        self.cbCA.setText(_translate("MainWindow", "Custom Attrubutes"))
        self.cbCE.setText(_translate("MainWindow", "Custom Errors"))
        self.btnUpdateCE.setText(_translate("MainWindow", "Update"))
        self.btnUpdateCA.setText(_translate("MainWindow", "Update"))
        self.label1_4.setText(_translate("MainWindow", "Custom Errors"))
        self.cbCErr.setItemText(0, _translate("MainWindow", "CEData1.txt"))
        self.cbCErr.setItemText(1, _translate("MainWindow", "CEData2.txt"))
        self.cbCErr.setItemText(2, _translate("MainWindow", "CEData3.txt"))
        self.cbCErr.setItemText(3, _translate("MainWindow", "CEData4.txt"))
        self.cbCErr.setItemText(4, _translate("MainWindow", "CEData5.txt"))
        self.cbCErr.setItemText(5, _translate("MainWindow", "CEData6.txt"))
        self.cbCErr.setItemText(6, _translate("MainWindow", "CEData7.txt"))
        self.cbCErr.setItemText(7, _translate("MainWindow", "CEData8.txt"))
        self.cbCErr.setItemText(8, _translate("MainWindow", "CEData9.txt"))
        self.cbCErr.setItemText(9, _translate("MainWindow", "CEData10.txt"))
        self.cbCAtt.setItemText(0, _translate("MainWindow", "CAData1.txt"))
        self.cbCAtt.setItemText(1, _translate("MainWindow", "CAData2.txt"))
        self.cbCAtt.setItemText(2, _translate("MainWindow", "CAData3.txt"))
        self.cbCAtt.setItemText(3, _translate("MainWindow", "CAData4.txt"))
        self.cbCAtt.setItemText(4, _translate("MainWindow", "CAData5.txt"))
        self.cbCAtt.setItemText(5, _translate("MainWindow", "CAData6.txt"))
        self.cbCAtt.setItemText(6, _translate("MainWindow", "CAData7.txt"))
        self.cbCAtt.setItemText(7, _translate("MainWindow", "CAData8.txt"))
        self.cbCAtt.setItemText(8, _translate("MainWindow", "CAData9.txt"))
        self.cbCAtt.setItemText(9, _translate("MainWindow", "CAData10.txt"))
        self.label1_3.setText(_translate("MainWindow", "Custom Attributes"))
        self.btnChoose_2.setText(_translate("MainWindow", "Choose"))
        self.btnChoose_3.setText(_translate("MainWindow", "Choose"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
