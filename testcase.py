age = 18
print(f"Nam nay toi {age} tuoi")
print(f"Sang nam toi {age + 1} tuoi")

n = 9
for i in range(1, 11):
    mul = n * i
    print(f"{n} x {i} = {mul}")

n = int(input())
sum = 0 
for i in range(1, n + 1):
    sum += i
print(f"Tong cua cac so tu 1 den {n} la: {sum}")