#Euclid's algorithm for the greatest common divisor of two numbers.
#Try entering 8 and 12.  The GCD is 4.
a=int(input("Enter A: "))
b=int(input("Enter B: "))
while b != 0:
    if a>b:
        a=a-b
    else:
        b=b-a
print(a)
