#17. Chuyển list từ điển thành từ điển tổng hợp
data = [
    {"name": "A", "score": 7},
    {"name": "B", "score": 9},
    {"name": "A", "score": 8},
]
result = {}
for item in data:
    ten = item["name"]
    diem = item["score"]
    if ten in result:
        result[ten].append(diem)
    else:
        result[ten] = [diem]
print("Tu dien tong hop la:",result)