#print a string
name = "Nandini"
print(name)

#lenght of string
print(len(name))

#convert string to uppercase
print(name.upper())

#covert string to lowercase
print(name.lower())

#find a character using index
print(name[0:5])
print(name[1:7])
print(name[::2])


#print first and last character
print(name[0])
print(name[-1])

#count a character
print(len(name))

#check whether a word exist in a string
print("Nandi" in name)
print("Nandu" in name)

#replace a word in a string
print(name.replace("Nandini", "Nandu"))

#reverse a string without loops
print(name[::-1])