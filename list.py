# score_list = [1 2 4 5 6 7 8]
# score_list [0], score_list [3]

# bst = ['v','jpngkok','ha']
# bts_list [0] 

# score_list = [1, 2, 4, 5, 6, 7, 8]
# print(score_list[0])

# mixed_list = [1, 'hello', 3.14, True]
# print(mixed_list[0], type(mixed_list[0])) # 1 <class 'int'>
# print(mixed_list[1]) # 'hello'
# print(mixed_list[2]) # 3.14
# print(mixed_list[3]) # True

# list = list (range (1, 20  ))
# print (list)

# n_list = [1, 2, 3, 4, 5]
# print (n_list)
# print (len (n_list)) # 
# យើងប្រើ len សម្រាប់ចាប់ធាតុទាំង៥ 

# n_list = [10, 20, 30, 40, 50]
# print(n_list[-1])
# print(n_list[-3])
# print(n_list[-5])

#slicing
# n_list = [10, 20, 30, 40, 50]
# n_list[1:4 ]

# person1 = ['davin',20,2,3,4,5]
# person2 = ['dalin',50,40,5,67,]
# person_list = person1 + person2
# print (person_list)

# a_list = ['a','b','c','d']
# a_list.append('e')
# print (a_list)


# slist = ['davin',178,'jonh',175.7,'jane',176.6]
# print(slist)
# slist.insert (4,"pin")
# slist.insert(5,123.2)
# print (slist) 


# list1 = [11, 22, 33,44 ]
# list1.append ([55,66])
# list1

# n_list = [11,22,33,44,55,66,'daliya',178.4]
# print(n_list)

# n_list.remove(44)
# n_list.remove(22)
# print(n_list)

#.List Methods
#.6.7 the pop method for deleting list Item
# n_list = [10,20,30,70]
# print(n_list)

# n = n_list.pop()

# print('n =', n)        
# print('n_list =', n_list)

#Deleting List Item Using the del Keyword
# bts = ["V","J-hope","Suga","Jungkook"]
# del bts [0]
# bts  

# n_list = [200,700 , 500,300,400]
# a_list = [0,'']

# any(n_list)

#import numpy as np 
# print (np.arange(0.9, 1.1,0.1))


# list1 = [3, 5, 7]
# list2 = [2, 3, 4, 5, 6]

# for j in list2:
#     for i in list1:
#         print(f"{i} * {j} = {i*j}".ljust(12), end="\t")
#     print()

# breads = ["12,45,67"]
# meats = ["67,90,87,90"]
# vegetable = ["78,09,65"]
# sauces = ["89,23,56,78"]
# for b in breads:
#     for m in meats:
#         for v in vegetable:
#             for s in sauces:
#                 print (b+ " + " + m + " + " + v + " + " + s, end = "\t" )

# for i in range (5):
#     print(i)

# r = range(2, 12, 3)
# print(list(r))

# for ch in 'Hello':
#     print(ch)

# st = 'program'
# for ch in st :
#     if ch in ['a','e','i','o','u']:
#         continue
#     print (ch)

# Flow control in loop 
# for i in range (3):
#     if i == 1:
#         continue
#     print ('welcome to everyone!!')
# print ("we're glad to see you")
# i

# #1.2keywork change flow of loop statement 
# i = 0
# while i < 3:

# for i in range (3):
#     print ('welcome to everyone !!') 
#     break 
# print ("We're glad to see you ") 
    
# mixed_list = [100,200,'apple',400]

# print (mixed_list[1] and mixed_list[3])  

# n_list = [11,22,33,44,55,66]
# print (n_list)
# print (len(n_list))

# name = input ("Enter the count number:")

# print (name)
# print (len(name))

# n_list = list(map(int, input("Enter numbers: ").split()))
# print(n_list)

# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)

# name = input("Enter your name: ")

# list_name = ['sokkhen','Rotha','Manith','Thyda','Sokpov','Rottanak','Vannoy']

# # check if name already exists
# if name in list_name:
#     print("Name already in list:", name)
# else:
#     list_name.append("Doctor")
#     print("Added new name:", name)

# print("Full list:", list_name)
# The code snippet `list1 = [3, 5, 7, 8]` and `list2 = [2, 4, 5, 6]` is defining two lists in Python.
# `list1` contains the elements `[3, 5, 7, 8]` and `list2` contains the elements `[2, 4, 5, 6]`.

# list1 = [3,5,7,8]
# list2 = [2,4,5,6]

# for j in list2:
#     for i in list1:
#         print(f"{i} * {j} = {i*j}".ljust(12), end="\t")
#     print()  

# base = int (input("Enter of base:"))
# height = int(input("Enter of height:"))

# c = (base**2 + height**2) **0.5

# print("Hypotenuse =", c)

# n_list = [1,2,3,4,5,6,7,8,9,10]
# even_list = list(filter(lambda x: x % 2==0,n_list))
# print(f"even_list{even_list}")

#upper_list 
# def to_upper(char):
#     return char.upper()
# a_list = ['a','b','c','d','e']

# upper_a_list = list(map(to_upper,a_list))
# print ("upper_list = ", upper_a_list)

a_list = ['sokkhen', 'dego']

upper_list = [name.upper() for name in a_list]

print("Upper list =", upper_list)