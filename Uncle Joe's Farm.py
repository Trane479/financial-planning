class Animal:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        print('Вы покормили', self.name)


class Cow(Animal):
    def get_milk(self):

        print('Вы взяли молока у', self.name)

    def make_a_sound(self):
        print('Moooooo')


class Goat(Cow):
    def make_a_sound(self):
        print('Ме')


class Sheep(Animal):
    def shear(self):
        print('Вы взяли шерсть у', self.name)

    def make_a_sound(self):
        print('Бе')


class Hen(Animal):
    def get_egg(self):
        print('Вы взяли яйца у', self.name)

    def make_a_sound(self):
        print('Кудах')


class Duck(Hen):
    def make_a_sound(self):
        print('Кря кря')


class Geese(Hen):
    def make_a_sound(self):
        print('Га га га')


geese1 = Geese('Серый', 5)
geese2 = Geese('Белый', 4)
cow = Cow('Манька', 200)
sheep1 = Sheep('Барашек', 80)
sheep2 = Sheep('Кудрявый', 95)
hen1 = Hen('Ко-Ко', 2)
hen2 = Hen('Кукареку', 3)
goat1 = Goat('Рога', 70)
goat2 = Goat('Копыта', 80)
duck1 = Duck('Кряква', 10)


farm = {
    'Feed': [geese1, geese2, cow, sheep1, sheep2, hen1, hen2, goat1, goat2, duck1],
    'Get milk': [cow, goat1, goat2],
    'Get shear': [sheep1, sheep2],
    'Get eggs': [hen1, hen2, duck1, geese1, geese2],
    'Make a sound': [geese1, geese2, cow, sheep1, sheep2, hen1, hen2, goat1, goat2, duck1]
}


def main():
    max_weight = 0
    sum_weight = 0
    for animal in farm['Feed']:
        sum_weight += animal.weight
        if animal.weight >= max_weight:
            max_weight = animal.weight
            max_weight_name = animal.name
    print(f'Больше всех весит {max_weight_name} - {max_weight}кг.')
    print(f'Общий вес всех животных на ферме {sum_weight}кг.')
    command = input('Что вы хотите сделать?\n').lower()

    if command == 'f':
        print('Кого хотите покормить?')

        for animals in farm['Feed']:
            print(animals.name)
        name = input()
        for animals in farm['Feed']:
            if name == animals.name:
                animals.feed()

    if command == 'gm':
        print('У кого хотите взять молоко?')
        for animals in farm['Get milk']:
            print(animals.name)
        name = input()
        for animals in farm['Get milk']:
            if name == animals.name:
                animals.get_milk()

    if command == 'gs':
        print('У кого хотите взять шерсть?')
        for animals in farm['Get shear']:
            print(animals.name)
        name = input()
        for animals in farm['Get shear']:
            if name == animals.name:
                animals.shear()

    if command == 'ge':
        print('У кого хотите взять яйца?')
        for animals in farm['Get eggs']:
            print(animals.name)
        name = input()
        for animals in farm['Get eggs']:
            if name == animals.name:
                animals.get_egg()

    if command == 'mas':
        print('Кого хотите услышать?')
        for animals in farm['Make a sound']:
            print(animals.name)
        name = input()
        for animals in farm['Make a sound']:
            if name == animals.name:
                animals.make_a_sound()

    if command == 'i':
        print('Список доступных команд:\n'
              'mas - услышать животное\n'
              'ge - взять яйца\n'
              'gs - взять шерсть\n'
              'gm - взять молоко\n'
              'f - покормить животное\n'
              )


main()