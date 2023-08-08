#  Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:


from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)
count = 10
while count > 0:
        print('Попытка ' + str(count))
        count -= 1
        user_num = int(input('Введи число между ' + str(LOWER_LIMIT) + ' и ' + str(UPPER_LIMIT) + ': '))
        if num < user_num :
                print('Меньше!')
        elif num > user_num:
                print('Больше!')
        else:
                print('В яблочко!!!!')
                break
else:
        print('Исчерпаны все попытки. Сожалею.')
print('Загаданое число: ' + str(num))
