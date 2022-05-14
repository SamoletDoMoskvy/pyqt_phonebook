from PyQt5 import QtWidgets, QtCore

from login_ui import Ui_MainWindow, RegistrationDialog, RestorePasswordDialog
from phonebook_ui import Ui_Form, CreateDialog
from db_controller import Controller, RequestsBuffer
from models import setup_db

import sys


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.forgButton.clicked.connect(self.openForgotPasswordDialog)
        self.ui.regButton.clicked.connect(self.openRegistrationDialog)
        self.ui.loginButton.clicked.connect(self.sign_in)

        self.regD = RegistrationDialog()

    def openRegistrationDialog(self):
        dialog = RegistrationDialog(self)
        dialog.exec()

    def openForgotPasswordDialog(self):
        dialog = RestorePasswordDialog(self)
        dialog.exec()

    def sign_in(self):
        login = self.ui.login.text()
        password = self.ui.password.text()
        try:
            if self.ui.cBox_pRem.isChecked():
                session = Controller().sign_in(login=login, password=password, remember_session=True)
            else:
                session = Controller().sign_in(login=login, password=password, remember_session=False)
            if not session:
                self.ui.label.setVisible(True)
                self.ui.password.setText('')
                self.ui.password.update()
            else:
                app.showWorkingUI(session=session)
        except Exception as exc:
            print(exc)


class WorkingWindow(QtWidgets.QMainWindow):
    def __init__(self, session):
        super(WorkingWindow, self).__init__()

        self.session = session

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.label.setText(f"Вы вошли как {session['name']}")
        self.ui.label.update()

        self.ui.createButton.clicked.connect(self.create_notes)
        self.ui.editButton.clicked.connect(self.edit_notes)
        self.ui.deleteButton.clicked.connect(self.delete_notes)
        self.ui.logoutButton.clicked.connect(self.logout)

        self.fill_table()

    def fill_table(self):
        data = Controller().get()
        c = 0
        self.ui.table.setRowCount(len(data))
        self.ui.table.update()

        for d in data:
            self.ui.table.setItem(c, 0, QtWidgets.QTableWidgetItem(f"{d.name}", type=d.id))
            self.ui.table.setItem(c, 1, QtWidgets.QTableWidgetItem(f"{d.phone}", type=d.id))
            self.ui.table.setItem(c, 2, QtWidgets.QTableWidgetItem(f"{d.date}", type=d.id))
            c += 1

        self.ui.table.itemChanged.connect(self.cell_change)

    def cell_change(self, item):
        id = item.type()

        if item.column() == 0:
            name = item.text()
            phone = self.ui.table.item(item.column(), 1).text()
            date = self.ui.table.item(item.column(), 2).text()
        elif item.column() == 1:
            name = self.ui.table.item(item.column(), 0).text()
            phone = item.text()
            date = self.ui.table.item(item.column(), 2).text()
        else:
            name = self.ui.table.item(item.column(), 0).text()
            phone = self.ui.table.item(item.column(), 1).text()
            date = item.text()

        data = RequestCollector(id=id,
                                name=name,
                                phone=phone,
                                date=date)

        data.add_to_buffer(data)

    def logout(self):
        Controller().logout(id=self.session['id'])
        app.showLoginUI(runned=True)

    def create_notes(self):
        dialog = CreateDialog(self)
        dialog.exec()
        self.fill_table()

    def edit_notes(self):
        pass

    def delete_notes(self):
        pass


class RequestCollector:
    def __init__(self, *args, **kwargs):
        self.id = kwargs['id']
        self.name = kwargs['name']
        self.phone = kwargs['phone']
        self.date = kwargs['date']

    @staticmethod
    def add_to_buffer(data):
        return RequestsBuffer().add(data)


class Application:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.ui = None

    def showLoginUI(self, runned=False):
        if not runned:
            self.application = LoginWindow()
            self.application.show()
            try:
                session = Controller().remember_check()
                if not session:
                    pass
                else:
                    app.showWorkingUI(session=session)
            except:
                pass
            sys.exit(self.app.exec())
        else:
            self.application.destroy()
            self.application = LoginWindow()
            self.application.show()

    def showWorkingUI(self, session):
        self.application.destroy()
        self.application = WorkingWindow(session)
        self.application.show()


if __name__ == '__main__':
    app = Application()
    app.showLoginUI()
