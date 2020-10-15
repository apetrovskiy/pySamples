import unittest


class MyTestCase(unittest.TestCase):
    def test_child_fields(self):
        id = 5
        name = "test 02"
        from child import Child
        child = Child(id, name)
        child.show()
        self.assertEqual(id, child.id)
        self.assertEqual(name, child.name)


if __name__ == '__main__':
    unittest.main()
