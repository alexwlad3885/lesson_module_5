"""
Домашнее задание по уроку "Различие атрибутов класса и экземпляра"

1. Создайте новый проект в PyCharm
2. Запустите созданный проект
Ваша задача:
1. Создайте новый класс Buiding с атрибутом total
2. Создайте инициализатор для класса Buiding, который будет увеличивать атрибут
   количества созданных объектов класса Building total
3. В цикле создайте 40 объектов класса Building и выведите их на экран командой print
4. Полученный код напишите в ответ к домашнему заданию
"""


class Buiding:

    total = 0

    def __init__(self):
        self.name: str
        self.number_of_objects: int = 1
        Buiding.total += self.number_of_objects


list_: list = []  # список объектов

for i in range(1, 41):
    name_ = "buiding" + str(i)  # формирование имени объекта
    bld = Buiding()  # создаем объект класса
    bld.name = name_
    bld.total = Buiding.total
    list_.append(bld)  # добавляем объект класса в список объектов

for bld in list_:
    print('name ', bld.name, '    total ', bld.total)
