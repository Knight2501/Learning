n = int(input("Nhap so nguyen cua ban: "))
if n < 0:
    print("Sai dieu kien.Vui long nhap lai.")
else:
    k = 1
    while n // k >= 10:
        k *= 10
        while k >= 1:
            chu_so = n // k
            print(chu_so,end =" ")
            m = n % k
            k //= 10
print(f"Cac chu so cua so nguyen la: ",m)
