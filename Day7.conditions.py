#find samllest of 3 numbers
a = int(input("Enter first num:"))
b = int(input("Enter second num:"))
c = int(input("Enter third num:"))
if a < b:
    if a < c:
        print(a, "is smaler")
    else:
        print(c, "is smaller")
else:
    if b < c:
        print(b, "is samller")
    else:
        print(c, "is samaller")

#check leap year
year = int(input("Enter year:"))

if year % 4 == 0:
    print(year, "is leap year")
else:
    print(year, "is not leap year")

#check vowel / consonant
ch = input("enter character:")

if ch == 'a' or ch == 'e' or ch == 'i' or ch =='o' or ch == 'u':
    print(ch, "is vowel")
else:
    print(ch, "is consonant")

#check whether character is alphabet
ch = input("Enter character:")

if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
    print(ch, "is alphabet")
else:
    print(ch, "is not alphabet")

#check whether two numbers is between two values
num = int(input("Enter a number:"))
if 1<= num <= 100:
    print(True)
else:
    print(False)

#check pass/fail
m = int(input("Enter marks:")) 
if 20 <= m <= 50:
    print("pass")
else:
    print("fail")

#garde calculator
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
    print("Garde:E")

#simple calculator using if/elif
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
op = input("Enter operator(+,-,*,/):")
if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "/":
    print(a/b)
else:
    print("Invaild operator")



