from unittest import TestCase


def setUpModule():
    print("setUpModule")


def tearDownModule():
    print("tearDownModule")


class Class1Test(TestCase):
    @classmethod
    def setUpClass(cls):
        print("    setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("    tearDownClass")

    def setUp(self):
        print("        setUp")

    def tearDown(self):
        print("        tearDown")

    def test_1(self):
        print("          class 1 test 1")

    def test_2(self):
        print("          class 1 test 2")


class Class2Test(TestCase):
    def test_1(self):
        print("          class 2 test 1")
