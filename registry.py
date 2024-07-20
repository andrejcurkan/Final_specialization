import pymysql
from models import Animal

class AnimalRegistry:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def determine_animal_class(self, animal_name):
        connection = pymysql.connect(host='localhost', user='user', password='password', db='Друзья_человека', charset='utf8mb4')
        cursor = connection.cursor()
        cursor.execute("SELECT animal_type FROM All_animals WHERE animal_name = %s", (animal_name,))
        result = cursor.fetchone()
        connection.close()
        if result:
            return result[0]
        else:
            return 'Unknown'

    def get_commands(self, animal_name):
        connection = pymysql.connect(host='localhost', user='user', password='password', db='Друзья_человека', charset='utf8mb4')
        cursor = connection.cursor()
        animal_class = self.determine_animal_class(animal_name)
        cursor.execute(f"SELECT command FROM {animal_class} WHERE animal_name = %s", (animal_name,))
        commands = cursor.fetchone()
        connection.close()
        return commands

    def train_animal(self, animal_name, new_commands):
        connection = pymysql.connect(host='localhost', user='user', password='password', db='Друзья_человека', charset='utf8mb4')
        cursor = connection.cursor()
        animal_class = self.determine_animal_class(animal_name)
        cursor.execute(f"UPDATE {animal_class} SET command = %s WHERE animal_name = %s", (new_commands, animal_name))
        connection.commit()
        connection.close()
