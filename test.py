a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))

def tam_giac(a, b, c):
    # Kiểm tra điều kiện tam giác (tổng 2 cạnh phải LỚN HƠN cạnh còn lại)
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        print("Ba canh khong tao thanh tam giac!")
        return 
    else:
        chu_vi = a + b + c 
        p = chu_vi / 2
        dien_tich = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print(f"Dien tich cua tam giac la: {dien_tich:.2f}")
        print(f"Chu vi cua tam giac la: {chu_vi:.2f}")