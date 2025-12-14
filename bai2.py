n = int(input("Nhap so nguyen:"))
lst = []
i = 2
while n > 1:
    if n % i == 0:
        lst.append(i)
        n //= i
    else:
        i += 1
print(f"{n} duoc phan tich thanh {lst}")