#swap two numbers
a = int(input("Enter first num:"))
b = int(input("Enter second num:"))

a,b=b,a
print("After Swaping")
print("a = ", a)
print("b = ", b)

#reverse string
name = "Nandini"
print(name[::-1])

#find largest of 3
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest number is:", largest)

#check even/odd
n = int(input("enter a number:"))
if n%2 == 0:
    print("Even")
else:
    print("Odd")

#check palindrome
for i in range (1,1000):
    if str(i) == str(i)[::-1]:
        print(i)

#find sum of digit
num = int(input("enter a number:"))
sum = 0
while num>0:
    digit = num % 10
    sum = sum + digit
    num = num//10
print("sum of digit =", sum)

#multiplication tables
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

#find largest in list
numbers = [10, 20, 30, 40, 50]
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
print("Largest number=", largest)

#find samllest in list
b = [45, 79, 65, 35]
smallest = b[0]
for i in b:
    if i < smallest:
        smallest = i
print("Smallest =", smallest)

#remove duplicates
c = [1,2,4,2,3,2,4,5,1,6,3,7,6]
d = []

for i in c:
    if i not in d:
        d.append(i)
print("After removing duplicate =", d)

#count frequency
a = [10, 20, 10, 30, 40, 30, 50]
b = []
for i in a:
    if a not in b:
        count = 0

        for j in a:
            if i == j:
                count = count + 1

        print(i, "=", count)
        b.append(i)

#find second largest
a = [45, 79, 65, 35]     
largest = a[0]
second = a[0]
for i in a:
    if i > largest:
        second = largest
        second = i
    elif i > second and i != largest:
        second = i
    print("Second largest =", largest)

#reverse list
a = ["n", 30, 4, "a"]
a.reverse()
print(a)

#count vowels
text = input("Enter a string: ")

count = 0

for ch in text:
    if ch in "aeiouAEIOU":
        count = count + 1

print("Number of vowels:", count)

#student grade program
marks = int(input("Enter marks:"))
if marks >=90:
    print("Grade:A")
elif marks >=75:
    print("Grade:B")
elif marks >=60:
    print("Grade:C")
elif marks >=50:
    print("Grade:D")
else:
    print("Fail")

#mini calculator
n1 = int(input("Enter first num:"))
n2 = int(input("Enter second num:"))
operator = input("Enetr operator(+,-,*,/):")

if operator == "+":
    print("Result=", n1+n2)
elif operator == "-":
    print("Result=", n1-n2)
elif operator == "*":
    print("Result=", n1*n2)
elif operator == "/":
    print("Result == n1/n2")
else:
    print("Invalid operator")

