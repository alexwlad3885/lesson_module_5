"""
Домашнее задание по уроку "Специальные методы классов"

Создайте новый проект в PyCharm
Запустите созданный проект

Ваша задача:
1. Создайте новый класс House
2. Создайте инициализатор для класса House, который будет задавать атрибут этажности self.numberOfFloors = 0
3. Создайте метод setNewNumberOfFloors(floors), который будет изменять атрибут numberOfFloors на параметр floors и
   выводить в консоль numberOfFloors
4. Полученный код напишите в ответ к домашему заданию
"""


class House:

    def __init__(self):
        self.number_of_floors = 0

    def set_new_number_of_floors(self, floors):
        floors: int
        self.number_of_floors += floors
        print(f'numberOfFloors - {self.number_of_floors}')
        print(f'floors - {floors}')
        return self.number_of_floors


h1 = House()
print(f'numberOfFloors - {h1.number_of_floors}')
print(f'setNewNumberOfFloors - {h1.set_new_number_of_floors(6)}')
