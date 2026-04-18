# str1=['a','b','c','b','a','b','c']
# dic = {}
# for ch in str1:
#     if ch not in dic.keys():
#         dic [ch]=0
#     dic[ch]+=1

# print('aphabet_counting:',dic) 

str1 = ['a','b','c','d','a','b','c']
dic = {}
for ch in str1:
    for ch in str1:
        dic.setdefault(ch,0)
        dic [ch]+= 1
        print (list(dic.item()))

print ('alphabet conting:',dic)