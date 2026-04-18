# num = int (input ("Enter your number: "))
# if num >=0:
#     if num == 0:
#         print ("It's 0.")
#     else: 
#         print ("It's a positive number.") 
# else: 
#     print ("It's a negative number.") 
num = int (input ("Enter your goal: "))
if num >= 100:
    print ("You have reached your goal.")
elif num >= 50:
    print ("You are halfway to your goal.")
elif num >= 25:
    print ("You are a quarter of the way to your goal.")
else:
    print ("You are just starting out on your goal.")
    