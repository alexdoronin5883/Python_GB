
import argparse
import logging


def quadratic_equations(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        logger.info("Ok! Уравнение имеет два корня.")
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        logger.info("Ok! Уравнение имеет один корень..")
        return -b / (2 * a)
    else:
        logger.warning("Уравнение не имеет корней.")
        return None


if __name__ == '__main__':
    logging.basicConfig(filename='project1.log', style='{', filemode='a', encoding='utf-8',
                        level=logging.NOTSET)
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(description='Solving quadratic equations')
    parser.add_argument('param', metavar='a b c', type=float, nargs=3, help='enter a b c separated by a space')
    args = parser.parse_args()
    print(quadratic_equations(*args.param))


 # python .\logging_2.py 2 -12 10
