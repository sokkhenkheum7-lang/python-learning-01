for i in range(3):
    for j in range(3):
        if j == 1:
            break
        num += j
        if i % 2 == 0:
            continue
        num += i
        print(num)