# Решите данную задачу в парадигме ООП (объектно-ориентированного программирования). 
# Программа должна вычислять цену билетов в маршрутке для пассажиров разных категорий. 
# Если возраст пассажира до 3-х лет, то ему предоставляется бесплатный проезд. 
# Если возраст пассажира 7–18 лет (школьник), то ему предоставляется скидка 50%. 
# Также пенсионерам предоставляется бесплатный проезд.

# Цена билета также зависит от расстояния, которое проезжает пассажир:
# До 20 км — стоимость 100 руб.;
# От 21 до 100 км — стоимость 150 руб.;
# От 101 до 200 км — стоимость 200 руб.;
# >= 201 км — стоимость 400 руб. 

class Passenger():
    def __init__(self, age, distance):
        self.age = age
        self.distance = distance

    def ticket_price(self):
        if self.distance <= 20:
            price_by_distance = 100
        elif self.distance <= 100:
            price_by_distance = 150
        elif self.distance <= 200:
            price_by_distance = 200
        else:
            price_by_distance = 400
        
        if self.age <= 3 or self.age >= 65:
            return 0
        elif 7 <= self.age <= 18:
            return price_by_distance / 2
        else:
            return price_by_distance   
    
passenger1 = Passenger(3, 150)
print(passenger1.ticket_price())

passenger2 = Passenger(17, 50)
print(passenger2.ticket_price())

passenger3 = Passenger(68, 125)
print(passenger3.ticket_price())

passenger4 = Passenger(32, 102)
print(passenger4.ticket_price())

passenger5 = Passenger(55, 19)
print(passenger5.ticket_price()) 

passenger6 = Passenger(6, 25)
print(passenger6.ticket_price())
        