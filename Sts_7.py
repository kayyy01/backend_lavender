#error handling. accounts for what the user will do
#try:
#   age = int(input("enter your age "))
#    print(age) 
#except ValueError:
#    print("your age should be a number")
#except NameError:
#    print("you did not enter your age")
#except Exception  as e:
#    print("Error: ",e)        


#######LISTS####
names =["kay","mina","jike"]
#new_names = list(("kay","mambo"))


#names[2] = "yasmin" #replaces mina with yasmin

#insert a name
#names.insert(0,"Charis")

#add items to list. adds item to the end of the list 
#names.append("Eulogia")

#remove an item from the list
#names.remove("ktistis")
#names.pop(0) #removes an item from the list using the index
#names.clear() #removes all items from the list but comes out as empty
#del names #deletes the entire list from the system


#create a copy of the list
#new_names = names.copy()
#new_names = list(names)
#new_names = names[:]

#arrange in order
#names.sort() #case sensitive in that an item starting with caps will be ordered first before the others
names.insert(0,"chief amuzu")
print(names)