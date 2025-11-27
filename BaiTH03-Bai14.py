#14. Tìm giá trị trung bình của list tuple
day_so_tuples = input("Nhap list tuple:")
n = len(day_so_tuples)
tong_x = 0
tong_y = 0
if n > 0:
    for x, y in day_so_tuples:
        tong_x += x
        tong_y += y
    trung_binh_x = tong_x / n
    trung_binh_y = tong_y / n
    print("Gia tri trung binh cua x la:",trung_binh_x)
    print("Gia tri trung binh cua y la:",trung_binh_y)