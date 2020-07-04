#this program will take a number as the input and prints whether the given number is prime or not.

n = int(input("enter the number.. "))

i = 2
while i<n:
    if n%i == 0:
        print("not prime")
        break
    i=i+1
if i == n:
    print("prime")
