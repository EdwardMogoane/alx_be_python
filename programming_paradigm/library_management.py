class Book:
    """Represents a book with title, author, and checkout status."""
    
    def __init__(self, title, author):
        """Initializes a Book instance."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Marks the book as returned."""
        self._is_checked_out = False

    @property
    def is_available(self):
        """Returns True if the book is available, False otherwise."""
        return not self._is_checked_out

class Library:
    """Manages a collection of books."""
    
    def __init__(self):
        """Initializes a Library instance."""
        self._books = []

    def add_book(self, book):
        """Adds a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.is_available:
                    book.check_out()
                    print(f"{title} checked out successfully.")
                else:
                    print(f"{title} is already checked out.")
                return
        print(f"{title} not found in library.")

    def return_book(self, title):
        """Returns a checked-out book by title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if not book.is_available:
                    book.return_book()
                    print(f"{title} returned successfully.")
                else:
                    print(f"{title} is already available.")
                return
        print(f"{title} not found in library.")

    def list_available_books(self):
        """Lists available books."""
        print("Available books:")
        for book in self._books:
            if book.is_available:
                print(f"{book.title} by {book.author}")
def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()

            
