#find largest element in list
numbers = [10, 20, 30, 40, 50]
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
print("Largest number=", largest)

#find smallest element
numbers = [10, 20, 30, 40, 50]
smallest = numbers[0]
for i in numbers:
    if i < smallest:
        smallest = i
print("Smallest number =", smallest)

#sum of list
l = [1,2,3,4]
sum = 0
for i in l:
     sum = sum + i
print("Sum =", sum)

#count even numbers
num = [24, 30, 55, 17, 99, 47, 4]
count = 0
for i in num:
    if i % 2 == 0:
        count = count + 1
print("Even numbers count=", count)

#count odd numbers
num = [24, 30, 55, 17, 99, 47, 4]
count = 0
for i in num:
    if i % 2 != 0:
        count = count + 1
print("Odd numbers count=", count)

#count positive numbers
n = [-4,-3,-21,0,2,3,4,5,6,7]
count = 0
for i in n:
    if i > 0:
         count = count + 1
print("Positive numbers count =", count )

#search for an element
num = [30, 40, 35, 67, 29]
search = 30
found = False
for i in num:
    if i == search:
        found = True

if found:
    print("element found")
else:
    print("element is not found")

#find duplicates
numbers = [10,20,35,30,20,30,45,60,30,10]
duplicates = []
for i in numbers:
    if numbers.count(i) > 1 and i not in duplicates:
        duplicates.append(i)
print("Duplicates =", duplicates)