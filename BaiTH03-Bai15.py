#15. Lọc phần tử theo điều kiện
n = int(input("Nhap day so: "))
lst = []
for i in range(n):
    lst.append(int(input()))

for v in lst:
    if v % 2 == 0 and v > 10:
        print("Day so moi la:",v)