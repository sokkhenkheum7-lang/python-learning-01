# i = 1 
# while i <=9:
#     print ( f" 1 * {i} = {1*i}\t")
#     i+=1

# i = 1
# while i <=9:
#     print ( f" 2 * {i} = {2*i}\t")  
#     i+=1

i = 1  
while i <= 9:
    j = 1  
    while j <= 9:
        print(f"{i} * {j} = {i*j}", end='\t')  
        j += 1
    print() 
    i += 1