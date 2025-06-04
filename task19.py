# Создайте список, содержащий по 3 объекта каждого класса (базовый класс People с атрибутами имя и возраст), 
# производный класс Worker, имеющий дополнительные атрибуты: должность (post) и зарплата (salary), 
# и производный класс Student, имеющий атрибуты оценки (marks) и текущие изучаемые дисциплины (subjects). 
# Для списка объектов выполните следующее:

# Выведите информацию о каждом человеке с помощью метода info.
# Выведите фамилии тех, кто моложе 30 лет.
# Выведите количество объектов класса Worker, имеющих зарплату ниже среднего.
# Выведите информацию о дисциплинах каждого объекта класса Student.

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f'Имя: {self.name}, Возраст: {self.age}')

class Worker(People):
    def __init__(self, name, age, post, salary):
        super().__init__(name, age)
        self.post = post
        self.salary = salary
    
class Student(People):
    def __init__(self, name, age, marks, subjects):
        super().__init__(name, age)
        self.marks = marks
        self.subjects = subjects

person = People('John', 50)
worker1 = Worker('Ben', 32, 'teacher', 25000)
worker2 = Worker('Alex', 26, 'programmer', 75000)
worker3 = Worker('Marina', 37, 'doctor', 22000)
student1 = Student('Alice', 15, [5, 5, 3, 5, 4], ['emglish', 'biology'])
student2 = Student('Vova', 16, [4, 4, 2, 3, 4], ['history', 'literature'])
student3 = Student('Dima', 13, [3, 5, 4, 5, 4], ['literature', 'emglish'])

list = [person, worker1, worker2, worker3, student1, student2, student3]
for elem in list:
    elem.info()

print("Список людей младше 30:")
for elem in list:
    if elem.age < 30:
        print(elem.name)
        

list_workers = []
for elem in list:
    if type(elem) == Worker:
        list_workers.append(elem.salary)

print("Список людей с зарплатой меньше среднего")
middle_salary  = sum(list_workers)/len(list_workers)

count = 0
for elem in list_workers:
    if elem < middle_salary:
        count += 1

print(count)
    

for elem in list:
    if type(elem) == Student:
        print(f'Дисциплины {elem.name}: {elem.subjects}')