from traitlets import HasTraits, Unicode


class ApplicationModel(HasTraits):

    name = Unicode("Hello")
