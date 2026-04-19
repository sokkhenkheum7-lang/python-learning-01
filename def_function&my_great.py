# def max2(m,n):
#     if m > n:
#         return m 
#     else:
#         return n 
# def min2 (m,n):
#     if m<n:
#         return m
#     else:
#         return n

# def my_great ():
#     print("Hello welcome to Python")
    
# my_great()
# my_great()
# my_great()
# my_great()

# def my_great (num):
#     print("hello_nihao")

# my_great(5)
# my_great(10)
# def my_great(num):
#     print("Hello", num)

# for i in range(1, 6):
    
#     my_great(i)

# def my_function(fname):
#     print(fname + "Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# def my_function(fname,lname):
#     print(fname + " " + lname)
    
# my_function("Emil","Refsnes")

# def power (x,n):
#     if n == 0:
#         return 1
#     else:
#         return x*power (x,n-1)
    
# x = int(input("Enter the value x:"))
# n = int(input("Enter the value n :"))

# print ("{}{} = {}".format(x,n,power(x,n)))

def my_function(*kids):
  print("The youngest child is " + kids[3])

my_function("Emil", "Tobias", "Linus","sokkhen")