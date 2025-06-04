# Разработайте программу учета книг для небольшой библиотеки. 
# Программа должна позволять добавлять новые книги, удалять старые, искать книги по различным параметрам 
# (например, по автору, названию или году издания). Также программа должна поддерживать функцию вывода списка всех книг, 
# отсортированного по выбранному пользователем критерию. Использовать парадигму объектно-ориентированного программирования.

class Book:
    def __init__(self, name, author, year, genre):
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre
    
    def __str__(self):
        return f'{self.name} {self.author} ({self.year}), {self.genre}'


class Library:
    def __init__(self):
        self.books = []
    
    def __str__(self):
        return '\n'.join([str(book) for book in self.books])
    
    def add_book(self, book):
        self.books.append(book)
    
    def delete_book(self, book):
        if book in self.books:
            self.books.remove(book)
        
    def find_book_name(self, name):
        result = [book for book in self.books if name.lower() in book.name.lower()]
        return result

    def find_book_author(self, author):
        result = [book for book in self.books if author.lower() in book.author.lower()]
        return result

    def find_book_year(self, year):
        result = [book for book in self.books if book.year == year]
        return result

    def find_book_genre(self, genre):
        result = [book for book in self.books if genre.lower() in book.genre.lower()]
        return result

    def sort_books(self, key):
        valid_keys = {
            'name': lambda book: book.name.lower(),
            'author': lambda book: book.author.lower(),
            'year': lambda book: book.year,
            'genre': lambda book: book.genre.lower()
        }

        return sorted(self.books, key=valid_keys[key])

    
        
book1 = Book("Война и мир", "Лев Толстой", 1869, "роман")
book2 = Book("Кэрри", "Стивен Кинг", 1974, "ужасы")
book3 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967, "роман")
book4 = Book("Гарри Поттер и философский камень", "ДЖоан Роулинг", 1997, "фентези")
book5 = Book("Кладбище домашних животных", "Стивен Кинг", 1983, "ужасы")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)


library.delete_book(book1)
print(library)

print("")
res = library.find_book_genre('ужасы')
for book in res:
    print(book)

print("")
res = library.sort_books('year')
for book in res:
    print(book)


    
        


    
        
