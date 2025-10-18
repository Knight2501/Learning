#0072. Tính tổng những số nguyên từ m đến n
m = int(input("Nhập giá trị của m: "))
n  = int(input(("Nhập giá trị của n: ")))
sum = 0

if m and n <= 0:
    print("=======")
    print("Error")
else:
    for i in range (m,n+1):
        if m <= n:
            sum += i
        else:
            print("Khong the co dap an chinh xac cho cau nay vi sai dieu kien de bai dua ra...")
            print("========")
    print("Tong cua 2 so m va n la: ",sum)

#0073. Đếm số lượng số nguyên chia hết cho 3 từ m đến n
m = int(input("Nhập giá trị m: "))
n = int(input("Nhập giá trị n: "))
count = 0
if m <= 0 and n <= 0:
    print("Sai dieu kien,vui long nhap lai")
else:
    for i in range(m,n + 1):
        if m <= n and i % 3 == 0:
            count += 1
    print("Số lượng giá trị nguyên chia hết cho 3 từ m đến n là: ",count)

#0074:Đếm số lượng số chẵn từ m đến n 
m = int(input("Nhập giá trị m: "))
n = int(input("Nhập giá trị n: "))
count = 0
if m and n <= 0:
    print("Lỗi điều kiện đưa ra")
elif m >= n:
    print("Lỗi điều kiện")
else:
    for i in range(m,n + 1):
        if i % 2 == 0:
            print(i)
        else:
            print("-")


        

    

