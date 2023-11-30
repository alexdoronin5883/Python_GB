# ------------------------------------------- 1 -----------------------------
"""
📌 Создайте функцию, которая запрашивает числовые данные от
   пользователя до тех пор, пока он не введёт целое или вещественное число.
📌 Обрабатывайте не числовые данные как исключения.
"""

import argparse
import logging

def get_numeric_input():
        try:
            user_input = input("Введите числовое значение: ")
            numeric_value = float(user_input)
            logger.info("Ok! Ввдено верное число!.")
            return numeric_value
        except ValueError:
            logger.error("Ошибка! Введите целое или вещественное число.")

            return

if __name__ == '__main__':
    logging.basicConfig(filename='project1.log', style='{', filemode='a', encoding='utf-8',
                        level=logging.NOTSET)
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description='my')
    parser.add_argument('-n', metavar='n', type=str, default=0, help='номер дня в формате "1"')

    print("Вы ввели:", get_numeric_input())