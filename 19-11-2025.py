def xin_chao():
    print("Xin chao,chao mung ban den voi buoi hoc!")
xin_chao()

def greet(name):
    print("Xin chao, " + name)
greet("Tuan")

def add(a, b):
    print("Tong cua a va b la:",a + b)
add(10,200)

def greet(name = "Thai"):
    print("Xin chao ", name)
greet()
greet("Khai")

def tat_ca_tong(*numbers):
    total = sum(numbers)
    print("Tong =",total)
tat_ca_tong(1, 2, 3, 4)
tat_ca_tong(6, 7, 8 ,9)

def binh_phuong(x):
    return x * x

result = binh_phuong(10)
print("Binh phuong: ",result)

def sum(a,b):   ## Tính tổng của a và b
    tong = a + b
    return tong

def kiemtrachanle(numb): ## Kiểm tra tổng của số này là chẵn hay lẻ
    if numb % 2 == 0:
        print("Day la so chan")
    else:
        print("Day la so le")

def kiemtraAD(numb):    ## Kiểm tra số này là số âm hay số dương 
    if numb > 0:
        print("So nay la so duong")
    else:
        print("Day la so am")

tong = sum(11,100)
kiemtrachanle(tong)
kiemtraAD(tong)


def gtln_gtnn(numbers):
    return min(numbers), max(numbers)
gia_tri_nho, gia_tri_lon = gtln_gtnn([1, 2, 4, 7, 9])
print("Gia tri nho nhat la: ",gia_tri_nho)
print("Gia tri lon nhat la: ",gia_tri_lon)

a = 100
def sum():
    b = 6
    print("Tong cua a va b ",a + b)

sum()
print("O ngoai bien ",a)

import math
print(math.sqrt(4))

import math as m
print(m.pow(5,10))

from math import pi,pow
print(pi)
print(pow(2, 3))

import main
main.greet("Ha Le Tuan")
print(main.add(3, 6))


import main as m 
m.greet("Ha Le Tuan")
print(m.add(1, 8))

from main import greet
greet("Ha Le Tuan")