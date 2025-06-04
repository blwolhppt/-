# Реализуйте структуру данных "Двусторонняя очередь" на языке программирования по вашему выбору. 
# Необходимо реализовать создание пустой очереди, добавление элемента очереди, удаление элемента, 
# отображение всех элементов очереди. Желательно использовать ООП.

class Deque:
    def __init__(self):
        self.deque = []

    def __str__(self):
        return " <-> ".join(str(elem) for elem in self.deque)

    def add_top(self, elem):
        return self.deque.insert(0, elem)

    def add_back(self, elem):
        self.deque.append(elem)

    def delete_top(self):
        self.deque.pop(0)

    def delete_back(self):
        self.deque.pop()

deque = Deque()
deque.add_back(2)
deque.add_back(4)
deque.add_back(6)
print(deque)
deque.add_top(3)
deque.add_top(1)
print(deque)
deque.delete_top()
print(deque)
deque.delete_back()
print(deque)
