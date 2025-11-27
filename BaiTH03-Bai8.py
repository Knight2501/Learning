#8. Tạo dictionary đơn giản
ten = input("Xin moi ban nhap ten cua 3 nguoi(cach nhau boi dau phay):")
tuoi = input("Xin moi ban nhap tuoi cua 3 nguoi(cach nhau boi dau phay):")
danh_sach_ten = ten.split(",")
danh_sach_tuoi = tuoi.split(",")
my_dict = {}
for ten,tuoi in zip(danh_sach_ten,danh_sach_tuoi):
    my_dict[ten] = tuoi
print("\n Danh sach ten va tuoi")
print(f"{ten}: {tuoi}")