# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor: Initializes the attributes of the book."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Prints a message when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation: Returns a user-friendly description of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation: Used for debugging and recreating the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
