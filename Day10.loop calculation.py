#sum of 1-10
sum = 0
for i in range (1,11):
    sum = sum + i
print("Sum =", sum)

#sum of 1-N
sum = 0
n = int(input("Enter N:"))
for i in range(1, n+1):
    print(i)

#sum of even number
sum = 0
for i in range(2,100,2):
    sum = sum + i
    print("Sum =", sum)

#sum of odd number
sum = 0
for i in range(1,20,2):
    sum = sum + i
    print(sum)

#multiplication of tables
for i in range(1,11):
    print(f"2*{i}={i*i}")

#factorial
num = int(input("enter a number:"))
fact = 1
for i in range(1, num+1):
    fact = fact*i
print("Factorial=", fact)

#count numbers
n = int(input("Enter a N:"))
count = 0
for i in range(1, n+1):
    count = count+1
print("Count =", count)

#find largest number
num = [14,9,30,4]
largest = num[0]
for i in num:
    if i > largest:
        largest = i
print("Largest number=", largest)