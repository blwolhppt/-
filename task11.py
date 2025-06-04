# Реализуйте алгоритм двоичного поиска в массиве на языке программирования по вашему выбору. 
# Покажите его применимость на массивах разной длины.

def bin_search(mas, num):
    start = 0
    end = len(mas)

    while start <= end:
        middle = (start + end) // 2
        elem = mas[middle]

        if num == elem:
            return middle
        elif num > elem:
            start = middle + 1
        elif num < elem:
            end = middle - 1
    return -1

mas = [21, 23, 120, 242, 258, 260, 260, 350, 351, 413]


print(bin_search(mas, 351))
print(bin_search(mas, 112))