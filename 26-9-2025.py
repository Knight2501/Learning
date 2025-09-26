print("Hello World")
a = 100 
b = 200.5
c = "Toi la Ha Le Anh Tuan"
print(a)
print(b)
print(c)
print(id(a))
print(id(b))
print(id(c))
print(int(a))
print(float(a))
print(int(b))
print(str(b))
print(type(a), type(b), type(c))
x = 10
y = 5
def sum():                  # Day la bien toan cuc
    return x + y
print(sum())

def sum(e ,f):              # Day la bien cuc bo
    sum = e + f
    return sum
print(sum(7, 8))


g, h, i = 10, 30.5, "Tuan"
print(g)
print(h)
print(i)
k = l = m = "Banh Chung"
print(k)
print(l)
print(m)


name = "Ha Le Tuan"
print("Xin chao "+ name)
n = 10
N = "Toi ten la gi"
print(n)
print(N)


age = 9
if age < 10:
    print("Ban la thieu nhi")
elif age < 17:
    print("Ban la tre vi thanh nien")
else:
    print("Ban la nguoi lon")

