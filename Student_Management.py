print("Welcome to the Student Management System!")
student = {
    "name": [],
    "age": [],  
    "grade": [],
    "Course": [],
}

while True:
    print("\nChoose an option:")
    print("1. Add a Student")
    print("2. Remove a Student")
    print("3. View Student")
    print("4. Exit")

    user_input = input("Enter your choice: ")

    # Add a student
    if user_input == "1":
        name = input("Enter the student's name: ")
        age = input("Enter the student's age: ")
        grade = input("Enter the student's grade: ")
        course = input("Enter the student's course: ")

        #add info to the dictionary
        student["name"].append(name)
        student["age"].append(age)
        student["grade"].append(grade)
        student["Course"].append(course)

        print(f"{name} has been added successfully!")
       

    # Remove a student
    elif user_input == "2":
        student_to_remove = input("Enter the name of student you want to remove: ")
        if student_to_remove in student["name"]:
            student["name"].remove(student_to_remove)
            print(f'"{student_to_remove}" has been removed from the library.')
        else:
            print("student not found.")

    # # View all students
    elif user_input == "3":
        if student:
            print("\nList of Student:")
        for i in range(len(student["name"])):
            print(f'Name: {student["name"][i]}, Age: {student["age"][i]}, Grade: {student["grade"][i]}, Course: {student["Course"][i]}')
        

    # # Exit
    elif user_input == "4":
        print("Goodbye!")
        break

    # # Invalid input
    else:
        print("Invalid choice. Please try again.")