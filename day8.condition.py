#electricity bill category
units = int(input("Enter units: "))

if units <= 100:
    print("Category: Low consumption")
elif units <= 200:
    print("Category: Moderate consumption")
elif units <= 300:
    print("Category: High consumption")
else:
    print("Category: Very high consumption")

#check voting eligibility
age = int(input("Enter your age: "))

if age > 18:
    print(" eligible for voting.")
else:
    print(" not eligible for voting.")

#check driving eligibility
age = int(input("Enter your age: "))

if age > 18:
    print("eligible for driving.")
else:
    print(" not eligible for driving.")

#find absolute value
value = int(input("Enter a value: "))

print("Absolute value =", abs(value))


#check whether two numbers are equal
a = int(input("Enter firts number:"))
b = int(input("Enter second number:"))
if a == b:
    print("True")
else:
    print("False")

#check whether a number is a multiple of another
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
if a % b == 0:
    print("multiple")
else:
    print("not a multiple")

#check triangle validity
a1 = int(input("Enter first angle:"))
a2 = int(input("Enter second angle:"))
a3 = int(input("Enter third angle:"))

if a1 > 0 and a2 > 0 and a3 > 0 and a1+a2+a3 == 180:
    print("Valid")
else:
    print("Not valid")