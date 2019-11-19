# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2000, 1000)
        MainWindow.setMouseTracking(True)
        MainWindow.setFocusPolicy(QtCore.Qt.WheelFocus)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("font: 10pt \"Ariel\";\n"
"border-radius: 20px;\n"
"border-width: 6px;\n")
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setEnabled(True)
        self.treeWidget.setGeometry(QtCore.QRect(0, 80, 401, 581))
        self.treeWidget.setStyleSheet("")
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.selectBtn = QtWidgets.QPushButton(self.centralwidget)
        self.selectBtn.setEnabled(True)
        self.selectBtn.setGeometry(QtCore.QRect(110, 20, 141, 51))
        self.selectBtn.setAutoFillBackground(False)
        self.selectBtn.setStyleSheet("font: 10pt \"Arial\";\n"
"border-radius: 20px;\n"
"border-width: 6px;\n")
        self.selectBtn.setObjectName("selectBtn")
        self.runBtn = QtWidgets.QPushButton(self.centralwidget)
        self.runBtn.setEnabled(True)
        self.runBtn.setGeometry(QtCore.QRect(500, 20, 141, 51))
        self.runBtn.setStyleSheet("background-color: #008CBA; \n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;")
        self.runBtn.setObjectName("runBtn")
        self.stopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn.setEnabled(True)
        self.stopBtn.setGeometry(QtCore.QRect(700, 20, 131, 51))
        self.stopBtn.setStyleSheet("background-color: #008CBA; \n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;")
        self.stopBtn.setObjectName("stopBtn")
        self.clearBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearBtn.setEnabled(True)
        self.clearBtn.setGeometry(QtCore.QRect(950, 610, 151, 51))
        self.clearBtn.setStyleSheet("background-color: #008CBA; \n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;")
        self.clearBtn.setObjectName("clearBtn")
        self.listWidget = QtWidgets.QTextBrowser(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(420, 81, 681, 581))
        self.listWidget.setMouseTracking(True)
        self.listWidget.setAutoFillBackground(True)
        self.listWidget.setStyleSheet("")
        self.listWidget.setObjectName("listWidget")
        self.refreshBtn = QtWidgets.QPushButton(self.centralwidget)
        self.refreshBtn.setGeometry(QtCore.QRect(900, 20, 151, 51))
        self.refreshBtn.setStyleSheet("background-color: #008CBA; \n"
"  border: none;\n"
"  color: white;\n"
"  padding: 15px 32px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  display: inline-block;\n"
"  font-size: 16px;")
        self.refreshBtn.setObjectName("refreshBtn")
        self.selectBtn.raise_()
        self.runBtn.raise_()
        self.stopBtn.raise_()
        self.treeWidget.raise_()
        self.listWidget.raise_()
        self.refreshBtn.raise_()
        self.clearBtn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selectBtn.setText(_translate("MainWindow", "Select Files"))
        self.runBtn.setText(_translate("MainWindow", "Run"))
        self.stopBtn.setText(_translate("MainWindow", "Stop"))
        self.clearBtn.setText(_translate("MainWindow", "Clear"))
        self.refreshBtn.setText(_translate("MainWindow", "Logs"))
