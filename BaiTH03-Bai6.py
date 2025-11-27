#6. Đảo ngược list
n = input("Nhap list:")
chuoi_moi = ""
for i in range(n -1,-1,-1):
    chuoi_moi += n[i]
print("Chuoi sau khi dao nguoc: ",chuoi_moi)
