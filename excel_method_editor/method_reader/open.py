import pathlib

import xlwings


def open(path: pathlib.Path) -> xlwings.Sheet:
    if path.suffix not in [".xlsx", ".xlsm"]:
        raise RuntimeError("Invalid path specified.")

    if len(xlwings.apps) == 0:
        app = xlwings.App(add_book=False)
        return app.books.open(path).sheets["Method"]
    else:
        return xlwings.books.open(path).sheets["Method"]
