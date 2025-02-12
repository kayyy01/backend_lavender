#create a dict
  #use curly brackets
  #allows you store multiple variables in a list
students = {
    "key":"value"
    "name": "kay"
    "age": "18"
}

#list
list = [name, age, gender]

#access
#use index to access items in a list
print(list(0))


#storing data in list becomes difficult when storing a person's info
#this problem can be solved using dictionaries
  print(students("name"))
  print(f'the age is {students("age")}')
  #here we use the key "name" to access the value stored in the dictionary

students = {
  "name" : ["kay", "mina", "jike"],
  "age" : 18
  "gender" : "female"
}  
print(students["name"][1])

#the code below has a list inside a dictionary
# to access the item in the list, say gyau, we need to access the list using the key "name"
#you follow the conventional way of accessing items in a list and then the index of that item in the list

students = {
  "name" : ["kay", "mina", "jike",["gyau","boahen"]],
  "age" : 18
  "gender" : "female"
}  
print(students["name"][3][1])

#looping through a dict
for key, value in students.items():
  print(key, value)


#change items in a dict
names = ["kay","mina","jike"]
names[0] = "Charis" #replace kay with charis

#add items to a dict
students["grade"] = "12"

#remove items from a dict
students.pop("grade")
students["grade"] = ""
