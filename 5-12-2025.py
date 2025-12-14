#0093
n = int(input())
ds = []
while n >= 1:
    i = n % 10
    ds.append(i)
    n //= 10
print(max(j for j in ds if j % 2 != 0))

#0094
n = int(input())
ds = []
while n >= 0:
    i % 10
    ds.append(i)
    n //= 10
print(min(j for j in ds if j % 2 == 0))

#0095