
# Доработаем задачи 5-6. Создайте класс-фабрику.
#     ○ Класс принимает тип животного (название одного из созданных классов)
#        и параметры для этого типа.
#     ○ Внутри класса создайте экземпляр на основе
#       переданного типа и верните его из класса-фабрики.


class Animals:

    def __init__(self, name):
        self.name = name

    def  animal_name(self):
        return f'Имя: {self.name}'

class Fish(Animals):

    def __init__(self, name, depth):
        super().__init__(name)
        self.depth = depth

    def get_info(self):
        return f'Глубина обитания: {self.name} = {self.depth} m.'

class Birds(Animals):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def get_info(self):
        return f'Размах крыльев: {self.name} = {self.wingspan} sm.'

class Reptiles(Animals):
    def __init__(self, name, length):
        super().__init__(name)
        self.length = length

    def get_info(self):
        return f'Длинна тела: {self.name} = {self.length} m.'

class Cat(Animals):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def get_info(self):
        return f'Порода кошки {self.name} = {self.breed}'


class Dog(Animals):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def get_info(self):
        return f'Порода собаки {self.name} = {self.breed}'

class AnimalsFactory:
    def __init__(self):
        self.animal_classes = {
            'Fish': Fish,
            'Reptiles': Reptiles,
            'Birds': Birds,
            'Cat': Cat,
            'Dog': Dog
        }

    def create_animal(self, animal_type, *args):
        if animal_type not in self.animal_classes:
            raise ValueError("Invalid animal type")

        animal_class = self.animal_classes[animal_type]
        return animal_class(*args)


if __name__ == '__main__':
    factory = AnimalsFactory()

fish = factory.create_animal('Fish', 'Goldfish', 0.3)
bird = factory.create_animal('Birds', 'Parrot', 1)
reptile = factory.create_animal('Reptiles', 'Cobra', 2)
cat = factory.create_animal('Cat', 'Fluffy', 'Persian')
dog = factory.create_animal('Dog', 'Buddy', 'Bigle')


print(fish.get_info())
print(bird.get_info())
print(reptile.get_info())
print(cat.get_info())
print(dog.get_info())