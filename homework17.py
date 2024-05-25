# Создайте новый класс Buiding
# Создайте инициализатор для класса Buiding, который будет задавать целочисленный атрибут этажности self.numberOfFloors
# и строковый атрибут self.buildingType
# Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения

class Buiding:

    def __init__(self, floor, type_):
        self.numberOfFloors = floor
        self.buildingType = type_

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


house = Buiding(10, "Дом")
house1 = Buiding(5, "Дом")

print(house == house1)
