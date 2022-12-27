import ast
import importlib
import os
from enum import Enum
from typing import Iterator

from gotic.models import ReadFileResponse


class FileToDelete(Enum):
    init = "__init__.py"
    pycache = "__pycache__"


def reader(path: str) -> Iterator:

    files = os.listdir(path)

    if FileToDelete.init.value in files:
        files.remove(FileToDelete.init.value)

    if FileToDelete.pycache.value in files:
        files.remove(FileToDelete.pycache.value)

    for file in files:

        with open(file=f"{path}/{file}") as f:
            node = ast.parse(f.read())

        classes_names = [n.name for n in node.body if isinstance(n, ast.ClassDef)]

        file_proccesed = os.path.splitext(file)[0]

        module_path = path.replace("/", ".")
        module = importlib.import_module(name=f"{module_path}.{file_proccesed}")

        classes = [getattr(module, name) for name in classes_names]

        f.close()

        yield ReadFileResponse(filename=file_proccesed, classes=classes)
