#0081. Tìm ước chung lớn nhất của hai số nguyên a và b 
import math
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
ucln = math.gcd(a, b)
print(f"Uoc chung lon nhat cua {a} va {b} la: ",ucln)
#0082. Rút gọn phân số
import math
a = int(input("Nhap tu so: "))
b = int(input("Nhap mau so: "))
ucln = math.gcd(a,b)
if b == 0:
    print("He so khong ra duoc ket qua")
else:
    tu_so = a // ucln
    mau_so = b // ucln
    print(f"Tu so rut gon cua {a} la: ",tu_so)
    print(f"Mau o rut gon cua {b} la: ",mau_so)
    print(f"Phan so rut gon cua {a}/{b} la: {tu_so}/{mau_so}")

#0083. Tìm số lượng chữ số của một số nguyên n
so = int(input("Nhap so nguyen ban muon nhap: "))
count = 0
while so >= 10:
    so = so // 10
    count += 1
print(f"So {so} co {count} chu so")