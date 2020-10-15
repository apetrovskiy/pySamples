import unittest
from filecontentloader import FileContentLoader


class MyTestCase(unittest.TestCase):
    def test_file_content(self):
        file_content_loader = FileContentLoader("c:/1/test.txt")
        content = file_content_loader.load_all()
        self.assertEqual(content[0], 'STRINGstring\n')
        print(content)


if __name__ == '__main__':
    unittest.main()
