#while loop
#runs a block of code till the condition set is unmet

# num = 10
# while not num >5:
#     print("My number is", num)
#     num -=1
    
#     if num == 15:
#         print("Yayy, I got to 15!")
#         break

#operators 
#and both conditions must be met for the code to run
#or  any one of the conditions is met. have a control when using this
#not if the condition is not true. 

# student = ["Randall", "Mina","Ziah", "Kay"]
# name = input("please enter your name.. ")

# while not name in student:
#     print("Name not found")
#     name = input("please enter the right name: ")

#     if name in student:
#         print("Name found thank you!")
#         break
   
# print("Welcome to the Book Title Library!")
# add_book = []

# while True:
#     print("\nChoose an option:")
#     print("1. Add a Book")
#     print("2. Remove a Book")
#     print("3. View All Books")
#     print("4. Exit")

#     user_input = input("Enter your choice: ")

#     # Add a book
#     if user_input == "1":
#         book = input("Enter the book title: ")
#         add_book.append(book)
#         print(f'"{book}" has been added to the library.')

#     # Remove a book
#     elif user_input == "2":
#         book_to_remove = input("Enter the book title to remove: ")
#         if book_to_remove in add_book:
#             add_book.remove(book_to_remove)
#             print(f'"{book_to_remove}" has been removed from the library.')
#         else:
#             print("Book not found.")

#     # View all books
#     elif user_input == "3":
#         if add_book:
#             print("Books in the Library:")
#             for b in add_book:
#                 print(f"- {b}")
#         else:
#             print("No books in the library.")

#     # Exit
#     elif user_input == "4":
#         print("Goodbye!")
#         break

    # # Invalid input
    # else:
    #     print("Invalid choice. Please try again.")        



print("Welcome to the Book Title Library!")
add_book = []

while True:
    print("\nChoose an option:")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. View All Books")
    print("4. Exit")

    user_input = input("Enter your choice: ")

    # Add a book
    if user_input == "1":
        book = input("Enter the book title: ")
        add_book.append(book)
        print(f'"{book}" has been added to the library.')

    # Remove a book
    elif user_input == "2":
        book_to_remove = input("Enter the book title to remove: ")
        if book_to_remove in add_book:
            add_book.remove(book_to_remove)
            print(f'"{book_to_remove}" has been removed from the library.')
        else:
            print("Book not found.")

    # View all books
    elif user_input == "3":
        if add_book:
            print("Books in the Library:")
            for b in add_book:
                print(f"- {b}")
        else:
            print("No books in the library.")

    # Exit
    elif user_input == "4":
        print("Goodbye!")
        break

    # Invalid input
    else:
        print("Invalid choice. Please try again.")