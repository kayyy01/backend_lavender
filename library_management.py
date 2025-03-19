# Library management System
#  Design and  implement a Python program to manage a library's collection of books/
# The program should be able to allow user to add a book, remove books, search for a book by title and author
# and display all the books in the library.


# LIBRARY MANAGEMENT SYSTEM
# 1. Add a Book
# 2. Remove a Book
# 3. Search for a Book
# 4. Display All books
# 5. Exit program


# BRAINSTORM


# 1. Welcome page
# 2. Functions to add, remove, search and display books
# 3. storage type Dictionary {}


# Program Flow
# Technical Design
    # Initialize the library
    # Functions to add, remove, search and display books
    # Main program to run the library
# User Interface Design
    # Welcome page
    # Menu options
    # User input
    # Error handling


# Initialize the library


# num = 0
book = {
    "John" : {1: "Harry Potter",
              2: "The Hobbit"
              },
    "Jane" : {1: "The Alchemist",
              2: "The Bible"
              }
}






#Encapsulation






class Library:
    def __init__(self):
        self.books = {} # Dictionary to store books
   
    def add_book(self, author, title):
        # Add a book
        if author not in self.books:
            self.books[author] = {1: title}
            print(f"{title} has been added to the library")
            print(self.books)
        else:
            num = max(self.books[author].keys()) + 1
            self.books[author][num] = title
            print(f"{title} has been added to the library")
            print(self.books)
   
   








si = Library()
s2 = Library()


print(si.add_book("John","Harry Potter"))
print(si.add_book("John","Fantastic Beasts"))