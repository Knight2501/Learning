s = 0 
while s < 100:
    s += 1 
    print(s)

count = 0 
while count < 10:
    print("Hello",count)
    count += 1

for i in range(10):
    if i == 10:
        break
    print(i)

for i in range(100):
    if i % 2  != 0:
        continue
    print(i)

for i in range(100,300):
    for n in range(400,500):
        if i % 2 == 0:
            print(i,n)
            break
    else:
        continue 

#Nhập vào 1 số nguyên dương n,dùng vòng lặp tính tổng từ 1 đến n và kiểm tra xem tổng đó là chẵn hay lẻ

n = int(input("Nhap vao so nguyen duong: "))
if n < 0:
    print("Nhap lai!!")
else:
    sum = 0
    for i in range(1,n + 1):
        sum += i
        print("Tong n so nguyen duong da nhap la: ",sum)
    if sum % 2 == 0:
            print("Tong nay la so chan") 
    else:
            print("Tong nay la so le")   

string1 = "Xin chao cac ban"
print(string1)

string2 = """Xin chao
cac ban"""
print(string2)

string_n = "Xin chao cac ban"
print(string_n[0])
print(string_n[0:3])
print(string_n[-1])
new_string = string_n[:7] + "Hello"
print(new_string)
string_w = "Xin chao\n cac ban \t den voi \\ Python \\"
print(string_w)
string_o = "Xin chao"
string_k = "cac ban"
print(string_o + " " + string_k)
print(string_o * 3)
 
name = "Tuan"
age = 18 
print("Toi ten la %s, toi %d tuoi",(name,age))
print("Toi ten la {}! Nam nay toi {} tuoi!".format(name,age))
print(f"Toi ten la {name},toi {age} tuoi")

ten1 = "ha le anh tuan"
ten2 = "HA LE ANH TUAN"
ten3 = "Ha Le Anh Tuan"
print(ten1.title())
print(ten2.title())
print(ten3.title())
ten4 = "Day la mot chuoi ky tu"
upper_ten4 = ten4.upper()
lower_ten4 = ten4.lower()
print(upper_ten4)
print(lower_ten4)

first_name = " Nga"
last_name = "Pham Thuy"
full_name = first_name + ' ' + last_name 
print(full_name)
message ="Hello " + full_name.title() + "!"
print(message)

text = " This is a message"
text_2 = " ! "
text_3 = text + text_2
text_4 = "toi la Tuan"
text_5 = "o giua"
text_6 = "2501200729122007"
rstrip = text_3.rstrip()
lstrip = text_3.lstrip()
strip = text_3.strip()
print(lstrip + '/' + rstrip + '/' + strip +'/')
print(text_4.capitalize())
print(text_5.center(100, "="))
print(text_5,len(text_5))

x = "Day la mot doan chuoi ky tu.Doan dau la ten.Doan sau la lop."
print(x.count("la"))
print(x.count("la",1,50))
print(x.find("la"))
print(text.endswith("e"))
print(text.startswith("H"))
print(x.find("sau"))
my_list = ["Hello","World","Python"]
x = '-'.join(my_list)
print(x)
print(x.replace("Day","Kia"))
print(x.replace("lop","So Thu Tu"))
print(x.split(", "))


