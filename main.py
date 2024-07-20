import os
import subprocess
import shutil
import pymysql

# 1. Создание и заполнение файлов
domestic_animals_content = "Собаки: Лайка, Овчарка\nКошки: Мурка, Барсик\nХомяки: Чарли, Белка"
grazing_animals_content = "Лошади: Мустанг, Пегас\nВерблюды: Камилла, Сара\nОслы: Инокентий, Булат"

with open("Домашние_животные.txt", "w") as f:
    f.write(domestic_animals_content)

with open("Вьючные_животные.txt", "w") as f:
    f.write(grazing_animals_content)

# 4. Создание директории (если не существует) и перемещение файлов
if not os.path.exists("animal_files"):
    os.mkdir("animal_files")
else:
    print("Директория animal_files уже существует.")

# Перемещение файлов в директорию
shutil.move("Домашние_животные.txt", "animal_files/")
shutil.move("Вьючные_животные.txt", "animal_files/")

# 3. Переименование файла
old_file = "animal_files/Домашние_животные.txt"
new_file = "animal_files/Друзья_человека.txt"

if os.path.exists(old_file):
    os.rename(old_file, new_file)
else:
    print(f"Файл {old_file} не найден. Переименование невозможно.")

# 7. Вывод истории команд в терминале Ubuntu
# Указать команды для Windows
# Удалить строку для Linux
# subprocess.run(["history"])

# 8. Подключение к MySQL и создание базы данных "Друзья_человека"
try:
    connection = pymysql.connect(host='localhost', user='user', password='password', charset='utf8mb4')
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS Друзья_человека")

    # 9. Создание таблиц с иерархией
    cursor.execute("USE Друзья_человека")

    cursor.execute("DROP TABLE IF EXISTS Domestic_animals")
    cursor.execute("DROP TABLE IF EXISTS Grazing_animals")
    cursor.execute("DROP TABLE IF EXISTS Equidae")
    cursor.execute("DROP TABLE IF EXISTS Young_animals")
    cursor.execute("DROP TABLE IF EXISTS All_animals")

    cursor.execute("""CREATE TABLE Domestic_animals (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        animal_name VARCHAR(255),
                        command VARCHAR(255),
                        birth_date DATE
                    )""")

    cursor.execute("""CREATE TABLE Grazing_animals (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        animal_name VARCHAR(255),
                        command VARCHAR(255),
                        birth_date DATE
                    )""")

    # 10. Заполнение низкоуровневых таблиц данными
    cursor.execute("""INSERT INTO Domestic_animals (animal_name, command, birth_date) 
                        VALUES ('Лайка', 'Сидеть, Лежать', '2019-01-15'),
                               ('Мурка', 'Мяукать, Есть', '2018-03-20')""")

    cursor.execute("""INSERT INTO Grazing_animals (animal_name, command, birth_date) 
                        VALUES ('Мустанг', 'Тянуть плуг, Галопировать', '2017-05-10'),
                               ('Инокентий', 'Таскать груз, Жевать', '2016-07-25')""")

    # 11. Удаление из таблицы верблюдов и объединение таблиц
    cursor.execute("DELETE FROM Grazing_animals WHERE animal_name LIKE '%Верблюд%'")

    cursor.execute("""CREATE TABLE Equidae (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        animal_name VARCHAR(255),
                        command VARCHAR(255),
                        birth_date DATE
                    )""")

    cursor.execute("""INSERT INTO Equidae (animal_name, command, birth_date)
                        SELECT animal_name, command, birth_date FROM Grazing_animals""")

    # 12. Создание новой таблицы "молодые животные"
    cursor.execute("""CREATE TABLE Young_animals AS
                        SELECT * FROM Domestic_animals
                        WHERE birth_date BETWEEN DATE_SUB(NOW(), INTERVAL 3 YEAR) AND DATE_SUB(NOW(), INTERVAL 1 YEAR)""")

    # 13. Объединение всех таблиц в одну
    cursor.execute("""CREATE TABLE All_animals AS
                        (SELECT 'Domestic' AS animal_type, id, animal_name, command, birth_date FROM Domestic_animals)
                        UNION ALL
                        (SELECT 'Grazing' AS animal_type, id, animal_name, command, birth_date FROM Equidae)""")


    # 14. Создание класса с инкапсуляцией методов и наследованием
    class AnimalRegistry:
        def __init__(self):
            self.animals = []

        def add_animal(self, animal):
            self.animals.append(animal)

        def determine_animal_class(self, animal):
            if animal in ['Собаки', 'Кошки', 'Хомяки']:
                return 'Домашние животные'
            elif animal in ['Лошади', 'Верблюды', 'Ослы']:
                return 'Вьючные животные'
            else:
                return 'Неизвестный класс'

        def get_commands(self, animal_name):
            connection = pymysql.connect(host='localhost', user='user', password='password', charset='utf8mb4')
            cursor = connection.cursor()
            animal_class = self.determine_animal_class(animal_name)
            if animal_class == 'Домашние животные':
                cursor.execute("SELECT command FROM Domestic_animals WHERE animal_name = %s", (animal_name,))
            elif animal_class == 'Вьючные животные':
                cursor.execute("SELECT command FROM Equidae WHERE animal_name = %s", (animal_name,))
            else:
                return None
            commands = cursor.fetchone()
            connection.close()
            return commands

        def train_animal(self, animal_name, new_commands):
            connection = pymysql.connect(host='localhost', user='user', password='password', charset='utf8mb4')
            cursor = connection.cursor()
            animal_class = self.determine_animal_class(animal_name)
            if animal_class == 'Домашние животные':
                cursor.execute("UPDATE Domestic_animals SET command = %s WHERE animal_name = %s",
                               (new_commands, animal_name))
            elif animal_class == 'Вьючные животные':
                cursor.execute("UPDATE Equidae SET command = %s WHERE animal_name = %s", (new_commands, animal_name))
            connection.commit()
            connection.close()


    # 15. Создание класса Счетчик с методом add()
    class Counter:
        def __init__(self):
            self.count = 0

        def add(self):
            self.count += 1

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            if exc_type is not None:
                raise RuntimeError("Error occurred in try block")
            else:
                if self.count == 0:
                    raise ValueError("Resource was not used")
                elif self.count > 1:
                    raise ValueError("Resource was not properly closed")
                else:
                    print("Resource was properly used and closed")


    # Пример использования класса Счетчик
    try:
        with Counter() as counter:
            # Завести новое животное
            animal_registry = AnimalRegistry()
            animal_registry.add_animal("Лайка")
            counter.add()

    except Exception as e:
        print(e)

finally:
    if connection:
        connection.close()
