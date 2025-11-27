#10. Tìm phần tử xuất hiện nhiều nhất
n = input("Nhap chuoi: ")
lst =  [].lower()
count = 0
for i in n:
    lst.append(input())

for v in lst:
    max = lst.count(v)
    if max > count:
        count = max
        chuoi_xuat_hien_nhieu_nhat = v
print(f"Phan tu xuat hien nhieu nhat la '{chuoi_xuat_hien_nhieu_nhat}' voi {count} lan xuat hien.")