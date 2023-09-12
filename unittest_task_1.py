import unittest

from spam_task_1 import task_1


class TestUniquString(unittest.TestCase):

    def test_latin_letters(self):
        self.assertEqual(task_1("srrh rtthety hh"),[121, 116, 115, 114, 104, 101, 32])

    def test_cyrillic_letters(self):
        self.assertEqual(task_1("фвлрп"), [1092, 1088, 1087, 1083, 1074])



if __name__ == '__main__':
    unittest.main()