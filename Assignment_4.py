user_name = input("what is your name?  ")
age = input("what is your age? ")
fav_color = input("what is favourite color? ")

user_info ={
    "name" : user_name,
    "age": age,
    "fav_color": fav_color
}

friends_name = input("what are your friend's name? ").split()
print("this is your info", user_info)
print("this is your friends' info", friends_name)

change = input("do you want to change the info given? Answer 'Yes' or 'No' ").capitalize()

if change == "Yes":
    intake  = input("Select either 1, 2, 3 or 4...  ")
    
    if intake == "1":
        User_name = input("what is your name?  ")
        User_info ={
            "name" : User_name,
            "age": age,
            "fav_color": fav_color
            }

    
        print(User_info)
        print(friends_name)

    elif intake == "2":
        Age = input("what is your age? ")
        User_info ={
            "name" : user_name,
            "age": Age,
            "fav_color": fav_color
            }

    
        print(User_info)
        print(friends_name)


    elif intake == "3":
        Fav_color = input("what is favourite color? ")
        User_info ={
            "name" : user_name,
            "age": age,
            "fav_color": Fav_color
            }

    
        print(User_info)
        print(friends_name)

    elif intake == "4":
        Friends_name = input("what are your friend's name? ").split()
        print(user_info)
        print(Friends_name)

   

else:
    print(user_info)
print(friends_name)



        





    