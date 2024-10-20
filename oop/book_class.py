class Book:
    def __init__(self, title, author, year):
        """Constructor: Initializes a Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Prints deletion message."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String Representation: Returns a human-readable string."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official Representation: Returns a string to recreate the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

# Example usage  ifor testing)
if __name__ == "__main__":
    book = Book("To Kill a Mockingbird", "Harper Lee", 1960)
    print(book)  # Utilizes __str__
    print(repr(book))  # Utilizes __repr__
    del book  # Utilizes __del__`
