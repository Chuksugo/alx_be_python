# library_management.py

class Book:
    """Class to represent a book in the library."""
    
    def __init__(self, title: str, author: str):
        self.title = title         # Public attribute
        self.author = author       # Public attribute
        self._is_checked_out = False  # Private attribute

    def check_out(self):
        """Check out the book, marking it as unavailable."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Return the book, marking it as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out

    def __str__(self):
        """String representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """Class to represent a library containing a collection of books."""
    
    def __init__(self):
        self._books = []  # Private list to store books

    def add_book(self, book: Book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title: str):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out '{title}'.")
                    return True
                else:
                    print(f"'{title}' is already checked out.")
                    return False
        print(f"'{title}' not found in the library.")
        return False

    def return_book(self, title: str):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned '{title}'.")
                    return True
                else:
                    print(f"'{title}' was not checked out.")
                    return False
        print(f"'{title}' not found in the library.")
        return False

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No available books.")
