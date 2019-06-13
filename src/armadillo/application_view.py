import sys
from PyQt5 import sip

from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QMainWindow, QLineEdit
from traitlets import observe, HasTraits, MetaHasTraits

class Meta(sip.wrappertype, MetaHasTraits):
    pass


class ApplicationView(HasTraits):
    def __init__(self, model, parent=None):
        super().__init__()
        self.model = model

    def _update_name(self, val):
        self.label.setText(val["new"].upper())

    def show(self):
        self.app = QApplication(sys.argv)
        self.main = QMainWindow()
        self.label = QLineEdit(parent=self.main)
        self.label.setText(self.model.name)
        self.main.setCentralWidget(self.label)
        self.model.observe(self._update_name, ["name"])
        self.label.textChanged.connect(self.sync_name)
        self.main.show()
        return self.app.exec_()

    def sync_name(self, val):
        self.model.name = val
