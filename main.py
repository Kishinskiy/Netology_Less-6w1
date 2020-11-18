class Animal:
    def __init__(self, name, kind, take, weight = 0.0, sound = ''):
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



sum_weight = 0

# Гуси
goose1 = Animal('Серый', 'гусь', 'яица', 2.3, 'гагочит')
goose2 = Animal("Белый", 'гусь', 'яица', 2.6, 'гагочит')

# Корова
cow = Animal('Манька', 'корова', 'молоко', 600, 'мычит')

# Овцы
sheep1 = Animal('Барашек', 'овца', 'шерсть', 130, 'блеет')
sheep2 = Animal('Кудрявый', 'овца', 'шерсть', 120, 'блеет')

# Куры
chicken1 = Animal('Ко-Ко', 'курица', 'яица', 1.3, 'кудахчет')
chicken2 = Animal('Кукареку', 'курица', 'яица', 1.6,'кудахчет')

# Козы
goat1 = Animal('Рога', 'коза', 'молоко', 140, 'блеет')
goat2 = Animal('Копыта', 'коза', 'молоко', 120, 'блеет')

# Утка
duck = Animal('Кряква', 'утка', 'яица', 1.6, 'крякает')

if __name__ == '__main__':
    max_weight = [0, 0]
    animals = [
        goose1,
        goose2,
        cow,
        sheep1,
        sheep2,
        chicken1,
        chicken2,
        goat1,
        goat2,
        duck]

    for anim in animals:
        anim.eat(3)
        anim.harvest()
        sum_weight += anim.weight
        if max_weight[1] < round(anim.weight, 2):
            max_weight = [anim.kind, round(anim.weight, 2)]

    print(f'общий вес всеж животных: {round(sum_weight, 2)}кг')
    print(f'самый большой вес у {max_weight[0]} = {max_weight[1]}кг')