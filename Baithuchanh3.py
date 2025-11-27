#1. Tính tổng phần tử trong list
n = int(input("Nhap so phan tu:"))
lst = []
sum = 0
for i in range(n):
    lst.append(int(input()))

for v in lst:
    sum += v
print("Tong cac phan tu trong list:",sum)

#2. Đếm số lần xuất hiện
n = input("Nhap chuoi: ")
lst = [].lower()
dem = 0
chuoi_dem = input("Nhap chuoi ky tu:").lower()
so_lan = n.count(chuoi_dem)
print(f"Ky tu '{chuoi_dem}' xuat hien {so_lan} trong chuoi.")

#3. Tìm phần tử lớn nhất
n = int(input("Nhap so:"))
lst = []
for i in range(n):
    lst.append(int(input()))
    max_value = max(lst)

for v in lst:
    if v == max_value:
        print("phan tu lon nhat trong list:",max_value)

#4. Kiểm tra phần tử có trong tuple hay không
n = input("Nhap tuple:")
gia_tri = tuple(n.split(","))
check = input("Nhap gia tri can kiem tra: ")
if check in gia_tri:
    print(f"Gia tri '{check}' co trong tuple")
else:
    print(f"Gia tri '{check}' khong co trong tuple")

#5. Chuyển list sang set
n = input("Nhap chuoi: ")
lst = [].lower()
for i in range(len(n)):
    lst.append(input().lower())
set_lst = set(lst)
print("Day sau khi chuyen doi la:",set_lst)

#6. Đảo ngược list
n = input("Nhap list:")
chuoi_moi = ""
for i in range(n -1,-1,-1):
    chuoi_moi += n[i]
print("Chuoi sau khi dao nguoc: ",chuoi_moi)

#7. Ghép 2 tuple
tup1 = input("Nhap tuple 1:")
tup2 = input("Nhap tuple 2:")
tup_sum = tup1 + tup2
print("Tuple sau khi ghep la:",tup_sum)

#8. Tạo dictionary đơn giản
ten = input("Xin moi ban nhap ten cua 3 nguoi(cach nhau boi dau phay):")
tuoi = input("Xin moi ban nhap tuoi cua 3 nguoi(cach nhau boi dau phay):")
danh_sach_ten = ten.split(",")
danh_sach_tuoi = tuoi.split(",")
my_dict = {}
for ten,tuoi in zip(danh_sach_ten,danh_sach_tuoi):
    my_dict[ten] = tuoi
print("\n Danh sach ten va tuoi")
print(f"{ten}: {tuoi}")

#9. Loại bỏ phần tử trùng trong list nhưng giữ thứ tự
n = input("Nhap chuoi:")
lst = []
for i in n:
    if i not in lst:
        lst.append(i)

print("List sau khi loai bo phan tu trung la:",lst)

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

#11. Gộp hai dictionary
n = input("Nhap dictionary thu nhat:")
m = input("Nhap dictionary thu hai:")
gop = n.copy()
for gia_tri in m.copy():
    if gia_tri not in gop:
        gop[gia_tri] = m[gia_tri]
    else:
        gop[gia_tri] += m[gia_tri]
print("Dictionary sau khi gop la:",gop)

#12. Tạo dictionary đếm ký tự
n = input("Nhap chuoi:")
my_dict = {}
for i in n:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1
print("Dictionary dem ky tu la:",my_dict)

#13. Tìm giao, hợp và hiệu của hai set
set1 = input("Nhap set 1:")
set2 = input("Nhap set 2:")
giao = set1.intersection(set2)
hop = set1.union(set2)
hieu = set1.difference(set2)
print("Giao cua 2 set la:",giao)
print("Hop cua 2 set la:",hop)
print("Hieu cua 2 set la:",hieu)

#14. Tìm giá trị trung bình của list tuple
day_so_tuples = input("Nhap list tuple:")
n = len(day_so_tuples)
tong_x = 0
tong_y = 0
if n > 0:
    for x, y in day_so_tuples:
        tong_x += x
        tong_y += y
    trung_binh_x = tong_x / n
    trung_binh_y = tong_y / n
    print("Gia tri trung binh cua x la:",trung_binh_x)
    print("Gia tri trung binh cua y la:",trung_binh_y)

#15. Lọc phần tử theo điều kiện
n = int(input("Nhap day so: "))
lst = []
for i in range(n):
    lst.append(int(input()))

for v in lst:
    if v % 2 == 0 and v > 10:
        print("Day so moi la:",v)

#16.Sắp xếp dictionary theo giá trị
n = input("Hay nhap dictionary theo cu phap {ten:diem}")
diem_hoc_sinh = sorted(n.items(), key=lambda x: x[1], reverse=True)
diem_sap_xep = dict(diem_hoc_sinh)
print("Dictionary sau khi sap xep la:",diem_sap_xep)

#17. Chuyển list từ điển thành từ điển tổng hợp
data = [
    {"name": "A", "score": 7},
    {"name": "B", "score": 9},
    {"name": "A", "score": 8},
]
result = {}
for item in data:
    ten = item["name"]
    diem = item["score"]
    if ten in result:
        result[ten].append(diem)
    else:
        result[ten] = [diem]
print("Tu dien tong hop la:",result)
#18. Tạo danh sách sản phẩm không trùng SKU
n = input("Nhap danh sach")
diction = {}
for sku,quantity in n:
    if sku in diction:
        diction[sku] += quantity
    else:
        diction[sku] = quantity
print("Danh sach san pham khong trung SKU la:",diction)

#19.Tìm cặp phần tử có tổng gần nhất với số 
def tim_tong_gan_nhat(n, N):
    n.sort()
    cap_gan_nhat = None
    khoang_cach_nho_nhat = float('inf')
    T,P = 0 , len(n) - 1
    while T < P:
        tong = n[T] + n[P]
        khoang_cach = abs(N - tong)
        if khoang_cach < khoang_cach_nho_nhat:
            khoang_cach_nho_nhat = khoang_cach
            cap_gan_nhat = (n[T], n[P])
        if tong < N:
            T += 1
        else:
            P -= 1
    return cap_gan_nhat

#20.Ma trận dưới dạng list lồng nhau
matrix = [
   [1,2,3],
   [4,5,6],
   [7,8,9]
]
n = len(matrix) 
tong_cheo_chinh = 0 
tong_cheo_phu = 0
for i in range(n):
    tong_cheo_chinh += matrix[i][i]
    tong_cheo_phu += matrix[i][n - 1 - i]
    tuple_of_tuples = tuple(tuple(row) for row in matrix)
print(f"Tổng đường chéo chính: {tong_cheo_chinh}")
print(f"Tổng đường chéo phụ: {tong_cheo_phu}")
print("Ma trận dưới dạng tuple of tuples:",tuple_of_tuples)
