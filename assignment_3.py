sentence = input("enter a sentence  ")

#Output Sentence Details
print(len(sentence))
print(len(sentence.split(" ")))
print(sentence.split(" ")[0])
print(sentence.split(" ")[-1])

#Modify the sentence
print(sentence.upper())
print(sentence.lower())
print(sentence.replace(" ","-"))


#Indexing & Slicing
print(sentence[0:3])
print(sentence[-3:])
print(sentence[::-1])

