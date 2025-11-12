ten = ["Tuan","Tuan","Anh","Ha Le"]
remove = set(ten)
print(remove)
so = [1, 2, 2, 2, 3, 4, 4, 5, 6]
so_moi = set(so)
print(so_moi)
set_khong = set()
so ={18, 20 ,22}
so.add(24)
so.update([30, 33, 36])
print(so)
set(so)
print(so)
so.remove(18)
print(so)
so.discard(27)
print(so)
so.pop()
print(so)
so.clear()
print(so)

so_moi = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for so_chan in so_moi:
    if so_chan % 2 == 0:
        print(f"{so_chan} la so chan")

binh_phuong_so = {x ** 2 for x in range(10)}
print(binh_phuong_so)
print(len(so_moi))
print(10 in so_moi)
print("con ho" not in so_moi)