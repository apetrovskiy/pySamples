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
