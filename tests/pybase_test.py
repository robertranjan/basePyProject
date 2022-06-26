from pybase import __version__
from pybase import app


def test_version():
    assert __version__ == "0.1.0"


def test_os_name():
    assert app.os_name() == "posix"
