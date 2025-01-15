class Book:
    def __init__(self, book_id, title, author, is_borrowed = False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def __str__(self):
        if self.is_borrowed:
            return f"Title: {self.title}, author: {self.author}, ID: {self.book_id} and book alredy borrowed!"
        else:
            return f"Title: {self.title}, author: {self.author}, ID: {self.book_id} and book is not borrowed!"

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return f"You borrowed '{self.title}'"
        return f"'{self.title}' is already borrowed."

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return f"You returned '{self.title}'"
        return f"'{self.title}' was not borrowed."


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        

    def __str__(self):
        return f"{self.name}, id:{self.member_id}"
    
    def borrow_book(self, book_id, library):
        book = library.search_book(book_id)
        if book and not book.is_borrowed:
            book.borrow()  # Call the borrow method of the Book instance
            self.borrowed_books.append(book)
            return f"\n{self.name} successfully borrowed '{book.title}'!"
        elif book and book.is_borrowed:
            return f"\nSorry, the book '{book.title}' is already borrowed."
        else:
            return f"\nSorry {self.name}. The book is not available in the library."

    def return_book(self, book_id, library):
        for book in self.borrowed_books:
            if book.book_id == book_id:
                book.return_book()
                self.borrowed_books.remove(book)
                library.add_book(book)
                return f"\n{self.name} successfully returned '{book.title}'."
        return "\nThe book is not in your borrowed list."
    
    def list_borrowed_books(self):
        if not self.borrowed_books:
            return f"{self.name} has not borrowed any books."
        borrowed_titles = [book.title for book in self.borrowed_books]
        return f"{self.name} has borrowed: " + ", ".join(borrowed_titles)


class Library:
    books = []
    members = []

    @classmethod
    def add_book(cls, book):
        cls.books.append(book)
    
    @classmethod
    def remove_book(cls, book_id):
        book = cls.search_book(book_id)
        if book:
            cls.books.remove(book)
            print(f"We removed '{book.title}' from the library.")
        else:
            print("Book not found in the library.")

    @classmethod
    def register_member(cls, member):
        cls.members.append(member)

    @classmethod
    def search_book(cls, book_id):
        """Search for a book by its ID and return the Book object."""
        for book in cls.books:
            if book.book_id == book_id:
                return book  
        return None  

    @classmethod
    def list_books(cls):
        return [str(book) for book in cls.books]

    @classmethod
    def list_members(cls):
        return [str(member) for member in cls.members]


Library.add_book(Book(1000, "harry potter", "Daniel Pedrozo", False))
Library.add_book(Book(1001, "Alice on never land", "Vitin", False))
Library.add_book(Book(1002, "Romeu and juliet", "pedrin", False))
Library.register_member(Member("vitin", 100))
Library.register_member(Member("Daniel", 101))


print("\n".join(Library.list_books()))
print("\n".join(Library.list_members()))
Library.search_book(1000)
Library.remove_book(1002)

# Access a specific member
vitin = Library.members[0]  # Assuming "vitin" is the first member in the registered list
daniel = Library.members[1]

# Borrow a book using the member instance
print(vitin.borrow_book(1000, Library))  
print(daniel.borrow_book(1002, Library))
print(daniel.borrow_book(1001, Library))

# List all library books
print("\n".join(Library.list_books()))

print(daniel.return_book(1001, Library))

print(daniel.list_borrowed_books())
print(vitin.list_borrowed_books())