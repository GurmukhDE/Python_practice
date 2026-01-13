
retries = 0

while retries<2:
    print("retrying....")
    retries+=1


#Print numbers from 1 to 10
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
#-------------------------

#Sum of numbers from 1 to N

n = 5
total = 0
i = 1

while i <= n:
    total += i
    i += 1

print(total)

#---------------------------

#Reverse a number
n = 123
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print(rev)

#--------------------------------

#Check palindrome number
n = 121
temp = n
rev = 0

while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10

if n == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#-------------------------------------

#Read numbers until user enters 0

total = 0

while True:
    num = int(input("Enter number: "))
    if num == 0:
        break
    total += num

print("Sum:", total)

#--------------------------------------
#When to use while instead of for?
# Unknown number of iterations
while True:
    password = input("Enter password: ")
    if password == "admin":
        print("Access granted")
        break
