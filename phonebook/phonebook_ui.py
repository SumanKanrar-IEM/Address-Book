# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'phonebook.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1123, 665)
        Dialog.setMinimumSize(QtCore.QSize(1123, 665))
        Dialog.setMaximumSize(QtCore.QSize(1123, 665))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("phonebook.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(161, 191, 255);")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 1061, 601))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("font: 75 15pt \"Comic Sans MS\";\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableView = QtWidgets.QTableView(self.tab)
        self.tableView.setGeometry(QtCore.QRect(20, 40, 731, 471))
        self.tableView.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.tableView.setObjectName("tableView")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(820, 210, 161, 51))
        self.pushButton.setStyleSheet("font: 75 15pt \"Comic Sans MS\";\n"
"background-color: rgb(255, 170, 127);\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(820, 300, 161, 51))
        self.pushButton_2.setStyleSheet("font: 75 15pt \"Comic Sans MS\";\n"
"background-color: rgb(255, 170, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("font: 75 15pt \"Comic Sans MS\";")
        self.tab_2.setObjectName("tab_2")
        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setGeometry(QtCore.QRect(30, 40, 371, 471))
        self.listWidget.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_2.setGeometry(QtCore.QRect(430, 40, 371, 471))
        self.listWidget_2.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.listWidget_2.setObjectName("listWidget_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(830, 230, 211, 91))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("font: 75 12pt \"Comic Sans MS\";\n"
"background-color: rgb(255, 170, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.listWidget_3 = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_3.setGeometry(QtCore.QRect(30, 40, 371, 471))
        self.listWidget_3.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.listWidget_3.setObjectName("listWidget_3")
        self.textEdit = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit.setGeometry(QtCore.QRect(430, 40, 591, 321))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.textEdit.setObjectName("textEdit")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_4.setGeometry(QtCore.QRect(640, 400, 191, 91))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("font: 75 15pt \"Comic Sans MS\";\n"
"background-color: rgb(255, 170, 127);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.listWidget_4 = QtWidgets.QListWidget(self.tab_4)
        self.listWidget_4.setGeometry(QtCore.QRect(30, 40, 371, 471))
        self.listWidget_4.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.listWidget_4.setObjectName("listWidget_4")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit.setGeometry(QtCore.QRect(430, 40, 601, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_2.setGeometry(QtCore.QRect(430, 100, 601, 321))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_5.setGeometry(QtCore.QRect(630, 440, 191, 91))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("font: 75 15pt \"Comic Sans MS\";\n"
"background-color: rgb(255, 170, 127);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget.addTab(self.tab_4, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Phonebook"))
        self.pushButton.setText(_translate("Dialog", "  Add Contact  "))
        self.pushButton_2.setText(_translate("Dialog", "Backup"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "          Contacts            "))
        self.pushButton_3.setText(_translate("Dialog", "Send Voice Message"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "          Voice Message         "))
        self.textEdit.setPlaceholderText(_translate("Dialog", "Type Message Here"))
        self.pushButton_4.setText(_translate("Dialog", "Send Message"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "         SMS         "))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "To  :    Email  ID  Here"))
        self.textEdit_2.setPlaceholderText(_translate("Dialog", "Type your Mail Here"))
        self.pushButton_5.setText(_translate("Dialog", "Send Mail"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "         Email          "))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


