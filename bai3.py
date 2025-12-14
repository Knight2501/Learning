n = int(input("Nhap so nguyen duong:"))
lst = []
for a in range(n + 1):
    b = n - a 
    lst.append([a, b])
print(lst)