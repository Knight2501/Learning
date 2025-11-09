#Bài 1: Đếm ký tự và chiều dài chuỗi
n = input("Nhap chuoi cua ban: ")
print("Do dai cua chuoi la: ",len(n))
for i in n:
    print(f"{i} xuat hien trong {n.count(i)} lan")

#Bài 2: Kiểm tra chuỗi đối xứng (Palindrome)
n = input("Nhap chuoi cua ban: ")
m = ''.join(reversed(n))
if m == n:
    print("Cau truc nay doi xung")
else:
    print("Cau truc nay khong doi xung")

#Bài 3: Đếm số nguyên âm và phụ âm trong chuỗi
n = input("Nhap mot chuoi tieng anh: ")
n = n.lower()
nguyen_am = "aeiou"
count_phu_am = 0
count_nguyen_am = 0
for char in n:
    if char.isalpha():
        if char in nguyen_am:
            count_nguyen_am += 1
        else:
            count_phu_am += 1
print("So nguyen am:", count_nguyen_am)
print("So phu am:", count_phu_am)

#Bài 4: Viết hoa chữ cái đầu mỗi từ
n = input("Nhap chuoi cua ban: ")
print(n.title())

#Bài 5: Thay thế từ trong chuỗi
n = input("Nhap chuoi cua ban: ")
m = "Python"
count = n.split().count(m)
print(n.replace("Python","AI"))

#Bài 6: Tách và nối chuỗi
n = input("Nhap chuoi cua ban: ")
m = n.split(" ")
y = "-".join(m)
print(y)

#Bài 7: Đếm số từ trong câu
n = input("Nhap cau: ")
m = len(n.split())
print(f"So tu trong {n} la {m}")

#Bài 8: Tổng, trung bình và phần tử lớn nhất
n = input("Nhap day so cua ban: ")
m = n.split()
y = list(map(int, m))
tong = sum(y)
print("Tong cua day so nay la: ",tong)
trung_binh = tong / len(m)
print("Trung binh cua day so nay la: ",trung_binh)
so_lon_nhat = max(y)
print(f"So lon nhat trong day {n} la: ",so_lon_nhat)

#Bài 9: Loại bỏ phần tử trùng lặp
n = input("Nhap day so cua ban: ")
m = n.split()
y = list(map(int, m))
tach = list(set(y))
print("Day so sau khi duoc tach la: ",tach)

#Bài 10: Đảo ngược danh sách
n = input("Nhap danh sach: ")
m = n.split()
dao_nguoc = m[::-1]
print("Danh sach sau khi dao nguoc la: ",dao_nguoc)

#Bài 11: Tính tổng các phần tử chẵn
n = input("Nhap cac so: ")
m = n.split()
y = list(map(int, m))
sum = 0
for i in y:
    if i % 2 == 0:
        sum += i
print("Tong cua cac so chan trong day la: ",sum)

#Bài 12: Tìm phần tử xuất hiện nhiều nhất
n = input("Nhap danh sach so: ")
m = n.split()
y = list(map(int, m))
xuat_hien = None
nhieu_nhat = 0
for i in y:
    dem = y.count(i)
    if dem > nhieu_nhat:
        nhieu_nhat = dem
        xuat_hien = i
print(f"Phan tu {xuat_hien} la phan tu xuat hien nhieu nhat.Voi {nhieu_nhat} lan")

#Bài 13: Gộp hai danh sách
n = input("Nhap danh sach dau tien: ")
m = input("Nhap danh sach thu hai: ")
y = list(map(int, n.split()))
z = list(map(int, m.split()))
a = y + z 
a.sort()
print("Danh sach duoc sap xep theo tang dan la: ",a)

#Bài 14: Lọc danh sách
m = input("Nhap danh sach dau tien: ")
n = input("Nhap danh sach thu hai: ")
y = list(map(int, m.split()))
z = list(map(int, n.split()))
a = y + z
danh_sach_moi = [element for element in a if element > 10]
print(danh_sach_moi)

#Bài 15: Danh sách từ trong chuỗi
n = input("Nhap doan danh sach trong chuoi: ")
for char in ". ! ? ,":
    n = n.replace(char, " ")

tu = n.lower().split()
dem_tu = {}
for word in tu:
    dem_tu[word] = dem_tu.get(word, 0) + 1
tu_sap_xep = sorted(dem_tu.items(),key = lambda x: x[1], reverse = True)
print("Danh sach theo thu tu giam dan la: ")
for tu,dem_tu in tu_sap_xep:
     print(f"{tu}:{dem_tu}")