n = int(input())
lst = []
sum = 0
for i in range(n):
    lst.append(int(input()))

for v in lst:
    sum += v

print(sum)