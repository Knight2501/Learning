#Bài 9:Nhập vào một chuỗi S, in ra chuỗi con có độ dài lớn nhất trong S, nếu có nhiều chuỗi con có độ dài giống nhau, in ra chuỗi con cuối cùng.

S = input("Nhap chuoi cua ban: ")
N = len(S)

chuoi_lon_nhat = ""
do_dai_lon_nhat = 0
for i in range(N):
    for j in range(i,N):
        chuoi_con_hien_tai = S[i:j + 1]
        do_dai_hien_tai = len(chuoi_con_hien_tai)
        if do_dai_hien_tai >= do_dai_lon_nhat:
            do_dai_lon_nhat = do_dai_hien_tai
            chuoi_lon_nhat = chuoi_con_hien_tai
print("========")
print("Độ dài lớn nhất: ",do_dai_lon_nhat)
print("Chuỗi lớn nhất: ",chuoi_lon_nhat)

#Bài 10:Nhập vào một chuỗi S, in ra chuỗi S1 là đảo ngược của S.
S = input("Nhập chuỗi: ")
S1 = "".join(reversed(S))
print(S1)

#Bài 11:Nhập vào một chuỗi S, thực hiện chuẩn hoá S với các yêu cầu sau:
#Các từ cách nhau bởi chỉ 1 dấu whitespace
#Chữ cái đầu của chuỗi in hoa, các kí tự còn lại là viết thường
#Chuỗi kết thúc bằng dấu .

S = input("Nhập chuỗi S:")
print("Chuỗi S có các từ cách nhau bởi 1 dấu whitespace là: ",S.split(" "))
print("Chuỗi S có chữ cái đầu của chuỗi in hoa,các kí tự còn lại là viết thường là: ",S.capitalize())
print("Kết thúc bằng dấu . là: ",S.endswith("."))