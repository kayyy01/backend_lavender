# class Car:
#     def __init__(self, make, model, year, color, price): #self = this object
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color
#         self.price = price    


# mark_one = Car("Toyota", "Camry", 2020, "Black", 30000)



class Student:
    school = "slightly techie"
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        print(f"hello , my name is {self.name} and I am {self.age} years old. I am in grade {self.grade}. I attend {self.school} " )    

    def change_grades(self, new_grade):
        self.grade = new_grade
        

s1 = Student("Mina",15,6)
s2 = Student("Devin", 14, 5)

s1.change_grades(8)
s1.introduce()


#static method
#functions being put together under a certain class
def school_rules():
    return "students must be in school by 7:30am"

#classmethod 
def get_school(cls):
    return cls.school

