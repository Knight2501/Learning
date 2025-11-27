with open("46.png","rb") as f:
    content = f.read()
    print("Kich thuoc file:", len(content), "bytes")

try:
    with open("filekhontontai.txt",'r',encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
        print("Khon the tim thay file.")

with open("students.txt",'r',encoding='utf-8') as f:
    ten = f.readlines()
    for n in ten:
         print("Sinh vien:",n.strip())
        