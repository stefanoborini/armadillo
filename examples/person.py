class Person(Model):
    name = String()
    age = Int()


PersonView = View(
    V(
        H(Label("Name"), LineEdit(bind="name")),
        H(Label("Age"), LineEdit(bind="age")),
    )
)

model = Person()
view = PersonView(model)

app = Application()
app.central_view = view
app.run()

