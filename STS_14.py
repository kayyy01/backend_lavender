#functions
# set it up by using the keyword "def"
#your press a button(call the function)
#it follows a set of instructions(execution of code)
#it gets you the coffee(result/output)

#how to write a function
# def function_name():
#      write set of instructions.

#      return the result
# call the function     

#Example 1
# def make_coffee():  #function definition
#     print("making coffee")

# make_coffee()

#Example 2
# parameter == placeholder
# argument == actual value
# def make_coffee(coffee_type):  #function definition
#      print(f"making {coffee_type} coffee")

# make_coffee("latte")
# make_coffee("Capucino")

#example 3
# def make_coffee(coffee_type, milk, sugar):
#      print(f"making {coffee_type} coffee with {milk} milk and {sugar} sugar")
     
     
# make_coffee("latte")

#example 4 
# def make_coffee(coffee_type = None, milk = "whole", sugar =2):
#      if coffee_type == None:
#           coffee_type = ["latte", "cappucino", "espresso"]
#      print(f"making {coffee_type[1]} coffee with {milk} milk and {sugar} sugar")

# make_coffee()

#example 5
#using *args and **kwargs
#*args = non-specific positional arguments
#used when you're not the number of arguments your function will be recieving

# def make_coffee(*args):
#      print(f"making {args[0]} coffee with {args[1]} milk and {args[2]} sugar")

# make_coffee("latte", "whole", 2, "espresso", 5)


def make_coffee(**kwargs):
    print("here is your coffee")
    
    # print(kwargs)
    print(f"making {kwargs['coffee']} coffee with {kwargs['milk']} milk and {kwargs['sugar']} sugar")

     
make_coffee(coffee = "latte", milk = "whole", sugar = 2)

#*agrs:
# for passing positional arguements
#operates as a tuple
#**kwargs 
# for passing keyword arguements
#operates as a dictionary