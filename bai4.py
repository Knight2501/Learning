n = int(input("Nhap so nguyen n:"))
if n >= 6 and n % 3 == 0:
    so_giua = n // 3 
    so_dau = so_giua - 1
    so_cuoi = so_giua + 1 
    print(f"{n} co 3 so tu nhien lien tien {so_dau}, {so_giua}, {so_cuoi}")
else:
    print(f"{n} khong phai la con so co tong la 3 so tu nhien lien tiep")