#4. Kiểm tra phần tử có trong tuple hay không
n = input("Nhap tuple:")
gia_tri = tuple(n.split(","))
check = input("Nhap gia tri can kiem tra: ")
if check in gia_tri:
    print(f"Gia tri '{check}' co trong tuple")
else:
    print(f"Gia tri '{check}' khong co trong tuple")