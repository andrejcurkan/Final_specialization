import pymysql

def create_database():
    connection = pymysql.connect(host='localhost', user='user', password='password', charset='utf8mb4')
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS Друзья_человека")
    connection.close()

def create_tables():
    connection = pymysql.connect(host='localhost', user='user', password='password', db='Друзья_человека', charset='utf8mb4')
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Dog (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        animal_name VARCHAR(255),
                        command VARCHAR(255),
                        birth_date DATE
                    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Cat (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        animal_name VARCHAR(255),
                        command VARCHAR(255),
                        birth_date DATE
                    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Hamster (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        animal_name VARCHAR(255),
                        command VARCHAR(255),
                        birth_date DATE
                    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Horse (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        animal_name VARCHAR(255),
                        command VARCHAR(255),
                        birth_date DATE
                    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Camel (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        animal_name VARCHAR(255),
                        command VARCHAR(255),
                        birth_date DATE
                    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Donkey (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        animal_name VARCHAR(255),
                        command VARCHAR(255),
                        birth_date DATE
                    )""")

    connection.close()

def fill_tables():
    connection = pymysql.connect(host='localhost', user='user', password='password', db='Друзья_человека', charset='utf8mb4')
    cursor = connection.cursor()

    cursor.execute("""INSERT INTO Dog (animal_name, command, birth_date) 
                        VALUES ('Лайка', 'Сидеть, Лежать', '2019-01-15'),
                               ('Шарик', 'Апорт, Голос', '2018-06-21')""")

    cursor.execute("""INSERT INTO Cat (animal_name, command, birth_date) 
                        VALUES ('Мурка', 'Мяукать, Кушать', '2018-03-20'),
                               ('Барсик', 'Кушать, Спать', '2019-09-13')""")

    cursor.execute("""INSERT INTO Hamster (animal_name, command, birth_date) 
                        VALUES ('Чарли', 'Бегать, Кушать', '2019-11-05'),
                               ('Белка', 'Бегать, Прятаться', '2018-12-17')""")

    cursor.execute("""INSERT INTO Horse (animal_name, command, birth_date) 
                        VALUES ('Мустанг', 'Тянуть плуг, Галопировать', '2017-05-10'),
                               ('Буцефал', 'Прыгать, Скакать', '2018-08-19')""")

    cursor.execute("""INSERT INTO Camel (animal_name, command, birth_date) 
                        VALUES ('Камилла', 'Таскать грузы', '2016-07-25'),
                               ('Сара', 'Таскать грузы, Пить воду', '2017-04-22')""")

    cursor.execute("""INSERT INTO Donkey (animal_name, command, birth_date) 
                        VALUES ('Инокентий', 'Таскать груз, Жевать', '2016-07-25'),
                               ('Булат', 'Тянуть телегу, Кричать', '2017-11-05')""")

    connection.commit()
    connection.close()

def delete_camels():
    connection = pymysql.connect(host='localhost', user='user', password='password', db='Друзья_человека', charset='utf8mb4')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Camel")
    connection.commit()
    connection.close()

def combine_horses_and_donkeys():
    connection = pymysql.connect(host='localhost', user='user', password='password', db='Друзья_человека', charset='utf8mb4')
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Equidae (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        animal_name VARCHAR(255),
                        command VARCHAR(255),
                        birth_date DATE
                    )""")

    cursor.execute("""INSERT INTO Equidae (animal_name, command, birth_date)
                        SELECT animal_name, command, birth_date FROM Horse
                        UNION
                        SELECT animal_name, command, birth_date FROM Donkey""")

    connection.commit()
    connection.close()

def create_young_animals_table():
    connection = pymysql.connect(host='localhost', user='user', password='password', db='Друзья_человека', charset='utf8mb4')
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Young_animals AS
                        SELECT *, TIMESTAMPDIFF(MONTH, birth_date, NOW()) AS age_in_months 
                        FROM (
                            SELECT * FROM Dog
                            UNION
                            SELECT * FROM Cat
                            UNION
                            SELECT * FROM Hamster
                            UNION
                            SELECT * FROM Equidae
                        ) AS combined
                        WHERE birth_date BETWEEN DATE_SUB(NOW(), INTERVAL 3 YEAR) AND DATE_SUB(NOW(), INTERVAL 1 YEAR)""")

    connection.commit()
    connection.close()

def create_all_animals_table():
    connection = pymysql.connect(host='localhost', user='user', password='password', db='Друзья_человека', charset='utf8mb4')
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS All_animals AS
                        SELECT 'Dog' AS animal_type, id, animal_name, command, birth_date FROM Dog
                        UNION ALL
                        SELECT 'Cat' AS animal_type, id, animal_name, command, birth_date FROM Cat
                        UNION ALL
                        SELECT 'Hamster' AS animal_type, id, animal_name, command, birth_date FROM Hamster
                        UNION ALL
                        SELECT 'Equidae' AS animal_type, id, animal_name, command, birth_date FROM Equidae""")

    connection.commit()
    connection.close()
