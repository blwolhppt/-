# Создать программу для анализа списка проданных товаров за один день, который содержит названия товаров.
# Программа должна определить три наиболее часто продаваемых товара и вывести их в порядке убывания популярности, 
# указывая количество продаж каждого товара. Для каждого товара в списке должно быть учтено его количество, 
# чтобы точно определить самые популярные товары.

list_product = ['Cucumber', 'Apple', 'Tomato', 'Cucumber','Banana', 'Orange', 'Tomato', 'Apple', 'Cucumber',  'Apple', 'Cucumber', 'Banana', 'Orange', 'Orange', 'Tomato', 'Cucumber', 'Cucumber', 'Tomato', 'Banana', 'Banana', 'Orange', 'Orange', 'Orange', 'Orange', 'Tomato', 'Cucumber', ]
set_product = set(list_product)

dict_product = {}

for elem in set_product:
    dict_product[elem] = list_product.count(elem)


top_products = dict(sorted(dict_product.items(), key=lambda item: item[1], reverse=True))

for i in range(3):
    print(f"{list(top_products)[i]} - {list(top_products.values())[i]}")