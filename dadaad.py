class Book:
    def __init__(self, title, author, year, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available
    
    def __str__(self):
        return f"Книга: '{self.title}' автор {self.author}, {self.year}. Доступна: {self.available}"

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
    
    def __str__(self):
        return f"Пользователь: {self.name} (ID: {self.user_id})"

class Library:
    def __init__(self):
        self.books = []
        self.users = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def add_user(self, user):
        self.users.append(user)
    
    def borrow_book(self, user_id, book_title):
        user = next((u for u in self.users if u.user_id == user_id), None)
        if not user:
            return "Пользователь не найден."


        book = next((b for b in self.books if b.title == book_title), None)
        if not book:
            return "Книга не найдена."
        
        if book.available:
            book.available = False
            return f"{user.name} взял книгу '{book_title}'."
        else:
            return f"Книга '{book_title}' в данный момент недоступна."
    
    def return_book(self, user_id, book_title):
        user = next((u for u in self.users if u.user_id == user_id), None)
        if not user:
            return "Пользователь не найден."
        book = next((b for b in self.books if b.title == book_title), None)
        if not book:
            return "Книга не найдена."
        
        if not book.available:
            book.available = True
            return f"{user.name} вернул книгу '{book_title}'."
        else:
            return f"Книга '{book_title}' не была взята."
    
    def list_available_books(self):
        available_books = [book for book in self.books if book.available]
        if available_books:
            return "\n".join(f"{index + 1}. {book}" for index, book in enumerate(available_books))
        else:
            return "В данный момент нет доступных книг."
    
    def user_interface(self, user_id):
        user = next((u for u in self.users if u.user_id == user_id), None)
        if not user:
            return "Пользователь не найден."

        print(f"Добро пожаловать, {user.name}!")
        
        while True:
            print("\nДоступные действия:")
            print("1. Список доступных книг")
            print("2. Взять книгу")
            print("3. Вернуть книгу")
            print("4. Выйти")

            action = input("Выберите действие (1-4): ")

            if action == "1":
                print("\nСписок доступных книг:")
                print(self.list_available_books())

            elif action == "2":
                book_title = input("\nВведите название книги, которую хотите взять: ")
                print(self.borrow_book(user_id, book_title))

            elif action == "3":
                book_title = input("\nВведите название книги, которую хотите вернуть: ")
                print(self.return_book(user_id, book_title))

            elif action == "4":
                print("До свидания!")
                break
            else:
                print("Неверный выбор, попробуйте снова.")


book1 = Book("1984", "Я впервые вижу", 1949)
book2 = Book("Как сказать нет", "Хз кто на книге не написано", 1960)

user1 = User("Кто это?", 1)
user2 = User("Я не могу понять кто он такой", 2)

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_user(user1)
library.add_user(user2)
library.user_interface(1)  
