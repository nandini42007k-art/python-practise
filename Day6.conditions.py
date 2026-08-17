#check positive/negative
num = int(input("Enter a number:"))
if num < 0:
    print("negative")
else:
    print("positive")

#check positive/negative/zero
num = int(input("Enter a number:"))
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("Zero")

#check even/odd
n = int(input("enter a number:"))
if n%2 == 0:
    print("Even")
else:
    print("Odd")

#check greater of two numbers
a = int(input("Enter firts num:"))
b = int(input("Enter second num:"))
if a > b:
    print(a, "is greater")
else:
    print(b, "is greater")

#check sameller of two numbers
x = 2
y = 4
if x < y:
    print(x, "is smaller")
else:
    print(y, "is samller")

#check whether a number is divisible by 5
a = int(input("Enter number:"))
if a%5==0:
    print(a, "is divisible by 5")
else:
    print(a, "is not divisible by 5")

#check whether a number is divisble by 3 and 5
num = int(input("enter a number:"))
if num%3==0 and num%5==0:
    print(num, "is divisible by 3 and 5")    
else:
    print(num, "is  not divisible by 3 and 5")

#find greatest of 3 numbers
a = int(input("Enter firts number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
if a > b:
    if a > c:
        print(a, "is greater")
    else:
        print(c, "is greater")
else:
    if b > c:
        print(b, "is greater ")
    else:
        print(c, "is greater")