class Controller:
    pass




class LineEditController(Controller):

    def __init__(self, model, prop_name, control):
        self._model = model
        self._prop_name = prop_name
        self._control = control

        signal = getattr(model, "_signal_"+prop_name+"_changed", None)
        if signal is None:
            raise RuntimeError("Could not find signal on model object")

        signal.connect(self._update_ui)
        control._line_edit.textChanged.connect(self._update_model)

    def _update_ui(self):
        print("update ui")
        self._control.setText(getattr(self._model, self._prop_name))

    def _update_model(self):
        print("update model")
        try:
            self.model = int(self._control._line_edit.text())
        except:
            self._control._line_edit.setStyleSheet("background-color: rgb(236, 200, 200);")
        else:
            self._control._line_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
