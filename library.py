print("Welcome to the Book Title Library")
add_book = []

while True:
    print("Choose an option:")
    print("1. Add a book  "
        "2. Remove a book  "
        "3. View a book  "
        "4.Exit"
        )


    user_input = input("Enter your choice(a number) ")

    #add a book
    if user_input == "1":
        book = input("Enter book title separated by a comma ")
        add_book.append(book)
        print(f"{book} has been added to the library")

   
    #remove a book
    elif user_input == "2":
        book_to_remove = input("Enter the book title to remove: ").strip()
        if book_to_remove in add_book:
            add_book.remove(book_to_remove)
            print(f"{book_to_remove} has been removed from the library")

        else:
            print("Book not found")    
            

        

    #view a book
    elif user_input == "3":
        if add_book:
            print("Books in the Library:")
            for i in add_book:
                print(f" {i}")
        else:
            print("No books in the library.")
        
    #exit
    elif user_input == "4":
        print("Goodbye")
        break

    # Invalid input
    else:
        print("Invalid choice. Please try again.")