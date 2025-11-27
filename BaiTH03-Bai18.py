#18. Tạo danh sách sản phẩm không trùng SKU
n = input("Nhap danh sach")
diction = {}
for sku,quantity in n:
    if sku in diction:
        diction[sku] += quantity
    else:
        diction[sku] = quantity
print("Danh sach san pham khong trung SKU la:",diction)