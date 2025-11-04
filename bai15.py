#Bài 15:Vẽ ngôi sao 
n = int(input("Nhập số cần nhập để tạo ra ngôi sao: "))
for i in range(1,n + 1):
    for j in range(i):
        print("*",end ="")
    print()


n = int(input("Nhập số cần nhập để tạo ra ngôi sao ngược: "))
for i in range(n, 1):
    for j in range(i):
        print("*",end= "")
    print()

n = int(input("Nhập số cần nhập để tạo ra ngôi sao ngược: "))
for i in range(n, 0, -1):
    for j in range(i):
        print("*",end= "")
    print()

n = int(input("Nhập số cần nhập để tạo ra ngôi sao: "))
for i in range(1,n + 1):
    print(" " * (n - i) * "*" * (i*2 - 1))