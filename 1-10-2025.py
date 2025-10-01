print("Hello World")
print("Hello","World",sep="-",end = "!\n")
x = ("Toi ten la","Ha Le Anh Tuan","Toi hoc lop D25 cua PTIT")


age =int(input("Nhap tuoi:"))
print("Tuoi cua ban la:",age)

name = input("Nhap ten:")
print("Xin chao " + name + "!",end= "\n")

num1 = int(input("Nhap so dau tien:"))
num2 = int(input("Nhap so sau do:"))
multiple = num1 * num2
print("Tich cua hai so la:",multiple)

money = float(input("Nhap cac menh gia tien da gui:")).split()
print("Cac menh gia tien ban da nhap trong ngan hang la: ",money)

a = int(input("Nhap a: "))
b = int(input("Nhap b: "))

print("a + b =",a + b)
print("a - b =",a - b)
print("a * b = ",a * b)
print("a / b =",a / b)
print("a // b =",a // b)
print("a % b =",a % b)
print(" a ** b =", a ** b)

a = int(input("Nhap a: "))
a += 10
a -= 5
a *= 3
a /= 4
a //= 2
a %= 3
a **= 4
print("Ket qua cua cac dap an voi a la: ",a)

a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
print("a == b",a == b)
print(" a != b",a != b)
print("a > b",a > b)
print("a < b",a < b)
print("a >= b",a >= b)
print("a <= b",a <= b)


a = True
b = False
print("a and b",a and b)
print("a or b",a or b)
print("not a",not a)


if age < 18:
    print("Ban chua du tuoi truong thanh")


if age > 18:
    print("Ban da du tuoi truong thanh")
else:
    print("Ban chua du tuoi truong thanh")


if age > 0 and age < 13:
    print("Ban la tre con")
elif age >= 13 and age < 18:
    print("Ban la thieu nien")
elif age >= 18 and age < 60:
    print("Ban la nguoi lon")
else:
    print("Ban la nguoi gia")

    #Nhap so tien dien

so_dien = int(input("Nhap so dien da su dung: "))
if so_dien <= 50:
    tien_dien= (so_dien * 600)
elif so_dien > 50 and so_dien <= 100:
    tien_dien = so_dien * 750
elif so_dien > 100 and so_dien <= 200:
    tien_dien = so_dien * 900
elif so_dien > 200:
    tien_dien = so_dien * 1200
print("So tien dien phai tra la:",tien_dien)



def tien_dien(a):
    if a <= 50:
        return a * 600
    elif a > 50 and a <= 100:
        return (50 * 600) + (a - 50) * 750
    elif a > 100 and a <= 200:
        return (50 * 600) + (50 * 750) + (a - 100) * 900
    elif a > 200:
        return (50 * 600) + (50 * 750) + (100 * 900) + (a - 200) * 1200
a = int(input("Nhap so dien da su dung: "))
print("So tien dien phai tra la:",tien_dien(a))
