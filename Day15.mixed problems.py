#student marks and grade program
m1 = int(input("Enter m1 marks:"))
m2 = int(input("Enter m2 marks:"))
m3 = int(input("Enter m3 marks:"))
m4 = int(input("Enter m4 marks:"))
m5 = int(input("Enter m5 marks:"))
m6 = int(input("Enter m6 marks:"))

Total = m1+m2+m3+m4+m5+m6
Percentage = Total/6

print("Total=", Total)
print("Percentage =", Percentage)

if Percentage >= 90:
    print("Grade:A")
elif Percentage >= 75:
    print("Grade:B")
elif Percentage >= 60:
    print("Grade:C")
elif Percentage >= 50:
    print("Grade:D")
else:
    print("Fail")

#number guessing logic
secret = 30
guess = int(input("Enter your guess:"))
if guess == secret:
    print("Correct! You guessed the number.")
elif guess < secret:
    print("Guess is bigger number.")
else:
    print("Guess is smaller number.")

#simple calculator
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

#prime number in range
for i in range(1,100):
   if i % 2 == 0:
       print(i)

#palindrome numbers in range
for i in range (1,1000):
    if str(i) == str(i)[::-1]:
        print(i)

#armstrong number in range
for num in range(1,501):
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + digit**3
        temp = temp // 10

    if total == num:
        print(num)

#sum of even and odd numbers separately
even = 0
odd = 0

for i in range(1,11):
    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i

print("Even sum =", even)
print("Odd sum =", odd)