import unittest


class MyTestCase(unittest.TestCase):
    def test_base_fields(self):
        id = 3; name = "test"
        from base import Base
        base = Base(id, name)
        base.show()
        self.assertEqual(id, base.id)
        self.assertEqual(name, base.name)


if __name__ == '__main__':
    unittest.main()
