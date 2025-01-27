sentence = input("enter a sentence  ")

#Output Sentence Details
print(len(sentence)) #shows the total number of characters including spaces
print(len(sentence.split(" "))) #shows the total number of words
print(sentence.split(" ")[0]) #shows the first word
print(sentence.split(" ")[-1]) #shows the last word

#Modify the sentence
print(sentence.upper()) #converts input to uppercase
print(sentence.lower()) #converts input to lowercase
print(sentence.replace(" ","-")) #replaces spaces with hyphens


#Indexing & Slicing
print(sentence[0:3]) #shows the first 3 characters
print(sentence[-3:]) #shows the last 3 characters
print(sentence[::-1]) #reverses the sentence

