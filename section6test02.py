a = int(input("Enter a: "))
b = int(input("Enter b: "))
 
if b == 0:
    print("Cannot divide by zero")
elif a % b == 0:
    print(a, "is a multiple of", b)
else:
    print(a, "is NOT a multiple of", b) 
    