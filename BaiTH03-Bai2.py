#2. Đếm số lần xuất hiện
n = input("Nhap chuoi: ")
lst = [].lower()
dem = 0
chuoi_dem = input("Nhap chuoi ky tu:").lower()
so_lan = n.count(chuoi_dem)
print(f"Ky tu '{chuoi_dem}' xuat hien {so_lan} trong chuoi.")