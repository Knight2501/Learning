tuple = input()
x = int(input())
count = 0 
for i in tuple:
    if i == str(x):
        count += 1
print(f" So {x} xuat hien {count} lan trong tuple")
