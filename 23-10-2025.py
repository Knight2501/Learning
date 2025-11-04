#Bài 79:
m = int(input("Nhập giá trị của m: "))
n = int(input("Nhập giá trị của n: "))
count_7 = 0
sum_2_or_3 = 0
count_2_or_3 = 0
if m < 0 and n < 0:
    print("Sai điều kiện,mời nhập lại")
elif m > n:
    print("Sai điều kiện")
else:
    for i in range(m,n + 1):
        if i % 7 == 0:
            count_7 += 1
        if i % 2 == 0 or i % 3 == 0:
            sum_2_or_3 += i
            count_2_or_3 += 1
    print("Có",count_7,"giá trị chia hết cho 7")
    if count_2_or_3 > 0:
            avg = sum_2_or_3 / count_2_or_3
            print("Trung bình cộng của các số chia hết cho 2 hoặc 3 là: ",avg)
    else:
        print("0.0")

#Bài 80:
m = int(input("Nhập giá trị của m: "))
n = int(input("Nhập giá trị của n: "))
count = 0
so = 0
if m < 0 and n < 0:
     print("Sai điều kiện,nhập lại")
elif m > n:
     print("Sai điều kiện,nhập lại")
else:
    for i in range(m,n + 1):
        if i % 5 == 0:
            so += i
            count += 1
    print(f"Có {count} số chia hết cho 5",so,sep='-')