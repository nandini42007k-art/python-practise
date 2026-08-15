#create a student dictionary
stud = {
    "name" : "Nandini",
    "college" : "ACET",
    "branch" : "AIML"
}
print(stud)

#access a value
print(stud.values())

#add a key-value pair
stud["Roll.no"] = "AI012"
print(stud)

#update
stud["Roll.no"] = "1DI25AI012"
print(stud)

#delet a key
stud.pop("college")
print(stud)

#use keys()
print(stud.keys())

#use values()
print(stud.values())

#use items()
print(stud.items())

#use get()
print(stud.get("name"))

#use update()
stud["roll.no"] = "AI012"
print(stud)
