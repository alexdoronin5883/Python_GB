
# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode
# каждого символа введённой строки отсортированный по убыванию.

def task_1(text: str) -> list[int]:
    """
       This function transforms input data based on certain condition.
       Args:
           text(str): The input data to be transformed.
       Returns:
           list[int]: The transformed data.

       >>> task_1("srrh rtthety hh")
       [121, 116, 115, 114, 104, 101, 32]

       >>> task_1("фвлрп")
       [1092, 1088, 1087, 1083, 1074]

       >>> task_1(1564)
       Traceback (most recent call last):
        ...
       TypeError: 'int' object is not iterable


       """
    return sorted(list(set(map(ord, text))), reverse=True)
# print (func("srrh rtthety hh"))

