#19.Tìm cặp phần tử có tổng gần nhất với số 
def tim_tong_gan_nhat(n, N):
    n.sort()
    cap_gan_nhat = None
    khoang_cach_nho_nhat = float('inf')
    T,P = 0 , len(n) - 1
    while T < P:
        tong = n[T] + n[P]
        khoang_cach = abs(N - tong)
        if khoang_cach < khoang_cach_nho_nhat:
            khoang_cach_nho_nhat = khoang_cach
            cap_gan_nhat = (n[T], n[P])
        if tong < N:
            T += 1
        else:
            P -= 1
    return cap_gan_nhat