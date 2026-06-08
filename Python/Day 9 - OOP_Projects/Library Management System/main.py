# This is the simple library management system that allows users to add books, view books, and search for books by title or author.

class Book:
    id = 1000

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.id = Book.id
        Book.id += 1

    def create_book(self):
        for i in range(1, 999):
            self.id += 1
            return self.id
            
        self.id = {
            "title": self.title,
            "author": self.author,
            "id": self.id
        }
        return self.id
    
    def get_book_info(self):
        return f"Title: {self.title}, Author: {self.author}, ID: {self.id}"
    
class User:
    user_id = 10000
    def __init__(self,name, age):
        self.name = name
        self.age = age
        self.user_id = User.user_id
        User.user_id += 1

    def create_new_user(self):
        for i in range(1, 9999):
            self.user_id += 1
            return self.user_id
        
        self.user_id = {
            "name": self.name,
            "age": self.age,
            "id": self.user_id
        }
        return self.user_id
    
    def get_user(self):
        return f"Name: {self.name}, Age: {self.age}, User Id : {self.user_id}"
    
class Library:
    def __init__(self,books,users):
        self.books = books
        self.users = users
        self.borrowed_books = []

    def add_book(self, book):
        self.books.append(book)

    def view_books(self):
        if len(self.books) == 0 :
            print("There are no any books left")
        for book in self.books:
            print(book.get_book_info())
    
    def borrow_book(self, book_id, user_id):
        for book in self.books:
            if book.id == book_id:
                for user in self.users:
                    if user.user_id == user_id:
                        print(f"{user.name} has borrowed {book.title}")
                        self.borrowed_books.append(book)
                        self.books.remove(book)
                        return
        print("Book or User not found.")

    def return_book(self, book_id, user_id):
        for book in self.borrowed_books:
            if book.id == book_id:
                for user in self.users:
                    if user.user_id == user_id:
                        print(f"{user.name} has returned {book.title}")
                        self.books.append(book)
                        return
        print("Book or User not found.")

    


print("Welcome to AZX Library Management")

books = []
users = []


library = Library(books, users)
while True:
    print("\n1. Library Management")
    print("2. Book Management")
    print("3. User Management")
    print("4. Exit")

    try:
        choice = input("Enter your choice: ")
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == '1':
        while True:
            print("\nLibrary Management")
            print("1. Add Book")
            print("2. View Books")
            print("3. Borrow Book")
            print("4. Return Book")
            print("5. Exit")

            sub_choice = input("Enter your choice: ")

            if sub_choice == '1':
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                book = Book(title, author)
                library.add_book(book)
                print(f"Book '{title}' by {author} added to the library.")
            
            elif sub_choice == '2':
                library.view_books()
            
            elif sub_choice == '3':
                try:
                    book_id = int(input("Enter book ID to borrow: "))
                except ValueError:
                    print("Invalid input. Book ID must be a number.")
                    continue
                try:
                    user_id = int(input("Enter user ID: "))
                except ValueError:
                    print("Invalid input. User ID must be a number.")
                    continue
                library.borrow_book(book_id, user_id)
            
            elif sub_choice == '4':
                try:
                    book_id = int(input("Enter book ID to return: "))
                except ValueError:
                    print("Invalid input. Book ID must be a number.")
                    continue
                try:
                    user_id = int(input("Enter user ID: "))
                except ValueError:
                    print("Invalid input. User ID must be a number.")
                    continue
                library.return_book(book_id, user_id)
        
            elif sub_choice == '5':
                print("Exiting the library management system.")
                break
        
            else:
                print("Invalid choice. Please try again.")

    elif choice == '2':
        while True:
            print("\nBook Management")
            print("1. Add Book")
            print("2. View Books")
            print("3. Exit")

            sub_choice = input("Enter your choice: ")

            if sub_choice == '1':
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                book = Book(title, author)
                library.add_book(book)
                print(f"Book '{title}' by {author} added to the library.")
            
            elif sub_choice == '2':
                library.view_books()
            
            elif sub_choice == '3':
                print("Exiting the book management system.")
                break
        
            else:
                print("Invalid choice. Please try again.")
    
    elif choice == '3':
        while True: 

            print("\nUser Management")
            print("1. Add User")
            print("2. View Users")
            print("3. Exit")

            sub_choice = input("Enter your choice: ")

            if sub_choice == '1':
                name = input("Enter user name: ")
                try:
                    age = int(input("Enter user age: "))
                except ValueError:
                    print("Invalid input. Age must be a number.")
                    continue
                user = User(name, age)
                library.users.append(user)
                print(f"User '{name}' added to the library.")
            
            elif sub_choice == '2':
                for user in library.users:
                    print(user.get_user())
            
            elif sub_choice == '3':
                print("Exiting the user management system.")
                break
        
            else:
                print("Invalid choice. Please try again.")
    
    elif choice == '4':
        print("Exiting the library management system.")
        break