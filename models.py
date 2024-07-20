class Animal:
    def __init__(self, name, commands, birth_date):
        self.name = name
        self.commands = commands
        self.birth_date = birth_date

class DomesticAnimal(Animal):
    def __init__(self, name, commands, birth_date):
        super().__init__(name, commands, birth_date)

class Dog(DomesticAnimal):
    pass

class Cat(DomesticAnimal):
    pass

class Hamster(DomesticAnimal):
    pass

class GrazingAnimal(Animal):
    def __init__(self, name, commands, birth_date):
        super().__init__(name, commands, birth_date)

class Horse(GrazingAnimal):
    pass

class Donkey(GrazingAnimal):
    pass

# Верблюдов исключаем, т.к. их перевезли в другой питомник
