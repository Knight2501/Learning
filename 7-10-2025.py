#0064. Đếm số lượng số tự nhiên chia hết cho 3 từ 1 đến n
n = int(input("Nhap so tu nhien chia het cho 3: "))
count = 0
for i in range(1, n + 1):
    n += 1 
    if n % 3 == 0:
        count += 1
print("So luong so chia het cho 3 la: ",count)

#0065. Tính tổng những số tự nhiên chẵn từ 1 đến n
n = int(input("Nhap so tu nhien chan: "))
count = 0 
sum = 0
for i in range(1,n + 1):
    n += 1 
    if n % 2 == 0:
        count += 1 
        sum += i 
print("Tong so tu nhien chan tu 1 den n la: ",sum)


#0066. Tính tổng những số tự nhiên chia hết cho 3 và 5 từ 1 đến n
n = int(input("Nhap so tu nhien chia het cho 3 va 5: "))
total = 0
for i in range(1,n + 1):
    n += 1
    if n % 3 == 0 and n % 5 == 0:
        print("So tu nhien chia het cho 3 va 5 la: ", i,sep=' ')

#0067. Tính tổng những số tự nhiên chia hết cho 3 hoặc 5 từ 1 đến n
n = int(input("Nhap so tu nhien chia het cho 3 va 5: "))
sum = 0 
count = 0 
for i in range(1,n + 1):
    n += 1 
    if i % 3 == 0 and i % 5 == 0:
        count += 1
        sum += i 
print("Tong so tu nhien chia het cho 3 va 5 la: ",sum)

#0068. Tính trung bình cộng những số tự nhiên chẵn từ 1 đến n
n = int(input("Nhap so tu nhien: "))
count = 0 
avg = 0 
for i in range(1,n + 1):
    n += 1 
    if n % 2 == 0:
        count += 1 
        avg += i // 2
print("TBC cua cac so chan la: ",avg)

#0069. Tính trung bình cộng những số tự nhiên chẵn từ 1 đến n chia hết cho 3  
n = int(input("Nhap so tu nhien: "))
count = 0 
avg = 0 
for i in range(1,n + 1):
    n += 1 
    if n % 5 == 0:
        count += 1 
        avg += i / 2
    else:
        print("0.0")
print("TBC cua cac so chan la: ",avg)

#0070. Tính trung bình cộng những số tự nhiên chia hết cho 3 và 5 từ 1 đến n
n = int(input("Nhap so tu nhien: "))
count = 0 
avg = 0 
for i in range(1,n + 1):
    n += 1
    if i % 3 == 0 and i % 5 == 0:
        count += 1 
        avg += i / 2
print("TBC cua nhung so tu nhien chia het cho 3 va 5 la: ",avg)

#0071. In những số tự nhiên từ m đến n
m = int(input("Nhap m: "))
n = int(input("Nhap n: "))
if m <= n:
    for i in range (m,n + 1):
        print(i,sep=' ')
else:
    print("Ket thuc chuong trinh")
