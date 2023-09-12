

import unittest

from my_module.spam_task_2 import task_2


class TestTransforData(unittest.TestCase):

    def test_integer(self):
        self.assertEqual(task_2("42"),42)

    def test_float(self):
        self.assertEqual(task_2("3.14"), 3.14)

    def test_negative_float(self):
        self.assertEqual(task_2("-7.5"), -7.5)

    def test_lowercase_string(self):
        self.assertEqual(task_2("Hello world"), 'hello world')

    def test_uppercase_string(self):
        self.assertEqual(task_2("UPPERCASE"), 'uppercase')

if __name__ == '__main__':
    unittest.main()