# content of test_module.py

import conftest
from smtplib import SMTP


def test_ehlo(smtp_connection: SMTP):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert b"smtp.gmail.com" in msg
    assert 0  # for demo purposes


def test_noop(smtp_connection: SMTP):
    response, msg = smtp_connection.noop()
    assert response == 250
    assert 0  # for demo purposes


def test_func1(basemod, optmod):
    assert round(basemod.func1(), 3) == round(optmod.func1(), 3)
