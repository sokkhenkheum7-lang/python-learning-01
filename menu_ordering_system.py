money = int (int(input ('pls enter your money (ex:1500) >>> ')))
if money < price * count : 
    print ('not enough money')
else : 
    change = money - price * count
print (f'your change is {change} dollars')