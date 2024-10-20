class Book:
    def __init__(self, title, author):
        """Base class for books"""
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        """Derived class for eBooks"""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{super().__str__()} (eBook, {self.file_size} MB)"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Derived class for print books"""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{super().__str__()} (Print Book, {self.page_count} pages)"

class Library:
    def __init__(self):
        """Library class to manage books"""
        self.books = []

    def add_book(self, book):
        """Add a book to the library"""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library"""
        for book in self.books:
            print(book)

if __name__ == "__main__":
    library = Library()

    book1 = Book("Pride and Prejudice", "Jane Austen")
    book2 = EBook("Snow Crash", "Neal Stephenson", 500)
    book3 = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    library.list_books()

