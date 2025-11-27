#16.Sắp xếp dictionary theo giá trị
n = input("Hay nhap dictionary theo cu phap {ten:diem}")
diem_hoc_sinh = sorted(n.items(), key=lambda x: x[1], reverse=True)
diem_sap_xep = dict(diem_hoc_sinh)
print("Dictionary sau khi sap xep la:",diem_sap_xep)