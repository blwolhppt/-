# Реализуйте структуру данных "Стек" на языке программирования по вашему выбору. 
# Необходимо реализовать создание пустого стека, добавление элемента, удаление элемента, 
# отображение всех элементов стека. Желательно использовать ООП.


class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        return ' -> '.join(str(elem) for elem in self.stack)

    def add_element(self, elem):
        return self.stack.append(elem)

    def delete_element(self):
        return self.stack.pop()


stack = Stack()

stack.add_element(2)
stack.add_element(1)
stack.add_element(4)
stack.add_element(3)
print(stack)

stack.delete_element()

print(stack)