from armadillo.controllers import LineEditController

def bind(model, view):
    controllers = []
    for child in traverse(view):
        bind_target = getattr(child, "bind", None)
        if bind_target is None:
            continue

        try:
            getattr(model, bind_target)
        except AttributeError:
            print("model does not contain bind target {}".format(bind_target))

        controllers.append(LineEditController(model, bind_target, child))
    return controllers


def traverse(node):
    for child in node.children:
        yield child
        yield from traverse(child)
