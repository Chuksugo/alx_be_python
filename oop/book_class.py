class Book:
    def __init__(self, title, author, year):
        """Constructor to initialize the book's title, author, and year."""
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' created.")

    def __del__(self):
        """Destructor to handle object deletion."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation for users."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation of the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
