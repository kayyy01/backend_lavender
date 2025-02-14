#lists use []
# tuples use ()
# sets use {} 

#tuples
#count, index
#use parenthesis 
meds = ("Panadol", "Aspirin", "Acetaminophen", "Vitamin C")
#packing & unpacking
#packing = when you assign values to a variable
# (morningMeds, afternoonMeds, eveningMeds) = meds #unpacking the tuple
# print(morningMeds)

#unpack just one item
# (*rest,eveningMeds) = meds 
# print(eveningMeds)

#unpack two items
# (morningMeds, eveningMeds,*rest) = meds
# print(rest)

(first_med, *others, last_med) = meds
print(others)
# med = list(meds) #convert from tuples into list
# med[2] = "Parcetamol"
# new_med = tuple(med) #converts from tuples into list
# print(new_med)

# ages = (18, 19, 20, 21, 22, 23)
# print(ages.count(20)) #counts the number of times 20 appears in the tuple
# print(ages.index(21)) #finds the index of 21


#Dictionaries
#use curly brackets
#use keys to access values
#use [] to access values
#pairing 2 items together in a key-value pair

#set
#use curly brackets
fruits = {"apple", "banana", "cherry"}

cars = {
    "brand" : "Ford Mustang",
    "electric" : False,
    "year" : 1964,
}
print(cars["brand"])
#can use a mixture of keys and values