# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'book.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(463, 587)

        self.table = QtWidgets.QTableWidget(Form)
        self.table.setColumnCount(3)
        self.table.setRowCount(3)
        self.table.setGeometry(QtCore.QRect(96, 91, 351, 461))
        self.table.setObjectName("tableView")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(6, 88, 84, 34))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(6, 150, 84, 34))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(6, 212, 84, 34))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(6, 336, 84, 34))
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(6, 398, 84, 34))
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(6, 274, 84, 34))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(6, 460, 84, 34))
        self.pushButton_7.setObjectName("pushButton_7")

        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(6, 522, 84, 34))
        self.pushButton_8.setObjectName("pushButton_8")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 431, 21))
        self.label.setObjectName("label")

        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(110, 50, 110, 34))
        self.pushButton_9.setObjectName("pushButton_9")

        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(220, 50, 110, 34))
        self.pushButton_10.setObjectName("pushButton_10")

        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(330, 50, 110, 34))
        self.pushButton_11.setObjectName("pushButton_11")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "А-Г"))
        self.pushButton_2.setText(_translate("Form", "Д-Ж"))
        self.pushButton_3.setText(_translate("Form", "Ж-Й"))
        self.pushButton_5.setText(_translate("Form", "О-С"))
        self.pushButton_6.setText(_translate("Form", "Т-Х"))
        self.pushButton_4.setText(_translate("Form", "К-Н"))
        self.pushButton_7.setText(_translate("Form", "Ц-Щ"))
        self.pushButton_8.setText(_translate("Form", "Э-Я"))
        self.label.setText(_translate("Form", "Вы вошли как %USER%"))
        self.pushButton_9.setText(_translate("Form", "Добавить"))
        self.pushButton_10.setText(_translate("Form", "Изменить"))
        self.pushButton_11.setText(_translate("Form", "Удалить"))
