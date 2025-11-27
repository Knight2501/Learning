#13. Tìm giao, hợp và hiệu của hai set
set1 = input("Nhap set 1:")
set2 = input("Nhap set 2:")
giao = set1.intersection(set2)
hop = set1.union(set2)
hieu = set1.difference(set2)
print("Giao cua 2 set la:",giao)
print("Hop cua 2 set la:",hop)
print("Hieu cua 2 set la:",hieu)