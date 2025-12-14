x = input("Nhap chuoi:")
x.split('')
for char in x:
    if char in x:
        print("True")
        break
else:
    print("False")
    