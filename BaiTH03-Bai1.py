#1. Tính tổng phần tử trong list
n = int(input("Nhap so phan tu:"))
lst = []
sum = 0
for i in range(n):
    lst.append(int(input()))

for v in lst:
    sum += v
print("Tong cac phan tu trong list:",sum)