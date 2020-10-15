import unittest


class MyTestCase(unittest.TestCase):
    def test_main(self):
        # self.assertEqual("__main__", __name__)
        self.assertEqual("test_module_name", __name__)

    def test_module(self):
        import module01
        self.assertEqual("module01", module01.module_name())


if __name__ == '__main__':
    unittest.main()
