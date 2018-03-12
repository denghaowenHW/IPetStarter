from app.api.article.resource import ns
from app.api.article import schemas


def init_module(api):
    _add_module(ns)
    api.add_namespace(ns)


def _add_module(namespace):
    for name in schemas.__all__:
        model = getattr(schemas, name)
        namespace.add_model(model.name, model)
