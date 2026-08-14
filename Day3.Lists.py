#create a list of 5 numbers
l = [1, 2, 3, 4, 5]
print(l)

#acess the first elements
print(l[0])
print(l[-5])

#acess the last elements
print(l[-1])
print(l[4])

#change an element
l[0] = 0
print(l)

#add an element using append()
l.append(6)
print(l)

#add mupltiple elements using extend()
l.extend([7, 8, 9])
print(l)

#insert an element
l.insert(9, 10)
print(l)

#remove an element
l.remove(0)
print(l)

#sort a list
a = [30, 4, 14, 9]
print(sorted(a))

#reverse a list
a.reverse()
print(a)

#find a length of a list
print(len(l))
print(len(a))