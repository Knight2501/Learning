student = {
    "ten": "Tuan",
    "tuoi": 18,
    "nganh": "CNTT UDU",
    "p2": {"name": "Tuan", "age": 18}
}

print(student["ten"])
print(student["tuoi"])
print(student["nganh"])

gt_moi = student.get("truong","Hoc vien cong nghe buu chinh vien thong")
student["truong"] = "Hoc vien cong nghe buu chinh vien thong"
print(student.items())
print(student["truong"])
print(student["p2"]["name"])
del student["p2"]


tu_dien = {
    "spoon": "Cái thìa",
    "fork": "cái nĩa",
    "bowl": "cái bát",
    "fish": "con cá"
}
while True:
    #THIẾT KẾ GIAO DIỆN MENU
    text = "TỪ ĐIỂN ANH VIỆT"
    x = text.center(20,'=')
    print(x)
    print("1 - Tra Từ Điển")
    print("2 - Thêm Từ Điển")
    print("3 - Xóa Từ Điển")
    print("4 - Kết Thúc Chương Trình")

    chon = input("Chọn chức năng bạn muốn sử dụng: ")

# 1 - Tra Từ Điển

if chon == "1":
    while True:
        tu = input("Nhập từ bạn muốn tìm kiếm: ")
        if tu == "0":
            break
        if tu in tu_dien:
            print(f"Nghĩa của từ {tu_dien} là: {tu_dien[tu]}")
        else:
            print("Không tìm thấy từ này trong từ điển")
        print("Bạn có muốn tra tiếp không?")
        if chon_yn == "n":
            break
        else:
            continue
# 2 - Thêm từ điển 
if choice == "2":
    while True:
        tu_moi = input("Xin mời bạn điền từ bạn sẽ nhập: ")
        if tu_moi in tu_dien:
            print("Từ này đã có sẵn trong từ điển rồi!!!")
        else:
            nghia = input("Xin mời nhập nghĩa của từ: ")
            tu_dien[tu] = meaning
            print("Từ này đã được thêm mới")   
        print("Bạn có muốn thêm từ không? (y/n)")
        if chon2 == "n":
            break
        else:
            continue

# 3 - Xóa từ điển
if chon == "3":
    while True:
        tu_xoa = input("Nhập từ cần xóa: ")
        if tu_xoa in tu_dien:
            del tu_dien[tu]
            print(f"Từ {tu_dien} đã được xóa thành công!")
        else:
            print("Không thể tìm thấy từ này để xóa ở trong từ điển")
        print("Bạn có muốn xóa từ khác không? (y/n)")
        if chon3 == "n":
            break
        else:
            continue

#4 - Kết thúc chương trình
if chon == "4":
    while True:
           print("Cảm ơn bạn đã sử dụng từ điển ANH VIỆT! Hẹn gặp lại")
           break     