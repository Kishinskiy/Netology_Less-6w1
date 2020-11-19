class Animal:
    def __init__(self):
        self.name = name
        self.kind = kind
        self.take = take
        self.weight = weight
        self.sound = sound

    def voice(self):
        return print(f'{self.kind} {self.sound}')

    def eat(self, food):
        self.weight += (0.1 * food)
        return print(f'{self.kind} {self.name} ест')

    def harvest(self):
        return print(f'вы получили {int(self.weight * 1)} {self.take}')


class Goose(Animal):
    def __init__(self, name, weight):
        self.kind = 'Гусь'
        self.name = name
        self.weight = weight
        self.take = 'Яица'
        self.sound = 'гагочит'


class Cow(Animal):
    def __init__(self, name, weight):
        self.kind = 'Корова'
        self.name = name
        self.weight = weight
        self.take = 'Молоко'
        self.sound = 'Мычит'

class Sheep(Animal):
    def __init__(self, name, weight):
        self.kind = 'Овца'
        self.name = name
        self.weight = weight
        self.take = 'Шерсть'
        self.sound = 'Блеет'

class Chicken(Animal):
    def __init__(self, name, weight):
        self.kind = 'Курица'
        self.name = name
        self.weight = weight
        self.take = 'Яица'
        self.sound = 'Кудахчет'

class Goat(Animal):
    def __init__(self, name, weight):
        self.kind = 'Коза'
        self.name = name
        self.weight = weight
        self.take = 'Молоко'
        self.sound = 'Блеет'

class Duck(Animal):
    def __init__(self, name, weight):
        self.kind = 'Утка'
        self.name = name
        self.weight = weight
        self.take = 'Яица'
        self.sound = 'Крякает'




# Гуси
seriy = Goose('Серый', 2.3)
beliy = Goose('Белый', 2.6)

# Корова
manka = Cow('Манька', 600)

# Овцы
barashek = Sheep('Барашек', 130)
kudriyaviy = Sheep('Кудрявый', 120)

# # Куры
koko=Chicken('Ко-Ко', 1.3)
kukareku = Chicken('Кукареку', 1.6)

# # Козы
roga = Goat('Рога', 140)
kopiyta = Goat('Копыта', 120)

# # Утка
kriyakva = Duck('Кряква', 1.6)


if __name__ == '__main__':
    sum_weight = 0
    max_weight = [0, 0]
    animals = [
        seriy,
        beliy,
        manka,
        barashek,
        kudriyaviy,
        koko,
        kukareku,
        roga,
        kopiyta,
        kriyakva]

    for anim in animals:
        anim.eat(3)
        anim.harvest()
        sum_weight += anim.weight
        if max_weight[1] < round(anim.weight, 2):
            max_weight = [anim.kind, round(anim.weight, 2)]

    print(f'общий вес всеж животных: {round(sum_weight, 2)}кг')
    print(f'самый большой вес у {max_weight[0]} = {max_weight[1]}кг')
