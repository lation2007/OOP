import math

class Diem:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

class DoanThang:
    def __init__(self, *args):
        if len(args) == 0:
            self.__d1 = Diem(8, 5)
            self.__d2 = Diem(1, 0)

        elif len(args) == 2 and isinstance(args[0], Diem):
            self.__d1 = args[0]
            self.__d2 = args[1]

        elif len(args) == 4:
            self.__d1 = Diem(args[0], args[1])
            self.__d2 = Diem(args[2], args[3])

        elif len(args) == 1 and isinstance(args[0], DoanThang):
            mau_goc = args[0]
            self.__d1 = Diem(mau_goc.get_d1().x, mau_goc.get_d1().y)
            self.__d2 = Diem(mau_goc.get_d2().x, mau_goc.get_d2().y)
        
        else:
            print("Loi: Tham so dau vao khong dung!")

    def get_d1(self): return self.__d1
    def get_d2(self): return self.__d2

    def set_d1(self, diem_moi): self.__d1 = diem_moi
    def set_d2(self, diem_moi): self.__d2 = diem_moi

    def tinh_do_dai(self):
        dx = self.__d1.x - self.__d2.x
        dy = self.__d1.y - self.__d2.y
        return math.sqrt(dx**2 + dy**2)

    def hien_thi(self):
        print(f"DoanThang [D1{self.__d1} -> D2{self.__d2}] | Do dai: {self.tinh_do_dai():.2f}")

print("--- 📏 KIEM TRA DOAN THANG ---")

dt1 = DoanThang()
dt1.hien_thi()

pA = Diem(0, 0)
pB = Diem(3, 4)
dt2 = DoanThang(pA, pB)
print("\nBan dau:", end=" ")
dt2.hien_thi()
pA.x = 10 
print("Sau khi sua Diem goc pA.x = 10:", end=" ")
dt2.hien_thi()

dt3 = DoanThang(1, 1, 5, 5)
print("\nKhoi tao tu 4 toa do:", end=" ")
dt3.hien_thi()

dt4 = DoanThang(dt3)
dt3.get_d1().x = 99
print("\nSau khi sua dt3, kiem tra dt4 (Deep Copy):")
print("dt3 bi sua:", end=" "); dt3.hien_thi()
print("dt4 giu nguyen:", end=" "); dt4.hien_thi()