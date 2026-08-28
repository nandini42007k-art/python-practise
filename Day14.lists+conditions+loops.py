#reverse a lists
num = [100,30,70,20,40,90]
num.reverse()
print(num)

#find second largest
a = [10, 20, 4, 45, 99]
largest = a[0]
second = a[0]

for i in a:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i
print("Second largest=", second)


#find second smallest
a = [10, 20, 4, 45, 99]
smallest = a[0]
second = a[0]

for i in a:
    if i < smallest:
        second = smallest
        smallest = i
    elif i < smallest and i != smallest:
        second = i
print("Second smallest=", second)

#remove duplicate
a = [5,2,5,8,2,9]
b =[]

for i in a:
    if i not in b:
        b.append(i)
print("after removing duplicates:", b)

#count frequency of each element
a = [10, 20, 10, 30, 20, 10]
b = []

for i in a:
    if i not in b:
        count = 0

        for j in a:
           if i == j:
               count = count + 1

        print(i, "=", count)
        b.append(i)

#separate even and odd numbers
num = [100, 30, 70, 20, 40, 90]
even = []
odd = []
for i in num:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even numbers:", even)
print("Odd numbers:", odd)