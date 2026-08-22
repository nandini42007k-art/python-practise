#print 1-10
i = 1
while i<=10:
    print(i)
    i += 1

#print even numbers
i = 2
while i<=20:
    print(i)
    i+=2

#print odd numbers
i = 1
while i<=50:
    print(i)
    i += 2

#sum 1-N
n = int(input("enter number:"))
i = 1
sum = 0
while i <= n:
    sum = sum + i
    i += 1
print("Sum =", sum)

#countdown 10-1
i = 10
while i>=1:
    print(i)
    i -= 1

#multiplication table
i = 0
while i<=10:
    print(f"2*{i}={2*i}")
    i += 1

#factorial
num = int(input("Enter number:"))
fact = 1
while 1<=num:
    fact = fact*num
    num -= 1
print("Factorial=", fact)

#count digits
num = int(input("Enter number:"))
fact = 1
while 1<=num:
    sum = sum + num
    num -= 1
print("Sum=", sum)