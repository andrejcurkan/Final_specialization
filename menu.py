from registry import AnimalRegistry
from models import Animal

def menu():
    registry = AnimalRegistry()
    while True:
        print("1. Завести новое животное")
        print("2. Определить животное в правильный класс")
        print("3. Увидеть список команд, которые выполняет животное")
        print("4. Обучить животное новым командам")
        print("5. Выйти")

        choice = input("Выберите опцию: ")
        if choice == '1':
            name = input("Введите имя животного: ")
            commands = input("Введите команды животного: ")
            birth_date = input("Введите дату рождения животного (YYYY-MM-DD): ")
            animal = Animal(name, commands, birth_date)
            registry.add_animal(animal)
        elif choice == '2':
            name = input("Введите имя животного: ")
            animal_class = registry.determine_animal_class(name)
            print(f"Животное {name} относится к классу {animal_class}")
        elif choice == '3':
            name = input("Введите имя животного: ")
            commands = registry.get_commands(name)
            print(f"Животное {name} выполняет следующие команды: {commands}")
        elif choice == '4':
            name = input("Введите имя животного: ")
            new_commands = input("Введите новые команды: ")
            registry.train_animal(name, new_commands)
            print(f"Животное {name} обучено новым командам.")
        elif choice == '5':
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите правильный вариант.")

if __name__ == "__main__":
    menu()
