import pytest

from spam_task_1 import task_1


@pytest.fixture
def latin_letters_input():
    return "srrh rtthety hh"

@pytest.fixture
def cyrillic_letters_input():
    return "фвлрп"



def test_task_1_latin_letters(latin_letters_input):
    result = task_1(latin_letters_input)
    assert result == [121, 116, 115, 114, 104, 101, 32]

def test_task_1_cyrillic_letters(cyrillic_letters_input):
    result = task_1(cyrillic_letters_input)
    assert result == [1092, 1088, 1087, 1083, 1074]



if __name__ == '__main__':
    pytest.main(['-v'])