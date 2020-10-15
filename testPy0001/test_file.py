import unittest
from testPy0001.module02 import cl002


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)

    def test_child_class(self):
        instanceClass002 = cl002()
        print(instanceClass002.int_var)
        self.assertEqual(10, instanceClass002.int_var)


if __name__ == '__main__':
    unittest.main()
