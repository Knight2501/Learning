import math
n = int(input())
for i in range(1, math.sqrt(n) + 1):
    if i * i == n:
        print("Yes")
        break
else:
    print("No")

n = int(input())
for i in range(1, n + 1):
    if i * i >= n:
        print("Yes")
        break
else:
    print("No")




