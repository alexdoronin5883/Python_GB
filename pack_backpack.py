# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.



def pack_backpack(things, max_weight):
    possible_things = []
    for thing, weight in things.items():
        if weight <= max_weight:
            possible_things.append(thing)
            max_weight -= weight
    return possible_things

things = {
    'Book1': 1.0,
    'Book2': 1.5,
    'Pen_box': 1.0,
    'Pen': 1.2,
    'Pensil': 0.5,
}
max_weight = 3
print(pack_backpack(things, max_weight))