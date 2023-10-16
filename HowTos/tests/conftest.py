# content of conftest.py
import smtplib

import pytest
from test_foocompare import Foo
import sys

sys.dont_write_bytecode = True


def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
        return [
            "Comparing Foo instances:",
            f"   vals: {left.val} != {right.val}",
        ]


# @pytest.fixture(scope="module")
@pytest.fixture(scope="session")
def smtp_connection():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)


"""
def determine_scope(fixture_name, config):
    if config.getoption("--keep-containers", None):
        return "session"
    return "function"


@pytest.fixture(scope=determine_scope)
def docker_container():
    yield spawn_container()
"""


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "env(name): mark test to run only on named environment"
    )
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line("markers", "serial")


def pytest_addoption(parser):
    parser.addoption(
        "--stringinput",
        action="append",
        default=[],
        help="list of stringinputs to pass to test functions",
    )
    parser.addoption("--all", action="store_true", help="run all combinations")


def pytest_generate_tests(metafunc):
    if "stringinput" in metafunc.fixturenames:
        metafunc.parametrize("stringinput", metafunc.config.getoption("stringinput"))
    if "param1" in metafunc.fixturenames:
        if metafunc.config.getoption("all"):
            end = 5
        else:
            end = 2
        metafunc.parametrize("param1", range(end))
    if "db" in metafunc.fixturenames:
        metafunc.parametrize("db", ["d1", "d2"], indirect=True)


# def pytest_addoption(parser):
#     parser.addoption("--all", action="store_true", help="run all combinations")


# def pytest_generate_tests(metafunc):
#     if "param1" in metafunc.fixturenames:
#         if metafunc.config.getoption("all"):
#             end = 5
#         else:
#             end = 2
#         metafunc.parametrize("param1", range(end))


# def pytest_generate_tests(metafunc):
#     if "db" in metafunc.fixturenames:
#         metafunc.parametrize("db", ["d1", "d2"], indirect=True)


class DB1:
    "one database object"


class DB2:
    "alternative database object"


@pytest.fixture
def db(request):
    if request.param == "d1":
        return DB1()
    elif request.param == "d2":
        return DB2()
    else:
        raise ValueError("invalid internal test config")


@pytest.fixture(scope="session")
def basemod(request):
    return pytest.importorskip("base")


@pytest.fixture(scope="session", params=["opt1", "opt2"])
def optmod(request):
    return pytest.importorskip(request.param)
