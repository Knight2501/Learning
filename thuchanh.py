#Bai 1:In vao 1 chuoi ki tu,in hoa chu cai dau,in hoa chu cai dau moi tu,in hoa toan bo,in thuong toan bo
x = "Tôi tên là Tuấn"
print(x.capitalize())
print(x.title())
print(x.upper())
print(x.lower())

#Bài 2:Nghĩ tới một trích dẫn của người nổi tiếng mà bạn thích.In trích dẫn
#Leningrad:"Học,học nữa,học mãi "
trich_dan = "\"Học,Học nữa,Học mãi\""
print("Leningrad once said: "+ trich_dan)

#Bài 3:Nhập vào một chuỗi kí tự.Kiểm tra xem chuỗi đó có thỏa mãn điều kiện không?
#Chỉ chứa số 0-9
#Chỉ chứa kí tự a-z
#Chỉ chứa kí tự a-z,số 0-9
#Tất cả đều viết hoa
#Tất cả đều viết thường

chuoi = input("Nhap chuoi ki tu: ")
if chuoi.isdigit():
    print("Chuoi nay chi chua so") #0-9
elif chuoi.isalpha(): #Chữ
    if chuoi.isupper():
        print("Chuoi nay chi chua ki tu viet hoa") #Chữ viêt hoa
    else:
        print("Chuoi nay chi chua ki tu viet thuong")   #Chữ viết thường
elif chuoi.isalnum():
    print("Chuoi nay chua ca ki tu va so") #Chữ và số
else:
    print("Chuoi nay chua ki tu dac biet")

#Bài 4:Nhập vào chuỗi gồm nhiều từ cách nhau bởi dấu whitespace
#Kiểm tra có kết thúc bằng từ end không
#Kiểm tra có từ "is" không.Có thì in ra vị trí đầu và số lần xuất hiện trong chuỗi
#Thay thế "is" bằng "are"
#Chuyển chuỗi thành danh sách chứa các từ và đếm lượng số lượng từ hiện có

chuoi = input("Nhap chuoi can nhap:")
if chuoi.strip().endswith("end"):
    print("Chuoi co end")
else:
    print("Chuoi khong co end")

if chuoi.strip("is"):
    print(chuoi.find("is"))
    print(chuoi.count("is"))
    print(chuoi.replace("Is","Are"))
else:
    print("Chuoi nay khong co is")

tu = chuoi.split()
print("So tu la:", chuoi.len(tu))
print("Danh sach cac tu la:",tu)

#Bài 5:Nhập vào hai chuỗi kí tự S1 và S2. In ra chuỗi kí tự S được tạo thành bằng cách chèn S2 vào chính giữa S1.

S1 = input("Nhap chuoi dau tien: ")
S2 = input("Nhap chuoi tiep theo: ")
giua = len(S1) // 2
S = S1[0:giua] + S2 + S1[giua:]
print(S)