class Students:
    ...
s1 = Students()
print(type(s1))


class Students:
    def __init__(ban_than,ten,tuoi):
        ban_than.ten = ten
        ban_than.tuoi = tuoi
s1 = Students("Bao",18)
print(s1.ten)
print(s1.tuoi)
s2 = Students("Nhat",18)
print(s2.ten)
print(s2.tuoi)

class Students:
    def __init__(self,ten,tuoi):
        self.ten = ten
        self.tuoi = tuoi
    def thong_tin(self):
        print(f"Ten: {self.ten}, Tuoi: {self.tuoi}")

bao = Students("Bao",18)
bao.thong_tin()


class Card:
    def __init__(self,loai,ten,gia):
        self.loai = loai
        self.ten = ten
        self.gia = gia
    
    def thong_tin(self):
        print(f"Loai: {self.loai}, Ten: {self.ten}, Gia: {self.gia}")

card1 = Card("Card On Board","Intel Graphics","0")
card1.thong_tin()
print(f"Card 1. Loai: {card1.loai}, Ten: {card1.ten}, Gia: {card1.gia}")

card2 = Card("Card Roi","Nvidia GTX 3060", "700$")
card2.thong_tin()
print(f"Card 2. Loai: {card2.loai}, Ten: {card2.ten}, Gia: {card2.gia}")


class NganHang:
    def __init__(self,ten_khach,so_du):
        self.ten_khach = ten_khach
        self.__so_du = so_du

    def hien_thi_so_du(self):
        print("So du khach:",self.__so_du)

        acc = NganHang("Dinh Nguyen Trong Bao",10000)
        acc.hien_thi_so_du() ##Lỗi không hiển thị số dư

class NganHang:
        def __init__ (self,ten_khach,so_du):
            self.ten_khach = ten_khach
            self.__so_du = so_du
    
        def hien_thi_so_du(self):
            print("So du khach:",self.__so_du)

        def rut_tien(self,so_tien):
            if so_tien > self.__so_du:
                print("So tien trong tai khoan cua quy khach khong du de rut tien")
            else:
                self.__so_du -= so_tien 
                print(f"Quy khach da rut thanh cong {so_tien} trong tai khoan.So du con lai la {self.__so_du}")
        
        def nap_tien(self,so_tien):
            self.__so_du += so_tien
            print(f"Quy khach da nap thanh cong {so_tien} vao tai khoan.So du hien tai la {self.__so_du}")

acc = NganHang("Ha Le Anh Tuan",5000)
acc.nap_tien(20000)
acc.hien_thi_so_du()


class nguoi:
    def __init__(ban_than,ten):
        ban_than.ten = ten

    def gioi_thieu(ban_than):
        print(f"Xin chao,toi la {ban_than.ten}")

class hoc_sinh(nguoi):
    def hoc_tap(ban_than):
        print(f"{ban_than.ten} dang hoc tap mon lap trinh Python huong doi tuong !")

hs1 = hoc_sinh("Ha Le Anh Tuan")
hs1.gioi_thieu()
hs1.hoc_tap()

class hoc_sinh(nguoi):
    def gioi_thieu(self):
        print(f"SInh vien: {self.ten}")

hs2 = hoc_sinh("To Duc Huy Hoang")
hs2.gioi_thieu()

class meo:
    def tieng(ban_than):
        print("Meo meo!")

class cho:
    def tieng(ban_than):
        print("Gau gau!")

animals = [meo(),cho()]

for dong_vat in animals:
    dong_vat.tieng()

