# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\hp\Desktop\EBooks\2018-2019 Currently\2ND\Linux Lab\proj2\proj.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1119, 847)
        Dialog.setStyleSheet("background:-webkit-gradient(linear, 80% 20%, 12% 16%, from(#2392B0), to(#6ED3ED))")
        self.cbData = QtWidgets.QComboBox(Dialog)
        self.cbData.setGeometry(QtCore.QRect(240, 10, 281, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 147, 176))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 215, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 181, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 73, 88))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 98, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 147, 176))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(144, 201, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 147, 176))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 215, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 181, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 73, 88))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 98, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 147, 176))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(144, 201, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 73, 88))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 147, 176))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 215, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(45, 181, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 73, 88))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(22, 98, 117))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 73, 88))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 73, 88))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 147, 176))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 147, 176))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 147, 176))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.cbData.setPalette(palette)
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
        self.cdRules = QtWidgets.QComboBox(Dialog)
        self.cdRules.setGeometry(QtCore.QRect(240, 50, 281, 31))
        self.cdRules.setObjectName("cdRules")
        self.cdRules.addItem("")
        self.cdRules.addItem("")
        self.cdRules.addItem("")
        self.cdRules.addItem("")
        self.cdRules.addItem("")
        self.cdRules.addItem("")
        self.cdRules.addItem("")
        self.cdRules.addItem("")
        self.cdRules.addItem("")
        self.cdRules.addItem("")
        self.label1 = QtWidgets.QLabel(Dialog)
        self.label1.setGeometry(QtCore.QRect(10, 70, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(11)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.lblValid = QtWidgets.QLabel(Dialog)
        self.lblValid.setGeometry(QtCore.QRect(40, 360, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(11)
        self.lblValid.setFont(font)
        self.lblValid.setObjectName("lblValid")
        self.validity = QtWidgets.QLabel(Dialog)
        self.validity.setGeometry(QtCore.QRect(50, 440, 161, 81))
        self.validity.setText("")
        self.validity.setObjectName("validity")
        self.btnChoose = QtWidgets.QPushButton(Dialog)
        self.btnChoose.setGeometry(QtCore.QRect(530, 10, 93, 71))
        self.btnChoose.setObjectName("btnChoose")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label1_2 = QtWidgets.QLabel(Dialog)
        self.label1_2.setGeometry(QtCore.QRect(10, 190, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium Cond")
        font.setPointSize(11)
        self.label1_2.setFont(font)
        self.label1_2.setObjectName("label1_2")
        self.lwData = QtWidgets.QListWidget(Dialog)
        self.lwData.setGeometry(QtCore.QRect(10, 90, 611, 91))
        self.lwData.setLineWidth(5)
        self.lwData.setObjectName("lwData")
        self.lwRules = QtWidgets.QListWidget(Dialog)
        self.lwRules.setGeometry(QtCore.QRect(10, 220, 611, 101))
        self.lwRules.setLineWidth(5)
        self.lwRules.setObjectName("lwRules")
        self.btnV = QtWidgets.QPushButton(Dialog)
        self.btnV.setGeometry(QtCore.QRect(120, 360, 61, 51))
        self.btnV.setStyleSheet("image: url(:/newPrefix/validicy.png)")
        self.btnV.setText("")
        self.btnV.setObjectName("btnV")
        self.lbGIF = QtWidgets.QLabel(Dialog)
        self.lbGIF.setGeometry(QtCore.QRect(440, 400, 161, 111))
        self.lbGIF.setObjectName("lbGIF")
        self.errors = QtWidgets.QListWidget(Dialog)
        self.errors.setGeometry(QtCore.QRect(20, 530, 591, 291))
        self.errors.setLineWidth(20)
        self.errors.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.errors.setObjectName("errors")
        self.cbCA = QtWidgets.QCheckBox(Dialog)
        self.cbCA.setGeometry(QtCore.QRect(210, 360, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(10)
        font.setUnderline(True)
        self.cbCA.setFont(font)
        self.cbCA.setObjectName("cbCA")
        self.cbCE = QtWidgets.QCheckBox(Dialog)
        self.cbCE.setGeometry(QtCore.QRect(400, 360, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(10)
        font.setUnderline(True)
        self.cbCE.setFont(font)
        self.cbCE.setObjectName("cbCE")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(650, 430, 461, 391))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.btnUpdateCE = QtWidgets.QPushButton(self.groupBox_2)
        self.btnUpdateCE.setGeometry(QtCore.QRect(180, 330, 93, 41))
        self.btnUpdateCE.setObjectName("btnUpdateCE")
        self.lwCEData = QtWidgets.QListWidget(self.groupBox_2)
        self.lwCEData.setGeometry(QtCore.QRect(10, 10, 181, 271))
        self.lwCEData.setAutoFillBackground(False)
        self.lwCEData.setObjectName("lwCEData")
        self.btnMove2 = QtWidgets.QPushButton(self.groupBox_2)
        self.btnMove2.setGeometry(QtCore.QRect(200, 120, 41, 31))
        self.btnMove2.setObjectName("btnMove2")
        self.listWidget_4 = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget_4.setGeometry(QtCore.QRect(250, 10, 191, 271))
        self.listWidget_4.setObjectName("listWidget_4")
        self.leCE = QtWidgets.QLineEdit(self.groupBox_2)
        self.leCE.setGeometry(QtCore.QRect(10, 290, 431, 31))
        self.leCE.setObjectName("leCE")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(650, 10, 461, 381))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.btnUpdateCA = QtWidgets.QPushButton(self.groupBox_3)
        self.btnUpdateCA.setGeometry(QtCore.QRect(180, 330, 93, 41))
        self.btnUpdateCA.setObjectName("btnUpdateCA")
        self.lwCAData = QtWidgets.QListWidget(self.groupBox_3)
        self.lwCAData.setGeometry(QtCore.QRect(10, 10, 181, 271))
        self.lwCAData.setAutoFillBackground(False)
        self.lwCAData.setObjectName("lwCAData")
        self.btnMove1 = QtWidgets.QPushButton(self.groupBox_3)
        self.btnMove1.setGeometry(QtCore.QRect(200, 120, 41, 31))
        self.btnMove1.setObjectName("btnMove1")
        self.lwCustomAttributes = QtWidgets.QListWidget(self.groupBox_3)
        self.lwCustomAttributes.setGeometry(QtCore.QRect(250, 10, 191, 271))
        self.lwCustomAttributes.setObjectName("lwCustomAttributes")
        self.leCA = QtWidgets.QLineEdit(self.groupBox_3)
        self.leCA.setGeometry(QtCore.QRect(10, 290, 431, 31))
        self.leCA.setObjectName("leCA")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cbData.setItemText(0, _translate("Dialog", "Data1"))
        self.cbData.setItemText(1, _translate("Dialog", "Data2"))
        self.cbData.setItemText(2, _translate("Dialog", "Data3"))
        self.cbData.setItemText(3, _translate("Dialog", "Data4"))
        self.cbData.setItemText(4, _translate("Dialog", "Data5"))
        self.cbData.setItemText(5, _translate("Dialog", "Data6"))
        self.cbData.setItemText(6, _translate("Dialog", "Data7"))
        self.cbData.setItemText(7, _translate("Dialog", "Data8"))
        self.cbData.setItemText(8, _translate("Dialog", "Data9"))
        self.cbData.setItemText(9, _translate("Dialog", "Data10"))
        self.cdRules.setItemText(0, _translate("Dialog", "Rules1"))
        self.cdRules.setItemText(1, _translate("Dialog", "Rules2"))
        self.cdRules.setItemText(2, _translate("Dialog", "Rules3"))
        self.cdRules.setItemText(3, _translate("Dialog", "Rules4"))
        self.cdRules.setItemText(4, _translate("Dialog", "Rules5"))
        self.cdRules.setItemText(5, _translate("Dialog", "Rules6"))
        self.cdRules.setItemText(6, _translate("Dialog", "Rules7"))
        self.cdRules.setItemText(7, _translate("Dialog", "Rules8"))
        self.cdRules.setItemText(8, _translate("Dialog", "Rules9"))
        self.cdRules.setItemText(9, _translate("Dialog", "Rules10"))
        self.label1.setText(_translate("Dialog", "Data"))
        self.lblValid.setText(_translate("Dialog", "Is It Valid?"))
        self.btnChoose.setText(_translate("Dialog", "Choose"))
        self.label.setText(_translate("Dialog", "Choose Data and Rules Set"))
        self.label1_2.setText(_translate("Dialog", "Rules"))
        self.lbGIF.setText(_translate("Dialog", "TextLabel"))
        self.cbCA.setText(_translate("Dialog", "Custom Attrubutes"))
        self.cbCE.setText(_translate("Dialog", "Custom Errors"))
        self.btnUpdateCE.setText(_translate("Dialog", "Update"))
        self.btnMove2.setText(_translate("Dialog", ">"))
        self.btnUpdateCA.setText(_translate("Dialog", "Update"))
        self.btnMove1.setText(_translate("Dialog", ">"))

#import source_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

