from PyQt5.QtCore import pyqtSignal

from armadillo.controls import LineEdit, View
from armadillo.application import Application
from armadillo.model import Model

MyView = View(
    LineEdit("foo", bind="foo"),
    LineEdit("bar"),
    View(
        LineEdit("Baz"),
        LineEdit("Quuz"),
        title="separate"
    )
)

class MyModel(Model):
    def __init__(self):
        super().__init__()
        self._foo = 5

    @property
    def foo(self):
        return self._foo

    @foo.setter
    def foo(self, value):
        self._foo = value
        self._signal_foo_changed.emit()

    _signal_foo_changed = pyqtSignal()

class MyApplication(Application):
    @property
    def central_view(self):
        return MyView

    @property
    def model(self):
        return MyModel()



app = MyApplication()
app.run()

