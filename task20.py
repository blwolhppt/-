# Найти максимальный элемент списка и элемент, следующий за ним, в двух парадигмах: структурной и функциональной. 
# Показать на примере программного кода основные особенности данных парадигм.

list = [10, 17, 189, 69, 30, 15, 43, 278, 41, 20, 23, 40, 18, 52, 133, 678, 50, 19, 15]

# Структурная парадигма
max_elem = 0
index = 0
for i in range(len(list)):
    if list[i] > max_elem:
        max_elem = list[i]
        index = i

print(f'Максимальный элемент: {max_elem}, индекс: {index}')
if index + 1 == len(list):
    print('Следующего элемента нет')
else:
    print(f'Следующий элемент: {list[index + 1]}, индекс: {index + 1}')


# Функциональная парадигма
def func(list):
    max_elem = max(list)
    index = list.index(max_elem)
    print(f'Максимальный элемент: {max_elem}, индекс: {index}')
    if index + 1 == len(list):
        print('Следующего элемента нет')
    else:
        print(f'Следующий элемент: {list[index + 1]}, индекс: {index + 1}')

func(list)


# написать через reduce
