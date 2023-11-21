import importlib.util
from pathlib import Path
import pytest


@pytest.fixture
def iter_homework():
    def iterator(number, nested=""):
        parent = Path(__file__).parents[1]
        pattern = "homework_%02d" % number
        if not nested:
            pattern += ".py"
        else:
            pattern += f"/{nested}.py"
        homeworks = set(_ for _ in Path.rglob(
            parent, pattern))
        for hwpath in homeworks:
            spec = importlib.util.spec_from_file_location(
                "m", hwpath)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            yield hwpath, module
    return iterator
