#Bài 1. In thông tin cá nhân
name = "Tuan"
age = 18
school = "Hoc vien cong nghe buu chinh vien thong"
print("Xin chào tôi là ",name, " ,năm nay",age," tuổi,đang học tại ",school)

#Bài 2. Tính chu vi và diện tích hình chữ nhật
chieu_dai = int(input("Nhập chiều dài: "))
chieu_rong = int(input("Nhập chiều rộng: "))
if chieu_dai and chieu_rong < 0:
    print("Nhap lai.")
elif chieu_dai <= chieu_rong:
    print("Nhap lai")
else:
    perimeter = (chieu_dai + chieu_rong ) * 2
    square = (chieu_dai * chieu_rong)
    print("Chu vi hình chữ nhật là: ",perimeter)
    print("Diện tích hình chữ nhật là: ",square)

#Bài 3. Chuyển đổi nhiệt độ
C = int(input("Nhập nhiệt độ C: "))
F = (C * 9/5) + 32
print("Nhiệt độ từ độ C chuyển qua độ F là: ",F)

#Bài 4. Tính điểm trung bình
Toan = float(input("Nhập điểm toán: "))
Van = float(input("Nhập điểm văn: "))
Anh = float(input("Nhập điểm anh: "))
if (Toan < 0 and Van < 0 and Anh < 0) or (Toan < 0) or (Van < 0) or (Anh < 0) or (Toan < 0 and Van < 0) or (Toan < 0 and Anh < 0) or (Van < 0 and Anh < 0):
    print("Sai dieu kien")
else:
    avg = (Toan + Van + Anh ) / 3
    print("Điểm trung bình 3 môn là: ",avg)

#Bài 5. Ghép chuỗi
ten = input("Nhập tên: ")
tuoi = int(input("Nhập tuổi: "))
print("Tôi tên là: ",ten,".Năm nay tôi",tuoi,"tuổi.Năm sau tôi sẽ",tuoi + 1,"tuổi")

#Bài 6. Kiểm tra số chẵn/lẻ
so = int(input("Nhập giá trị: "))
if so < 0:
    print("Sai dieu kien.")
else:
    if so % 2 == 0:
        print("Day la so chan")
    else:
        print("Day la so le ")

#Bài 7. So sánh hai số
a = int(input("Nhập giá trị a: "))
b = int(input("Nhập giá trị b: "))
if a < b:
    print("Số b lớn hơn a")
else:
    print("Số a lớn hơn b")

#Bài 8. Xếp loại học lực
diem = float(input("Nhập điểm của mình: "))
if diem < 0:
    print("Điểm không hợp lệ")
else:
    if diem >= 8.0:
        print("Học sinh giỏi")
    elif 6.5 <= diem < 8.0:
        print("Học sinh khá")
    elif 5 <= diem < 6.5:
        print("Học sinh trung bình")
    else:
        print("Học sinh yếu")

#Bài 9. Tính tiền điện
so_dien = int(input("Nhập số điện: "))
if so_dien < 0:
    print("Sai đề bài")
else:
    if 0 <= so_dien <= 50:
        tien = so_dien * 1800
        print("Số tiền đóng theo số điện là",tien)
    elif 51 <= so_dien <= 100:
        tien = (50 * 1800) + (100-so_dien) * 2000
        print("Số tiền đóng theo số điện là",tien)
    else:
        tien = (50 * 1800) + (50 * 2000) + (so_dien * 2500)
        print("Số tiền đóng theo số điện là",tien)

#Bài 10. Kiểm tra năm nhuận
nam = int(input("Nhập năm."))
if nam < 0:
    print("Before Christ")
    if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
        print("Năm ",nam, " là năm nhuận") 
    else:
        print("Năm bình thường")
else:
    print("AD")
    if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
        print("Năm ",nam, " là năm nhuận") 
    else:
        print("Năm bình thường")

#Bài 11. In bảng cửu chương
n = int(input("Nhập số: "))
if n <= 0:
    print("Sai điều kiện")
else:
    for i in range(0,9):
        i += 1
        mul = n * i
        print("Bảng cửu chương của số ",n,"là: ",mul)

#Bài 12. Tính tổng từ 1 đến n
n = int(input("Nhập n: "))
sum = 0
for i in range(0,n):
    i += 1
    sum += i
print("Tổng của các số từ 1 đến %d là:" %(n),sum)

#Bài 13. Đếm số chẵn trong dãy
n = int(input("Nhập dãy n nguyên: "))
count = 0
if n <= 0:
    print("Sai điều kiện")
else:
    for i in range(1,n + 1):
        if i % 2 == 0:
            count += 1
    print("Dãy này có:",count," số chẵn")

#Bài 14. Đoán số bí mật
import random
n = random.randint(1,10)
while True:
    if a <= 0:
        print("Dừng trò chơi")
    else:
        a = int(input("Nhập a: "))
        if n < a:
            print("Số bạn đoán to quá!")
        elif n > a:
            print("Số bạn đoán bé quá")
        else:
            print("Bạn đoán đúng rồi!!! Chúc mừng bạn")

#Bài 15. Vẽ tam giác sao
n = int(input("Nhập số hàng sao: "))
if n <= 0:
    print("Sai điều kiện rồi! Nhập lại ")
else:
    for i in range(1,n + 1):
        for j in range(i):
            print("*",end ="")
        print()

             
        