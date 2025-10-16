#Bài 6:Nhập chuỗi S:Tìm tất cả các chữ số xuất hiện trong chuỗi S.Tính tổng các chữ số trong chuỗi S.Nếu không có thì comment "Come on.I'm so tired"
S = input("Nhap chuoi: ")
digits = [int(ch) for ch in S if ch.isdigit()]
if digits:
    print("Các chữ số xuất hiện trong chuỗi S:", digits)
    print("Tổng các chữ số trong chuỗi S:", sum(digits))
else:
    print("Come on.I'm so tired")

#Bài 7:Nhập vào chuỗi S và S1. Xoá tất cả S1 xuất hiện trong S và in ra S cuối cùng.
#Khi có giá trị S1 trong S => Xóa luôn giá trị trong S và in ra S cuối với điều kiện tất cả các giá trị S không có trong S1
S = input("Nhap chuoi 1:")
S1 = input("Nhap chuoi 2:")
Ve_Sau = " " 
for ki_tu in S:
    if ki_tu not in S1:
        Ve_Sau += ki_tu
print(Ve_Sau)

#Bài 8: Nhập vào chuỗi S và S1. Xoá S1 xuất hiện lần đầu tiên trong S và in ra S.
S = input("Nhap chuoi S: ")
S1 = input("Nhap chuoi S1: ")
index = S.find(S1)
if index != -1:
    Ve_Sau = S[:index] + S[index+len(S1):]
    print(Ve_Sau)
else:
    print(S)


