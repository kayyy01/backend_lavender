user_name = input("what is your name ")
age = input("what's your age  ")
fav_color = input("what's your favourite colour  ")


friends_name = input("what are the names of your friends: ")

user = {
    "name": user_name,
    "age" : age,
    "favourite color" : fav_color,    
}

friends_name_list = friends_name.split(",")

print(user)
print("If you want to make a change 'Yes', else type 'No' ")

change = input("do you want to change? ").capitalize()

if change == "Yes":
    User_name = input("what is your name ")
    Age = input("what's your age  ")
    Fav_color = input("what's your favourite colour  ")

    user["age"] = age
    user["Favourite_color"] = Fav_color
    print("updated user", user)
    print("list of friends:", friends_name)

else: 
    print("list of friends", friends_name_list)


# if condition:
#run if-else if there is one condition

#run if-elif-else if there is multiple conditions
