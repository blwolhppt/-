# Гидрометцентр оповестил о снегопаде в г. Москве. Для того, чтобы могли расчистить дороги, следует выяснить, 
# сколько снегоуборочных машин потребуется. Известно, что на каждый сантиметр слоя выпавшего снега требуется 
# 50 снегоуборочных машин и 20 машин для вывоза снега. Помимо этого, следует учитывать загруженность дорог в Москве. 
# На каждый балл загруженности дорог (от 0 до 10 включительно) следует выпускать дополнительно на 5% снегоуборочных машин 
# и машин для вывоза снега. Рассчитать сколько машин потребуется при прогнозируемом количестве осадков и ситуации на 
# дорогах в г. Москве.

# Решите данную задачу в парадигме ООП (объектно-ориентированного программирования). 
# Создать класс с полями: день недели, прогнозируемое количество осадков, пробки, а также метод для расчета 
# необходимого количества машин для уборки в текущий день и метод вывода результатов на экран.

import math

class CarCounter:
    def __init__(self, day, precipitation, traffic):
        self.day = day
        self.precipitation = precipitation
        self.traffic = traffic

    def count_cars(self):
        amount_plowing_cars = self.precipitation * 50
        amount_remowal_cars = self.precipitation * 20

        if self.traffic == 0:
            return amount_plowing_cars, amount_remowal_cars
        else: 
            return math.ceil(amount_plowing_cars*(1.05)**self.traffic), math.ceil(amount_remowal_cars*(1.05)**self.traffic)


day1 = CarCounter('Понедельник', 4, 0)
print(f'{day1.day}: {day1.count_cars()[0]} снегоуборочных машин и {day1.count_cars()[1]} машин для вывоза снега')

day2 = CarCounter('Вторник', 6, 3)
print(f'{day2.day}: {day2.count_cars()[0]} снегоуборочных машин и {day2.count_cars()[1]} машин для вывоза снега')

day3 = CarCounter('Среда', 2, 10)
print(f'{day3.day}: {day3.count_cars()[0]} снегоуборочных машин и {day3.count_cars()[1]} машин для вывоза снега')

day4 = CarCounter('Четверг', 8, 1)
print(f'{day4.day}: {day4.count_cars()[0]} снегоуборочных машин и {day4.count_cars()[1]} машин для вывоза снега')