#Bai 19 Viet cac so nhan trong bang cuu chuong tu 1 den 10
for i in range(1, 11):
    for j in range(i, 11):
        print(f"{i} * {j} = {i * j}", end=" ")
        print()


#Bai 20 Viet chuong trinh de kiem tra xem so dau vao la so chan hay so le
num = int(input("Nhap so can kiem tra: "))
if num % 2 == 0:
    print(num, "La so chan")
else:
    print(num,"La so le")

#Bai 21 Viet chuong trinh de in ra tat ca cac so chan tu 1 den 100
for i in range(1,101):
    if i % 2 == 0:
        print(i,"La cac so chan phu hop")

#Bai 22 Viet chuong trinh de in ra tat ca cac so le tu 1 den 100
for i in range(1,101):
    if i % 2 != 0:
        print(i,"La cac so le phu hop")
    
#Bai 23 Viet chuong trinh de tinh tong cac so tu 1 den n
n = int(input("Nhap so n:"))
tong = 0
for i in range(1, n+1):
    tong += i
print("Tong cac so tu 1 den", n, "la:", tong)

#Bai 24 Viet chuong trinh de tinh giai thua cua mot so nguyen duong n
n = int(input("Nhap so nguyen duong n:"))
giai_thua = 1 
for i in range(1, n+1):
    giai_thua *= i
print("Giai thua cua", n, "la:", giai_thua)

#Bai 25 Viet chuong trinh de in ra tat ca cac so nguyen to tu 1 den n
n = int(input("Nhap so n:"))
print("Cac so nguyen to tu 1 den", n, "la:")
for num in range(2,n + 1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
        