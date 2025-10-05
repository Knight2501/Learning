#0058. In ra các chữ số lẻ của một số có 8 chữ số
n = input("Nhap so co 8 chu so: ")
for i in n:
    if int(i % 2 !=0):
        print(i, end = ' ')

#0059. Tính tổng các chữ số chẵn của một số có 8 chữ số
n = input("Nhap so chan co 8 chu so: ")
sum = 0
for i in n:
    if int(i) % 2 == 0:
        sum += int(i)
        print("Tong cac chu so chan la: ",sum)

#0060. Tìm chữ số lớn nhất và nhỏ nhất của một số có 8 chữ số
n = input("Nhap so tu nhien co 8 chu so: ")
max = int(n[0])
min = int(n[0])
for i in n:
    if int(i) > max:
        max = int(i)
    if int(i) < min:
        min = int(i)
print("So lon nhat la: ",max,".So nho nhat la: ",min)

#0061. Tính tổng các chữ số của một số có n chữ số
n = int(input("Nhap so tu nhien co n chu so: "))
for i in range(1,n + 1):
    n += 1 
    print(i,end=' ')

#0062. Tính tổng các chữ số của một số có n chữ số
n = int(input("Nhap so tu nhien co n chu so: "))
sum = 0
for i in range(1,n + 1):
    sum += i
print(sum)

#0063. In những số tự nhiên chia hết cho 3 từ 1 đến n
n = int(input("Nhap nhung so tu nhien chia het cho 3: "))
for i in range(1, n + 1):
    n += 1 
    if n % 3 == 0:
        print(i,sep=' ')
print("So chia het cho 3 la: ",i)
