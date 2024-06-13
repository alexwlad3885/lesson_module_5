"""
Дополнительное практическое задание по модулю: "Классы и объекты."

Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности.

Задание "Свой YouTube":

Университет Urban подумывает о создании своей платформы, где будут размещаться дополнительные
полезные ролики на тему IT (юмористические, интервью и т.д.). Конечно же для старта написания интернет
ресурса требуются хотя бы базовые знания программирования.
Именно вам выпала возможность продемонстрировать их, написав небольшой набор классов, которые будут
выполнять похожий функционал на сайте.

Всего будет 3 класса: UrTube, Video, User.

Общее ТЗ:
Реализовать классы для взаимодействия с платоформой, каждый из которых будет содержать методы
добавления видео, авторизации и регистрации пользователя и т.д.

"""
import hashlib

global current_user
class User:
    """
    Класс пользователей
    атрибуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
    """

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        self.data = {}

    def register(self, nickname, password, age):
        """
        функция регистрации пользователей
        :param nickname: имя (ник) пользователя
        :param password: пароль
        :param age: возраст пользователя
        :return: запись данных в словарь user_base
        """
        self.data[nickname] = password, age
        print('регистрация прошла')

    def log_in(self, login, password):
        global current_user
        if login in self.data and password == self.data.setdefault(login, None)[0]:
            current_user = login
            print("log_in прошел ", current_user)
            return True, current_user
        else:
            # Сброс на начало
            return False, print("Ваш логин или пароль не соответствует.\nПопробуйте еще раз...")

    def log_out(self, nickname, password, age):
        nickname = None
        password = None
        age = None
        return nickname, password, age


    def hash_password(self, password):
        """
        функция хеширования пароля алгоритмом sha3_256
        :param password: первичный пароль пользователя
        :return: хешированный пароль пользователя
        """

        hashed_password = hashlib.sha3_256(password.encode()).hexdigest()
        return hashed_password

    def check_password(self, password_hash, user_password_2):
        """
        Функция проверки пароля
        :param password_hash: хешированный пароль пользователя
        :param user_password_2: пароль пользователя введенный повторно
        :return: True - если пароли совпали
        """
        input_password_hash = hashlib.sha3_256(user_password_2.encode()).hexdigest()
        return input_password_hash == password_hash



class Video:
    """
    Класс видео
    атрибуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки
             (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
    """

    def __init__(self, title, duration, adult_mode, bool):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode
        self.bool = False


class UrTube:
    """
    Класс платформы размещения видеороликов
    Атрибуты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
    """

    def __init__(self, users, videos, current_user_):
        self.users: list = []
        self.videos = videos
        self.current_user = current_user_

    def __add__(self, other):
        return print('добро пожаловать в UrTube')




if __name__ == '__main__':
    ur = UrTube(None, None, None)
    user_base = User(None, None, None)

    while True:
        # обнуление переменных для следующего цикла
        current_user = ""
        user_login = ""
        user_password = ""
        user_password_2 = ""
        password_hash = ""
        user_age = ""

        user_login = input("Введите логин: ")
        if user_login in user_base.data:                            # если логин есть в базе
            print(f'Пользователь ,{user_login}, уже существует')
            user_password = input("Введите пароль: ")
            password_hash = user_base.hash_password(user_password)  # замена простого пароля на хешированный
            # print(user_login)
            # print(password_hash)
            # print(user_base.log_in(user_login, password_hash))
            if user_base.log_in(user_login, password_hash):            # сравнение логина и пароля с базой
                print("Идем дальше")
                user_age = user_base.data.setdefault(user_login, None)[1]
                # ur.__add__()

                # print(user_base.data.setdefault(user_login, None)[0])
                # print(user_base.data.setdefault(user_login, None)[1])
                """
                тело программы
                """


            else:
                print(f'{user_login}, Досвидания')
                user_base.log_out(user_login, password_hash, user_age)
                continue
        else:
            print(f'Пользователь ,{user_login}, не найден')         # если логина нет в базе
            user_password = input("Введите пароль: ")
            password_hash = user_base.hash_password(user_password)  # замена простого пароля на хешированный
            user_password_2 = input("Введите пароль еще раз для проверки: ")
            if user_base.check_password(password_hash, user_password_2):    # Проверка на правильность введения пароля
                print('Вы ввели правильный пароль')
                user_age = input("Введите свой возраст: ")
                user_base.register(user_login, password_hash, user_age)  # занесение данных в базу
                if user_base.log_in(user_login, password_hash):
                    print('Пользователь прошел регистрацию')
                    ur.users.append(user_base.data)
                    ur.current_user = current_user
                    print(ur.users)
                    print(ur.current_user)
                    # user_base.log_out(user_login, password_hash, user_age)


                else:
                    print('Пользователь не прошел регистрацию')


                """
                тело программы
                """
            else:
                user_base.log_out(user_login, password_hash, user_age)
                print('Извините, но пароли не совпадают')


            print(user_base.data)
