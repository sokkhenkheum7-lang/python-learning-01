# thistuple = ("banana","apple","cherry","pinapple")
# print (thistuple [0])

# tup = (1,4,6,8,9,3,7)
# temp = list(tup)
# temp.sort()
# print(temp)
# tup1 = (1,1,1,1,2,3,3,4)

# tup = (1,2,3,4)
# 3 in tup

# person = ['sokha','kanha','kanha','borey','sreykroblak']
# print ('I want to meet :',person[len(person)-1])
# print (person.count("kanha"))
# print(person.count('kanha'))
# print (person)

# str = 'hello'
# print(str * 3)
# ran = list(range(5))*3
# print (ran)

# ran = tuple (range(5))*3
# print (ran)

# immutable data type 
# string1 = 'ABC'
# string2 = 'ABC'
# if string1 == string2:
#     print("It's sam.")
#     if string1 is string2:
#         print ("It's same object ")
#     else : 
#         print ("It's deferent Object")
# else :
#     print ("It's different")


# print (id(string1), 'vs.', id(string2))

# t1 = 'a','b','c'
# t2 = ('a','b','c')
# t3 = ('d','e')

# print (t1 == t2)

# print (t1 > t3)

# print (t1 < t3)

# print (t2 + t3)

# print ([t2 + t3])

# print (t1)

# sale_record = (100 , 121 ,120, 130 , 140 , 120, 122, 123, 190, 125)
# i = 1
# count = 0
# while i < len (sale_record):
#         if sale_record[i] < sale_record [i-1]:
#             count += 1
#         i+= 1

# print("In the past 10 days,", count, " days had reduced sales compared to the previous day.")
   

#Let's code in Tuple 
# step 1 

# population_a = (100,150,230,120,180,100,140,95,81,21,4)
# population_b = (300,420,530,420,400,300,40,5,1,1,1)
# # step 2
# oldA = sum (population_a[7:])
# oldB = sum (population_b[7:])
# sumA,sumB = sum (population_a), sum(population_b)

# oldRateA, oldRateB = oldA/sumA,oldB/sumB
# print ('The aging degrees of villages A and B are {:5.3f} and {:5.3f} each.'.format (oldRateA,oldRateB))

# t = (1,2,2,3,4,4,4,4,5,5,5,5,6)

# most = max(set(t), key=t.count)
# print("Most Frequent:", most)

# list = [(),(1,),[],'abc',(),(),(1,)('a',),('a','b'),((),),'']

# result = [x for x in data if x != [] and x != 'n ']

sales_record = (100, 121, 120, 130, 140, 120, 122, 123, 190, 125)

i = 1
count = 0

while i < len(sales_record):
    if sales_record[i] < sales_record[i - 1]:
        count += 1
    i += 1

print("In the past 10 days,", count, "days had reduced sales compared to the previous day.")