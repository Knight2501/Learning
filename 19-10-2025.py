#0075. Đếm số lượng số nguyên chẵn từ m đến n
m = int(input("Nhập giá trị của m: "))
n = int(input("Nhập giá trị của n: "))
count = 0
if m <= 0 and n <= 0:
    print("Loi dieu kien.Vui long nhap lai")
elif m > n:
    print("Loi dieu kien thoa man")
else:
    for i in range(m,n+1):
        if i % 2 == 0:
            count += 1
            print(count)

#0076. Tính tổng những số nguyên chẵn từ m đến n
m = int(input("Nhập giá trị m: "))
n = int(input("Nhập giá trị n: "))
sum = 0 
if m < 0 and n < 0:
    print("Sai lenh.Vui long nhap lai")
elif m > n:
    print("Sai dieu kien.Vui long nhap lai")
else:
    for i in range(m,n + 1):
        if i % 2 == 0:
            sum += i
    print("Tổng từ m đến n là: ",sum)

#0077. Tính trung bình cộng những số nguyên chẵn từ m đến n
m = int(input("Nhập giá trị m: "))
n = int(input("Nhập giá trị n: "))
sum = 0
if m < 0 and n < 0:
    print("Sai dieu kien.Vui long nhap lai.")
elif m > n:
    print("Sai dieu kien.Hay nhap lai.")
else:
    for i in range(m,n + 1):
        if i % 2 == 0:
            sum += i / 2 
    print("Trung bình cộng của 2 số m và n là: ",sum)

#0078. Tính trung bình cộng những số nguyên chia hết cho 2 và 3 từ m đến n
#Số thứ nhất chia hết cho 5 và số thứ 2 chia hết cho 2 và 3 
m = int(input("Nhập giá trị m: "))
n = int(input("Nhập giá trị n: "))
sum = 0
avg = 0 
if m and n < 0:
    print("Lỗi điều kiện.Vui lòng nhập lại")
elif m > n:
    print("Điều kiện đưa ra bị lỗi.Hãy nhập lại")
else:
    for i in range(m,n + 1):
        if i % 2 == 0 and i % 3 == 0:
            avg += i // 2
        print("Trung bình cộng của m và n là: ",avg)
    else:
        print("0")
        if i % 5 == 0:
            sum += i
            print("Số chia hết cho 5 là: ",sum)