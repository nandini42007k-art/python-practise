#reverse number
num = input("Enter a number:")
reverse = num[::-1]
print(reverse)

#palindrome number
num = (input("Enter a number:"))
if num == num[::-1]:
    print("Palindrome number")
else:
    print("Not palindrome number")

#find sum of digit
num = int(input("enter a number:"))
sum = 0
while num>0:
    digit = num % 10
    sum = sum + digit
    num = num//10
print("sum of digit =", sum)

#find largest digit
a = int(input("enter first digit:"))
b = int(input("enter second digit:"))
c = int(input("enter third digit:"))
if a>b:
    if a>c:
        print(a, "is largest")
    else:
        print(c, "is largest")
else:
    if b>c:
        print(b, "is largest")
    else:
        print(c, "is largest")

#find smallest digit
num = int(input("enter a number:"))
smallest = 9
while num > 0:
    digit = num % 10
    if digit < smallest:
        smallest = digit
    num = num//10
print("Smallest digit:", smallest)

#check armstrong number
num = int(input("enter a 3 digit number:"))
a = num//100
b = (num//10)%10
c = num%10

sum = a**3 + b**3 + c**3
print(sum)

#check prime number
n = int(input("enter a number:"))
count = 0 
for i in range(1, num+1):
    if num % i == 0:
        count = count + 1
if count == 2:
    print("Prime number")
else:
    print("Not prime number")