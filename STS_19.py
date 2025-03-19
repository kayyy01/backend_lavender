#classes
#python is an object oriented programming language
#classes is a blueprint(a structure of how an object should look like) for creating objects
# objects are created from classes

# class Person:
#     name = " "
#     age = " "
#     gender = " "
#     #you can define a function inside a class and this is called a method
#     def speak(self):
#         print(f"My name is {self.name}")

#     def getAge(self,number):
#         print(self.age + number)  



# person1 = Person()
# person1.name = "Mina"
# person1.age = 18
# person1.gender = "female"

# person2 = Person()
# person2.name = "Sam"
# person2.age = 18
# person2.gender = "female"

# person3 = Person() #even though there are 3 different people, they all wiil have a name, age and gender annd can be different.
# person3.name = "Akua "
# person3.age = 18
# person3.gender = "female"

    

# class Animal:
#     name = " "
#     age = " "
#     legs = ""
#     tail = False

# goat = Animal()
# goat.name = "goat"
# goat.legs = 4
# goat.tail = True

#the idea is to consolidate x'tics
#create a structure that allows to replicate easily

#name classes with capital letters.

    


# print(person2.name)


# class Person:
#     #init method. basically a constructor
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender


# person1 = Person("Mina", 18, "female")
# print(person1.name)


# class Student:
#     name = ""
#     age = ""
#     programme = ""
#     level = ""

# class Programme:
#     name = ""
#     department = ""

# Process_plan = Programme()

# student1 = Student()
# student1.programme = Process_plan



class Student:
    def __init__(self, name = "", age = 0, program = None, level = "100"):
        self.name = name
        self.age = age
        self.program = program
        self.level = level
    
    
    
student1 = Student(name ="enoch",age = 12, program =None,level = "200")        
print(vars(student1))
