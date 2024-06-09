"""
Домашнее задание по уроку "Перегрузка операторов"

1. Создайте новый проект в PyCharm
2. Запустите созданный проект
Ваша задача:
1. Создайте новый класс Building
2. Создайте инициализатор для класса Building, который будет задавать целочисленный атрибут этажности
 self.numberOfFloors и строковый атрибут self.buildingType
3. Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения
4. Полученный код напишите в ответ к домашему заданию

"""


class Building:

    def __init__(self, number, tupe_):
        self.number_of_floors: int = number
        self.building_tupe: str = tupe_

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors and self.building_tupe == other.building_tupe


bld_1 = Building(12, "Модель_1")
bld_2 = Building(12, "Модель_1")
bld_3 = Building(9, "Модель_2")

print(bld_1 == bld_2)
#   здания равны, т.к. кол-во этажей (number_of_floors) и тип здания (building_tupe) равны
print(bld_1 == bld_3)
#   здания не равны, т.к. кол-во этажей (number_of_floors) и тип здания (building_tupe) не равны
