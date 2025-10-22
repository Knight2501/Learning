sinh_vien = ["Tuan", "Bao", "Quyen"]
print(sinh_vien)
print(sinh_vien[0])
print(sinh_vien[-1])
print(sinh_vien[0:1])
print(sinh_vien[-1:0])
so_sinh_vien = len(sinh_vien)
print(so_sinh_vien)
for i in range(so_sinh_vien):
    print(i,so_sinh_vien[i])

for i in sinh_vien:
    print(sinh_vien)

print("Sinh viên trước khi thay đổi là: ",sinh_vien)
sinh_vien[1] = "Nga"
print("Sinh viên sau khi thay đổi là: ",sinh_vien)

sao_chep = sinh_vien.copy()
sinh_vien[2] = "Matcha Latte"
print(sinh_vien)

list = [10, 20, 30, 40, 50, 60]
#C1:
for i in list:
    list[i] += 2
    print(list)
## 12,22,32,42,52,62

#C2
list = [x + 2 for x in list]
print(list)
## 12,22,32,42,52,62

#C3
list = list(map(lambda x: x + 2, list))
print(list)
## 12,22,32,42,52,62

#C4
for i in range(len(list)):
    list += i
print(list)
## 11, 22, 33, 44, 55, 66

for index,value in enumerate(list):
    list[index] = value + 2
print(list)

def element_change(lst, old_value, new_value):
    return [new_value if x == old_value else x for x in lst]

list = [[10, 20, 30, 40, 50, 60], [70, 80, 90, 100], [110, 120, 130, 140]]
list = element_change(list, 20, 36)
print(list)
list[0][5] = 69
print(list)
list = filter(lambda x: x % 2 == 0, list)
print(list)

from functools import reduce
list2 = [10, 20, 30, 40]
tong = reduce(lambda x, y: x + y, reduce)
print(tong)

list3 = [100,200,300]
list4 = [400,500,600]
x = list3
y = list4
result = [x + y for x + y in zip(list3,list4)]
print(result)

import itertools
list5 = [(1,2), (3,4), (5,6)]
result_1 = list(itertools.starmap(lambda x, y: x + y, list5))
print(list5)

list_moi = list3 + list4
print(list_moi)
del(list[2])
da_xoa = list3.pop(2)
print(da_xoa)
list3.remove(100)
print(list3)
n = list3.reverse()
print(n)

