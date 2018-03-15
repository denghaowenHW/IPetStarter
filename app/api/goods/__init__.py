from app.api.goods.resource import ns
from app.api.goods import schemas


def init_module(api):
    _add_module(ns)
    api.add_namespace(ns)


def _add_module(namespace):
    for name in schemas.__all__:
        model = getattr(schemas, name)
        namespace.add_model(model.name, model)
