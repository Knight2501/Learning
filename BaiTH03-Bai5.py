#5. Chuyển list sang set
n = input("Nhap chuoi: ")
lst = [].lower()
for i in range(len(n)):
    lst.append(input().lower())
set_lst = set(lst)
print("Day sau khi chuyen doi la:",set_lst)