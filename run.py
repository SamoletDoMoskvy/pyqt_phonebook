from PyQt5 import QtWidgets

from log_window import Ui_MainWindow, RegistrationDialog, RestorePasswordDialog
from book_window import Ui_Form
from db_controller import Controller
from backend import setup_db

import sys


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.forgButton.clicked.connect(self.openForgotPasswordDialog)
        self.ui.regButton.clicked.connect(self.openRegistrationDialog)
        self.ui.loginButton.clicked.connect(self.signIn)

        self.regD = RegistrationDialog()

    def openRegistrationDialog(self):
        dialog = RegistrationDialog(self)
        dialog.exec()

    def openForgotPasswordDialog(self):
        dialog = RestorePasswordDialog(self)
        dialog.exec()

    def signIn(self):
        login = self.ui.login.text()
        password = self.ui.password.text()
        try:
            session = Controller().signIn(login=login, password=password)
            app.showWorkingUI(session=session)
        except Exception as exc:
            print(exc)


class WorkingWindow(QtWidgets.QMainWindow):
    def __init__(self, session):
        super(WorkingWindow, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.label.setText(f"Вы вошли как {session['name']}")
        self.ui.label.update()

        self.ui.table
        self.ui.table.setItem(0, 0, QtWidgets.QTableWidgetItem("Text in column 1"))


class Application:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.application = LoginWindow()
        self.ui = None

    def showLoginUI(self):
        self.application.show()
        sys.exit(self.app.exec())

    def showWorkingUI(self, session):
        self.application.destroy()
        self.application = WorkingWindow(session)
        self.application.show()


if __name__ == '__main__':
    app = Application()
    app.showLoginUI()
