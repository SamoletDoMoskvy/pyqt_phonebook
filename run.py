from PyQt5 import QtWidgets

from log_window import Ui_MainWindow, RegistrationDialog, RestorePasswordDialog
from book_window import Ui_Form

import sys


class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.forgButton.clicked.connect(self.openForgotPasswordDialog)
        self.ui.regButton.clicked.connect(self.openRegistrationDialog)
        self.ui.loginButton.clicked.connect(self.continueAsUser)

    def openRegistrationDialog(self):
        dialog = RegistrationDialog(self)
        dialog.exec()

    def openForgotPasswordDialog(self):
        dialog = RestorePasswordDialog(self)
        dialog.exec()

    # TODO: Add login
    def continueAsUser(self):
        app.showWorkingUI()


class WorkingWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(WorkingWindow, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)


class Application:
    def __init__(self):
        self.app = QtWidgets.QApplication([])
        self.application = LoginWindow()

    def showLoginUI(self):
        self.application.show()
        sys.exit(self.app.exec())

    def showWorkingUI(self):
        self.application.destroy()
        self.application = WorkingWindow()
        self.application.show()


if __name__ == '__main__':
    app = Application()
    app.showLoginUI()
