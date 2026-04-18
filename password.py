my_id = '00001123'
password = 'python'
String1 = input ("Enter your password: ")
String2 = input ("Re-enter your password: ")

if String1 == my_id and String2 == password:
    print ('Welcome to Python programming.')
elif String1 != my_id :
    print ('Invalid id. Please try again.')
else :
    print ('Invalid password. Please try again.')