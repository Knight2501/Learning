a,b,c = map(int,input().split())
if a < 0 and b < 0 and c < 0:
    print("So canh cua tam giac khong the am duoc!")
elif a == b or a == c or b == c:
    print("Tam giac can")
elif a == b == c:
    print("Tam giac deu")
elif a * a + b * b == c * c or a * a + c* c == b * b or b * b + c * c == a * a:
    print("Tam giac vuong")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Khong phai tam giac")
elif a + b > c or a + c > b or b + c > a:
    print("Tam giac thuong")
