N = int(input())
f = [1, 2, 4, 7]
x = y = 0
if N in f:
    print(-1)
else:
    if N % 10 in [1, 4, 6, 9]:
        x = N // 5 - 1
        y = (N % 5 + 5) // 3
    elif N % 10 in [2, 7]:
        x = N // 5 - 2
        y = (N % 5 + 10) // 3
    else:
        x = N // 5
        y = N % 5 // 3
    print(x+y)





# 1 == 6
# 2 == 12
# 3 == 3
# 4 == 9
# 5 == 5
# 6 == 6
# 7 == 12
# 8 == 8
# 9 == 9
# 10 == 10