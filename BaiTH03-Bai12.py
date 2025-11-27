#12. Tạo dictionary đếm ký tự
n = input("Nhap chuoi:")
my_dict = {}
for i in n:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1
print("Dictionary dem ky tu la:",my_dict)