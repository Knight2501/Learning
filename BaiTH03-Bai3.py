#3. Tìm phần tử lớn nhất
n = int(input("Nhap so:"))
lst = []
for i in range(n):
    lst.append(int(input()))
    max_value = max(lst)

for v in lst:
    if v == max_value:
        print("phan tu lon nhat trong list:",max_value)