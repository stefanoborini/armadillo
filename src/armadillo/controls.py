from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QLabel, QHBoxLayout, QGroupBox


class Control:
    def __init__(self):
        self._ui = None
        self._children = []

    def init_ui(self):
        pass

    @property
    def children(self):
        return self._children


class View(Control):
    def __init__(self, *children, filename=None, **kwargs):
        super().__init__()

        self._children = children
        self._filename = filename
        self._title = kwargs.get("title")

    def init_ui(self, parent=None):
        if self._filename is not None:
            return uic.loadUi(self._filename)

        if self._title:
            self._ui = QGroupBox()
            self._ui.setTitle(self._title)
        else:
            self._ui = QWidget()
        layout = QVBoxLayout()
        self._ui.setLayout(layout)

        for child in self.children:
            ui = child.init_ui(self._ui)
            layout.addWidget(ui)

        return self._ui


class LineEdit(Control):
    def __init__(self, name, bind=None):
        super().__init__()
        self._name = name
        self._bind = bind

    def init_ui(self, parent):
        self._ui = QWidget(parent=parent)
        layout = QHBoxLayout()
        self._ui.setLayout(layout)

        label = QLabel(parent=self._ui)
        label.setText(self._name)
        layout.addWidget(label)
        line_edit = QLineEdit(parent=self._ui)
        self._line_edit = line_edit
        layout.addWidget(line_edit)

        return self._ui

    @property
    def bind(self):
        return self._bind

