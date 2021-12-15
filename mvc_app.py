import sys
from model.model import Model
from controllers.main_ctrl import MainController
from views.main_view import MainView

from PyQt5.QtWidgets import QApplication

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        
        self.controller = MainController()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_()) 