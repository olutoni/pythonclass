# listt = list(range(1, 10))
# print(listt)

for i in range(1, 11):
    if i == 1:
        print(f"{i}st", end=' ')
    elif i == 2:
        print(f"{i}nd", end=' ')
    elif i == 3:
        print(f"{i}rd", end=' ')
    else:
        print(f"{i}th", end=' ')
