import pytest

from my_module.spam_task_2 import task_2


@pytest.fixture
def integer_input():
    return "42"

@pytest.fixture
def float_input():
    return "3.14"

@pytest.fixture
def negative_float_input():
    return "-7.5"

@pytest.fixture
def lowercase_input():
    return "Hello World"

@pytest.fixture
def uppercase_input():
    return "UPPERCASE"


def test_task_2_integer(integer_input):
    result = task_2(integer_input)
    assert result == 42

def test_task_2_float(float_input):
    result = task_2(float_input)
    assert result == 3.14

def test_task_2_negative_float(negative_float_input):
    result = task_2(negative_float_input)
    assert result == -7.5

def test_task_2_lowercase(lowercase_input):
    result = task_2(lowercase_input)
    assert result == 'hello world'

def test_task_2_uppercase(uppercase_input):
    result = task_2(uppercase_input)
    assert result == 'uppercase'

if __name__ == '__main__':
    pytest.main(['-v'])