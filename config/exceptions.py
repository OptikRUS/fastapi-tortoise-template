from importlib import import_module


def get_exceptions() -> list[Exception]:

    modules: list[import_module] = [
        import_module('users.exceptions'),
    ]

    exceptions = list[Exception]
    for module in modules:
        exceptions = [
            exception_cls for exception_cls in (getattr(module, name) for name in dir(module))
            if isinstance(exception_cls, type) and getattr(exception_cls, '__module__', None) == module.__name__
        ]

    return exceptions
