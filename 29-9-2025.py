#Bai 14 dao nguoc mot so da cho
num = 76542
reverse_num = 0
while num > 0:
    digit = num % 10
    reverse_num = (reverse_num * 10) + digit
    num = num // 10
print("So dao nguoc la:", reverse_num)

#Bai 15 Tim so co o vi tri muc le 
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(len(my_list)):
    if i % 2 != 0:
        print("So o vi tri le la:", my_list[i])

#Bai 16 Tim so lap phuong cua cac so tu 1 den 6 
num = 6
for i in range(1,num + 1):
    print("So chinh phuong cua ", i, "la: ", i ** 3)

#Bai 17 Tim tong cua mot day so co so hang den n
num = 2
n = 5 
total = 0
for i in range(1,n + 1):
    total = total + num
    num = (num * 10) + 2
    print("Tong cua",n, "so chinh phuong la: ",total)

#Bai 18 Ve hinh ngoi sao tam giac
n = 5 
for i in range(n+1):
    for j in range(i):
        print("*",end=" ")
    print(" ")
for j in range(n-1,0, -1):
    for k in range(j):
        print("*",end=" ")
    print()
