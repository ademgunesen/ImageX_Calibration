import sys
from PyQt5.QtWidgets import QApplication

from controllers.main_ctrl import MainController

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)

        self.controller = MainController()

#main
if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())