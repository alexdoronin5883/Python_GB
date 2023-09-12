
def task_2(data):
    """
    This function transforms input data based on certain condition.
    Args:
        data (str): The input data to be transformed.
    Returns:
        int, float, str: The transformed data.

    >>> task_2("42")
    42

    >>> task_2("3.14")
    3.14

    >>> task_2("-7.5")
    -7.5

    >>> task_2("Hello world")
    'hello world'

    >>> task_2("UPPERCASE")
    'uppercase'
    """
    if data.isdecimal():
        result = int(data)
    elif data.replace('.', '', 1).isdecimal():
        result = float(data)
    elif data[0] == '-' and data.replace('-', '', 1).replace('.', '', 1).isdecimal():
        result = float(data)
    elif data != data.lower():
        result = data.lower()
    else:
        result = data.upper()
    return result

# data = input('Введите данные: ')
# result = task_2(data)
# print(f'{result= }')

