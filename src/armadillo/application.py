import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from armadillo.controls import View
from armadillo.databinding import bind


class Application(object):

    def __init__(self):
        self._app = None

    @property
    def central_view(self):
        return View()

    @property
    def model(self):
        return None

    def run(self):
        self._app = QApplication(sys.argv)
        main = QMainWindow()
        central_view = self.central_view
        central_widget = central_view.init_ui(main)
        main.setCentralWidget(central_widget)

        controllers = bind(self.model, central_view)
        print(controllers)
        main.show()

        return self._app.exec_()

