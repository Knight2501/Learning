#11. Gộp hai dictionary
n = input("Nhap dictionary thu nhat:")
m = input("Nhap dictionary thu hai:")
gop = n.copy()
for gia_tri in m.copy():
    if gia_tri not in gop:
        gop[gia_tri] = m[gia_tri]
    else:
        gop[gia_tri] += m[gia_tri]
print("Dictionary sau khi gop la:",gop)