#9. Loại bỏ phần tử trùng trong list nhưng giữ thứ tự
n = input("Nhap chuoi:")
lst = []
for i in n:
    if i not in lst:
        lst.append(i)

print("List sau khi loai bo phan tu trung la:",lst)